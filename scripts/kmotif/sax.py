# implementation of SAX algorithm

import string
import math

import numpy as np
import scipy.stats

import sequitur


STD_EPS = 1e-6


def normalize(a):
    if a.std() < STD_EPS:
        return np.zeros_like(a)
    else:
        return (a - a.mean()) / a.std()


# source: https://stackoverflow.com/a/27609714/2124834
def greedy_split(arr, n, axis=0):
    """Greedily splits an array into n blocks.

    Splits array arr along axis into n blocks such that:
        - blocks 1 through n-1 are all the same size
        - the sum of all block sizes is equal to arr.shape[axis]
        - the last block is nonempty, and not bigger than the other blocks

    Intuitively, this "greedily" splits the array along the axis by making
    the first blocks as big as possible, then putting the leftovers in the
    last block.
    """
    length = arr.shape[axis]
    # compute the size of each of the first n-1 blocks
    block_size = int(np.ceil(length / float(n)))
    # the indices at which the splits will occur
    ix = np.arange(block_size, length, block_size)
    return np.array(np.split(arr, ix, axis))

def bins(a,alpha):
    return np.array([scipy.stats.norm.ppf(x/alpha) for x in range(1,alpha)]) * np.nanstd(a) + np.nanmean(a)
    #return np.array([scipy.stats.norm.ppf(x/alpha) for x in range(1,alpha)]) * a.std().data + a.mean().data

def split(a,w):
    g = w*math.ceil(len(a)/w)
    return np.pad(a,(0,g-len(a)),'edge').reshape((int(g/w),-1))

def sax(a,w,bins):
    segments = split(a, w)
    means = segments.mean(axis=1)
    digits = np.digitize(means, bins + [1])
    return tuple(digits)


def numerosity(l):
    r = [(l[0],1)]
    for e in l[1:]:
        if e == r[-1][0]:
            r[-1] = (e, r[-1][1] + 1)
        else:
            r.append([e,1])
    return np.array(r)


def subsax(a,w,n,overlap,bins):
    shape = (len(a) - n + 1, n)
    strides = [a.dtype.itemsize] * 2
    all_subsequences = np.lib.stride_tricks.as_strided(a, shape, strides)
    subsequences = all_subsequences[::int(max(1, round(n * (1 - overlap))))]
    sax_words = [sax(s, w, bins) for s in subsequences]
    return np.array(sax_words) # np.array(numerosity(sax_words))

if __name__ == '__main__':

    #a = np.array([0,1,2,0,5,5] * 5)
    #a = sax(a,5,4,0)

    a = np.array([0,1,2,3,4,5,6,7,8,9,8,7,8,9,8,7,6,5,4,3,2,1,0])

    #w = 5
    #dsize = 8
    #shape = (len(a) - dsize - 1, w)
    #strides = (dsize, dsize)
    #a = np.lib.stride_tricks.as_strided(a, shape, strides)
    #print(a)

    bins = bins(a,alpha=5)
    r = sax(a, w=5, bins=bins)
    print('input:')
    print(a)
    print('output:')
    print(r)

    #plt.plot(a)
    #plt.show()


    #TIMING TESTS FOR CHARACTERS VS TUPLES AS SYMBOLS

    # import timeit
    #
    # setup = '''
    # import random
    # import string
    # x = ''.join(random.choice(string.ascii_letters) for _ in range(2))
    # y = ''.join(random.choice(string.ascii_letters) for _ in range(2))
    # '''
    #
    # r = timeit.Timer('x==y',setup=setup).repeat(7,1000)
    #
    # setup = '''
    # import random
    # import string
    # import numpy as np
    # x = np.array([random.randint(0,4) for _ in range(5)])
    # y = np.array([random.randint(0,4) for _ in range(5)])
    # '''
    #
    # t = timeit.Timer('(x-y<0.1).all()',setup=setup).repeat(7,1000)
    #
    # print(min(r))
    # print(min(t))

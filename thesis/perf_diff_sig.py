import scipy.spatial.distance
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set(style='white')

string = """  Full Data & $ 0.64 \pm 0.16 $ & $ 0.72 \pm 0.22 $ & $ 0.70 \pm 0.14 $ & $ 0.56 \pm 0.16 $ & $ 0.59 \pm 0.13 $ \\
Variable means and variances & $ 0.68 \pm 0.13 $ & $ 0.71 \pm 0.15 $ & $ 0.66 \pm 0.12 $ & $ 0.66 \pm 0.16 $ & $ 0.68 \pm 0.10 $ \\
Jesse Zwamborn's project & $ 0.76 \pm 0.12 $ & $ 0.77 \pm 0.14 $ & $ 0.78 \pm 0.10 $ & $ 0.74 \pm 0.14 $ & $ 0.78 \pm 0.09 $ \\
T-patterns & $ 0.83 \pm 0.16 $ & $ 0.80 \pm 0.13 $ & $ 0.88 \pm 0.15 $ & $ 0.84 \pm 0.16 $ & $ 0.81 \pm 0.20 $ \\
$k$-motifs & $ 0.86 \pm 0.10 $ & $ 0.88 \pm 0.07 $ & $ 0.87 \pm 0.09 $ & $ 0.69 \pm 0.17 $ & $ 0.94 \pm 0.05 $"""


data = []
labels = []
for line in string.split('\n'):
    mean,std =[float(x.strip('$ ')) for x in line.split('&')[1].split('\\pm')]
    data.append([mean,std])
    labels.append(line.split('&')[0].strip())


r = scipy.spatial.distance.pdist(data, metric=lambda x,y: scipy.stats.ttest_ind_from_stats(x[0], x[1], 10, y[0], y[1], 10)[1])

a = np.array(scipy.spatial.distance.squareform(r))
np.fill_diagonal(a,1)
a = a < 0.05

mask = np.zeros_like(a, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
np.fill_diagonal(mask,False)

g = sns.heatmap(a, mask=mask, square=True, cmap='viridis', linewidths=.5, cbar=False)
g.set_xticklabels(labels, rotation=90)
g.set_yticklabels(reversed(labels), rotation=0)
#plt.show()
fig = g.get_figure()
fig.savefig("images/perf_sig.png", dpi=300, bbox_inches='tight')
import numpy as np

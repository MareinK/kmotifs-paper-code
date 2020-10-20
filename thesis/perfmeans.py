import numpy as np

string = """  Full data & 0.64 \pm 0.16 & 0.72 \pm 0.22 & 0.7 \pm 0.14 & 0.56 \pm 0.16 & 0.59 \pm 0.13
  Means and variances & 0.68 \pm 0.13 & 0.71 \pm 0.15 & 0.66 \pm 0.12 & 0.66 \pm 0.16 & 0.68 \pm 0.10
  Jesse's project & 0.77 \pm 0.12 & 0.77 \pm 0.14 & 0.78 \pm 0.10 & 0.74 \pm 0.14 & 0.78 \pm 0.09
  T-patterns & 0.83 \pm 0.16 & 0.80 \pm 0.13 & 0.88 \pm 0.15 & 0.84 \pm 0.16 & 0.81 \pm 0.20
  $k$-motifs & 0.86 \pm 0.09 & 0.85 \pm 0.13 & 0.90 \pm 0.07 & 0.73 \pm 0.10 & 0.95 \pm 0.06"""

a = []
for line in string.split('\n'):
    l = []
    for part in line.split('&')[1:]:
        x, y = part.split('\pm')
        l.append([float(x),float(y)])
    a.append(l)
a = np.array(a)
print(a.mean(axis=0))

from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")
d = pd.read_csv("../data/EEG data.csv", header=None, index_col=False)
d.columns = ['Subject ID', 'Video ID', 'Attention', 'Mediation', 'Raw', 'Delta', 'Theta', 'Alpha 1', 'Alpha 2', 'Beta 1', 'Beta 2', 'Gamma 1', 'Gamma 2', 'Predefined Label', 'User-Defined Label']
d = d.drop(d.columns[[0, 1, 2, 3, 4, 13, 14]], axis=1)
corr = d.corr()

mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

f, ax = plt.subplots(figsize=(11, 9))

cmap = sns.diverging_palette(220, 10, as_cmap=True)

sns.heatmap(corr, mask=mask,
            square=True,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

plt.show()
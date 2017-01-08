# Experiment 1
'''
Exclude all except [0]
Output [14]
'''
# pylint: disable=C0103
from data.data import EEG
import numpy as np
from sklearn.model_selection import train_test_split

X = EEG[:, [0, 1]]
y = EEG[:, [14]].reshape(12811, )
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
    )

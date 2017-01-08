'''
Random Forest
'''
# pylint: disable=C0103
from sklearn.ensemble import RandomForestClassifier
from data import *

rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(only_eeg.X_train, only_eeg.y_train)
print(rfc.score(only_eeg.X_test, only_eeg.y_test))
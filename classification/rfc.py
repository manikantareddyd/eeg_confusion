'''
Random Forest
'''
# pylint: disable=C0103
from sklearn.ensemble import RandomForestClassifier
from data import *

rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(only_subject.X_train, only_subject.y_train)
print(rfc.score(only_subject.X_test, only_subject.y_test))
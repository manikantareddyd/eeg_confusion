"""
Module for Preprocessing Data
"""
# pylint: disable=C0103

from config import *
from numpy import genfromtxt


EEG = genfromtxt(EEG_DATA, delimiter=",")
# DMG = genfromtxt(DMG_DATA, delimiter=",")

'''
[0]: Subject ID
[1]: Video ID
[2]: Attention (Proprietary measure of mental focus)
[3]: Mediation (Proprietary measure of calmness)
[4]: Raw (Raw EEG signal)
[5]: Delta (1-3 Hz of power spectrum)
[6]: Theta (4-7 Hz of power spectrum)
[7]: Alpha 1 (Lower 8-11 Hz of power spectrum)
[8]: Alpha 2 (Higher 8-11 Hz of power spectrum)
[9]: Beta 1 (Lower 12-29 Hz of power spectrum)
[10]: Beta 2 (Higher 12-29 Hz of power spectrum)
[11]: Gamma 1 (Lower 30-100 Hz of power spectrum)
[12]: Gamma 2 (Higher 30-100 Hz of power spectrum)
[13]: predefined label (whether the subject is expected to be confused)
[14]: user-defined label (whether the subject is actually confused)
'''

'''
SUBJECT_ID = 0	25	Han Chinese	  M
SUBJECT_ID = 1	24	Han Chinese	  M
SUBJECT_ID = 2	31	English	      M
SUBJECT_ID = 3	28	Han Chinese	  F
SUBJECT_ID = 4	24	Bengali	      M
SUBJECT_ID = 5	24	Han Chinese	  M
SUBJECT_ID = 6	24	Han Chinese	  M
SUBJECT_ID = 7	25	Han Chinese	  M
SUBJECT_ID = 8	25	Han Chinese	  M
SUBJECT_ID = 9	24	Han Chinese	  F
'''

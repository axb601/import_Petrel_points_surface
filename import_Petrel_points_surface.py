# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:51:11 2020

@author: BIRCHHAWKINS
"""

"""
This is a script for importing a Petrel surface as a Pandas dataframe
The Petrel surface must be converted to a point set within Petrel and exported as Irap classic points (ASCII)
It is useful to convert the Z values to positive integers

"""

import pandas as pd

with open('C:\\Users\\BIRCHHAWKINS\\Python\\data\\NTO', 'r') as f:
    data = pd.read_csv(f, sep=" ", names=["X", "Y", "Z"])

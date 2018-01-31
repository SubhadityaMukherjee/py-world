import csv,os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline

os.chdir(os.getcwd())
data = pd.read_csv('fd-export.csv')
print(data.plot())

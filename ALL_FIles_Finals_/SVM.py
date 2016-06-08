
# coding: utf-8

# In[1]:

#Trying SVM with linear Kernal and BPF


# In[4]:

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split 
from sklearn import metrics
import warnings
import seaborn as sns
import numpy as np
sns.plt.show
get_ipython().magic('matplotlib inline')
from sklearn import svm

import os


# In[6]:

pd_close = pd.read_csv("Final\Eye_close.csv")
pd_open = pd.read_csv("Final\Eye_open.csv")
data = pd.read_csv("Final\Date.csv")


# In[7]:

X = pd.concat([pd_close, pd_open], ignore_index=True)


# In[9]:

y = pd.read_csv("Final\Target.csv")


# In[10]:

y=y.values.ravel()


# In[ ]:

NSVM= range(1,100)
scores = []
for n in NSVM:
    clf = svm.SVC(kernel="linear", C=0.025)
    clf.fit(X,y)
    X_train,X_test,y_train,y_test=train_test_split (X,y,test_size=0.75)
    y_hat= clf.predict(X_test)
    scores.append(metrics.accuracy_score(y_test,y_hat))


# In[ ]:




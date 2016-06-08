
# coding: utf-8

# In[1]:

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


# In[2]:

with warnings.catch_warnings():
    warnings.simplefilter("ignore")


# In[3]:

pd_close = pd.read_csv("Eye_close.csv")
pd_open = pd.read_csv("Eye_open.csv")
data = pd.read_csv("Date.csv")


# In[4]:

X = pd.concat([pd_close, pd_open], ignore_index=True)


# In[5]:

y = pd.read_csv("Target.csv")


# In[ ]:

y=y.values.ravel()


# In[ ]:

Nlogreg= range(1,100)
scores = []
for n in Nlogreg:
    clf = LogisticRegression()
    clf.fit(X,y)
    X_train,X_test,y_train,y_test=train_test_split (X,y,test_size=0.75)
    y_hat= clf.predict(X_test)
    scores.append(metrics.accuracy_score(y_test,y_hat))


# In[ ]:

Scores_reg=(sum(scores)/len(scores))


# In[ ]:




# In[ ]:




# ### 

# In[ ]:

NSVM= range(1,1)
scores = []
for n in NSVM:
    cls = svm.SVC(kernel='linear',C='0.025')
    cls.fit(X,y)
    X_train,X_test,y_train,y_test=train_test_split (X,y,test_size=0.75)
    y_hat= cls.predict(X_test)
    scores.append(metrics.accuracy_score(y_test,y_hat))


# In[ ]:

Scores_SVM=(sum(scores)/len(scores))


# In[ ]:

print ('Accuracy of Logistic is :{}'.format(Scores_reg))


# In[ ]:

print ('Accuracy of SVM is :{}'.format(Scores_SVM))


# In[ ]:




# In[ ]:




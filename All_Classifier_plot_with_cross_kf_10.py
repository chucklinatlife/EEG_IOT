
# coding: utf-8

# In[7]:

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split 
from sklearn import metrics
import seaborn as sns
import numpy as np
from sklearn import svm
from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
get_ipython().magic('matplotlib inline')
from sklearn import preprocessing
from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as ply
import numpy as np
import plotly.plotly as py
import plotly.tools as tls
py.sign_in('MohammedAlnemari', 'll40wpx72n')


# In[64]:

X = pd.read_csv("Date_new_learning - Date.csv")
X=X.as_matrix()
X =preprocessing.normalize(X,norm='l2')                    
y = pd.read_csv("Target_new_160 - Sheet1.csv")
y=y.as_matrix()
y=y.ravel()


# In[65]:

#K = range(1,100)
#Classifier = []
#for n in Classifier_range:
clf = KNeighborsClassifier(8)
clf= clf.fit(X,y)
scores_KNN=cross_val_score(clf,X,y,cv=80,scoring="accuracy")
#y_hat= clf.predict(X_test)
#    Classifier.append(Classifier)
scores_KNN=(sum(scores_KNN)/len(scores_KNN))
print ('Accuracy of KNN_3 is :{}'.format(scores_KNN))    
#plt.plot(Classifier_range,scores)
#plt.xlabel("Classifier range")
#plt.ylabel("Testing Accuracy")


# In[10]:

#Classifier_range = range(1,10)
#scores = []
#for n in Classifier_range:
clf1 = SVC(kernel="linear", C=0.025)
clf1.fit(X,y)
Scores_SVCL=cross_val_score(clf1,X,y,cv=10,scoring="accuracy")
#y_hat= clf1.predict(X_test)
Scores_SVCL=(sum(Scores_SVCL)/len(Scores_SVCL))
print ('Accuracy of sSVC(kernel="linear", C=0.025) is :{}'.format(Scores_SVCL))     
#plt.plot(Classifier_range,scores)
#plt.xlabel("Classifier range")
#plt.ylabel("Testing Accuracy")


# In[11]:

#Classifier_range = range(1,100)
#scores = []
#for n in Classifier_range:
clf2 = SVC(kernel ='rbf',gamma=2, C=1)
clf2.fit(X,y)
#   X_train,X_test,y_train,y_test=train_test_split (X,y,test_size=0.75)
#y_hat= clf2.predict(X_test)
Scores_SVC_G= cross_val_score(clf2,X,y,cv=10,scoring="accuracy")
#    scores.append(metrics.accuracy_score(y_test,y_hat))    
Scores_SVC_G=(sum(Scores_SVC_G)/len(Scores_SVC_G))
print ('Accuracy of SVC(gamma=2, C=1) is :{}'.format(Scores_SVC_G))   
#plt.plot(Classifier_range,scores)
#plt.xlabel("Classifier range")
#plt.ylabel("Testing Accuracy")


# In[12]:

#Classifier_range = range(1,100)
#scores = []
#for n in Classifier_range:
clf3 = DecisionTreeClassifier(max_depth=5)
clf3.fit(X,y)
#X_train,X_test,y_train,y_test=train_test_split (X,y,test_size=0.50)
Scores_DecisionTreeClassifier = cross_val_score(clf3,X,y,cv=10,scoring="accuracy")

#y_hat= clf3.predict(X_test)
#scores.append(metrics.accuracy_score(y_test,y_hat))    
Scores_DecisionTreeClassifier=(sum(Scores_DecisionTreeClassifier)/len(Scores_DecisionTreeClassifier))
print ('Accuracy of DecisionTreeClassifier(max_depth=5) is :{}'.format(Scores_DecisionTreeClassifier))   
#plt.plot(Classifier_range,scores)
#plt.xlabel("Classifier range")
#plt.ylabel("Testing Accuracy")


# In[13]:

#Classifier_range = range(1,100)
#scores = []
#for n in Classifier_range:
clf4 = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=2)
clf4.fit(X,y)
#X_train,X_test,y_train,y_test=train_test_split (X,y,test_size=0.75)
Scores_RandomForestClassifier= cross_val_score(clf2,X,y,cv=10,scoring="accuracy")
#y_hat= clf.predict(X_test)
#scores.append(metrics.accuracy_score(y_test,y_hat))    
Scores_RandomForestClassifier=(sum(Scores_RandomForestClassifier)/len(Scores_RandomForestClassifier))
print ('Accuracy of RandomForestClassifier :{}'.format(Scores_RandomForestClassifier)) 
#plt.plot(Classifier_range,scores)
#plt.xlabel("Classifier range")
#plt.ylabel("Testing Accuracy")


# In[15]:

#Classifier_range = range(1,100)
#scores = []
#for n in Classifier_range:
clf5 = AdaBoostClassifier()
clf5.fit(X,y)
#X_train,X_test,y_train,y_test=train_test_split (X,y,test_size=0.75)
Scores_AdaBoostClassifier= cross_val_score(clf5,X,y,cv=10,scoring="accuracy")
#y_hat= clf.predict(X_test)
#scores.append(metrics.accuracy_score(y_test,y_hat))    
Scores_AdaBoostClassifier=(sum(Scores_AdaBoostClassifier)/len(Scores_AdaBoostClassifier))
print ('Accuracy of AdaBoostClassifier is :{}'.format(Scores_AdaBoostClassifier))
#plt.plot(Classifier_range,scores)
#plt.xlabel("Classifier range")
#plt.ylabel("Testing Accuracy")


# In[19]:

Classifiers_name_sores= ['AdaBoost:'+str(Scores_AdaBoostClassifier)+ "|"+'RandomForest:'+str(Scores_RandomForestClassifier)+
                       "|"+'DecisionTree : '+str (Scores_DecisionTreeClassifier)+ "|"+'SVCG :'+ str (Scores_SVC_G)+ "|"+'SVCL:'+str(Scores_SVCL) 
                      +"|"  +'KNN :' + str (scores_KNN)]


# In[21]:

Classifiers_scores = [(Scores_AdaBoostClassifier),(Scores_RandomForestClassifier)
                       ,(Scores_DecisionTreeClassifier),(Scores_SVC_G),(Scores_SVCL) 
                     ,(scores_KNN)]


# In[68]:

colors = ['b', 'c', 'y', 'm', 'r','k']

lo = ply.scatter(no_clf[0], clf_scores[0], marker='o',s=100,color=colors[2])
ll = ply.scatter(no_clf[1], clf_scores[1], marker='o',s=100,color=colors[0])
l  = ply.scatter(no_clf[2], clf_scores[2], marker='o',s=100,color=colors[1])
a  = ply.scatter(no_clf[3], clf_scores[3], marker='x',s=100,color=colors[5])
h  = ply.scatter(no_clf[4], clf_scores[4], marker='o',s=100,color=colors[3])
hh = ply.scatter(no_clf[5], clf_scores[5], marker='o',s=100,color=colors[4])

text = iter(['AdaBoost' , 'Random Forest' , 'Decision Tree ' ,  'SVM with Gamma ' ,  'SVM with Linear ' , ' KNN_3'])


mpl_fig = plt.gcf()
plotly_fig = tls.mpl_to_plotly( mpl_fig )

for dat in plotly_fig['data']:
    t = text.__next__()
    dat.update({'name': t, 'text':t})

plotly_fig['layout']['showlegend'] = True
py.plot(plotly_fig)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[67]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[52]:




# In[57]:




# In[ ]:




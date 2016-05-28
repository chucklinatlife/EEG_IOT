import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
get_ipython().magic(u'matplotlib inline')


open_ds = pd.read_csv("eopen_high_alphatext.txt")
close_ds = pd.read_csv("eclosed_high_alphatext.txt")


#here just check moving mean 
open_ds["sma_10"] = pd.stats.moments.rolling_mean(open_ds["0"], 10)
close_ds["sma_10"] = pd.stats.moments.rolling_mean(close_ds["0"], 10)

#here label the open with 0 
ds = pd.DataFrame()
ds["sma_10"] = open_ds["sma_10"][10:].values
ds["label"] = 0

#here label the close with 1 
ds_c = pd.DataFrame()
ds_c["sma_10"] = close_ds["sma_10"][10:].values
ds_c["label"] = 1
ds_c

#concat both 
ds = pd.concat([ds, ds_c], ignore_index=True)
ds

#the classifier 
cls = LogisticRegression()


ds.sma_10
ds.label


#learning the classifer 
cls.fit(ds[["sma_10"]], ds.label)

#the accuracy of the classifer 
cls.score(ds[["sma_10"]], ds.label)


#split data to train and test 
x_train,x_test,y_train,y_test = train_test_split(ds[["sma_10"]], ds.label, train_size=0.75)

#do the same traning 
cls.fit(x_train, y_train)


#percentage of train 
cls.score(x_train, y_train)

#percentage of the test
cls.score(x_test, y_test)

#predict on the incomeing data 
cls.predict("Put the incoming data ")


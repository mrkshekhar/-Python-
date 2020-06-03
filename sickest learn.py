#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
test_idx = [0,50,100]

#training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print (test_target)
print (clf.predict(test_data))

#viz code

# test data

print (test_data[1],test_target[1])
print (iris.feature_names,iris.target_names)


# In[1]:


# Import
from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree
iris = load_iris()

# Showing the data (this part I changed too)
print(iris.data[0])
print(iris.target[0])
for i in range(len(iris.target)):
    print('Example {},\t label {},\t features {}'.format(i , iris.target[i] , iris.data[i]))

# Training data
test_idx = [0,50,100]
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# Testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print(test_target)
print(clf.predict(test_data))

# Exporting the decision tree
from sklearn.externals.six import StringIO
import pydot

dot_data = StringIO()

tree.export_graphviz(clf,
                     out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     impurity=False)

# I used this module (graphviz) to generate the graph
import graphviz as gp
graph = gp.Source(dot_data.getvalue())
graph.render("iris", view = True)


# In[3]:


pip install pydot


# In[2]:


pip install graphviz


# In[ ]:





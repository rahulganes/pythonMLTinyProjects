
# coding: utf-8

# In[39]:


from sklearn import tree
#x=[height,weight]
X =[[160,60],[160,40],[160,90],[150,50],[150,40],[150,60],[170,70],[170,40],[170,100],[155,55],[155,30],[155,70]]
Y = ['perfect','underweight','overweight','perfect','underweight','overweight','perfect','underweight','overweight','perfect','underweight','overweight']

bmidetector = tree.DecisionTreeClassifier()
bmidetector.fit(X,Y)
height = int(input("enter your height:"))
weight = int(input("enter your weight:"))
prediction = bmidetector.predict([[height,weight]])
print(prediction)


# In[35]:


print("rahul")


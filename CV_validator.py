
# coding: utf-8

# In[35]:




from validate_email import validate_email
import DNS


from geopy.geocoders import Nominatim

addresslocation = input("Enter your Address here :")
geolocator = Nominatim(user_agent="Curriculum_Validator")
location = geolocator.geocode(addresslocation)
try:
    location.latitude
    a0 = 1
except:
    a0 = 0
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type

number = input("Enter your phone number with country code :")
try :
    if(carrier._is_mobile(number_type(phonenumbers.parse(number)))):
        a1 = 1
    else:
        a1 = 0 
except:    
    a1 = 0

emailid = input("Enter your email-id :")    
is_valid = validate_email(emailid,verify=True)
if is_valid == True:
    a3 = 1
else:
    a3 = 0
    
qual=input("Enter your qualification :")
qual_List = ['b.tech','b.e','B.Tech','B.E']
qualifi = qual.split()
seting = set(qualifi)&set(qual_List)
if seting != set():
    a4 = 1
else:
    a4 = 0

exp = int(input("Enter your experience(in numbers) :"))

if exp>6:
    a5 = 1
elif exp>3:
    a5 = 0
else:
    a5 = -1

describeyourselves = input("Describe yourselves :")
from textblob import TextBlob

analyse = TextBlob(describeyourselves)
if(analyse.sentiment.polarity>0.25):
    a2 = 1
elif(analyse.sentiment.polarity<0.25 )and(analyse.sentiment.polarity>-0.25):
    a2 = 0
else:
    a2 = -1

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree

dataset = pd.read_csv(r'C:\Users\rg\Desktop\ipynb\dataset\CV_dataset2.csv') #ENTER YOUR DATA SET HERE
X = dataset.iloc[:, :-1].values #ORIGINAL DATA
Y = dataset.iloc[:, 6].values

clf = tree.DecisionTreeClassifier()

clf.fit(X,Y)
print(a0,a1,a2,a3,a4,a5)
print("Verdict :") #PREDICTED RESULTS
print(clf.predict([[a0,a1,a4,a3,a2,a5]]))

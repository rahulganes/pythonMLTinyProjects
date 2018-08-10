
# coding: utf-8

# In[35]:



from geopy.geocoders import Nominatim

addresslocation = input("Enter YOur Address here :")
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
describeyourselves = input("Describe yourselves :")
from textblob import TextBlob

analyse = TextBlob(describeyourselves)
if(analyse.sentiment.polarity>0.25):
    a2 = 1
elif(analyse.sentiment.polarity<0.25 )and(analyse.sentiment.polarity>-0.25):
    a2 = 0
else:
    a2 = -1

from sklearn import tree

clf = tree.DecisionTreeClassifier()

X = [[0,0,-1],[0,0,0],[0,0,1],[0,1,-1],[0,1,0],[0,1,1],[1,0,-1],[1,0,0],[1,0,1],[1,1,-1],[1,1,0],[1,1,1]]
Y = ['Highly Risky','Risky','Intermediate','Risky','Intermediate','Good','Risky','Intermediate','Good','Intermediate','Good','Excellent']

clf.fit(X,Y)

print("How trustworthy are you?")
print(clf.predict([[a0,a1,a2]]))


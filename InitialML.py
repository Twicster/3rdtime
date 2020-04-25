import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model, preprocessing, svm, metrics
from sklearn.utils import shuffle

data = pd.read_csv("GTExData.csv")  #load data in dataframe
DatPatLiv = pd.read_csv("PathologylistLiver.csv")
DatPatPan = pd.read_csv("PathologylistPancreas.csv")

#entries with both cirrhosis and steatosis. Edit data so it only reflects worst stage of the condition. Then check average fat content for these stages.
#for i in range(len(DatPatLiv)):
#    if data["Fat.Percentage_liver"][i]>=50:
#        print(data["Subject.ID"][i])
#steatosis, inflammation, fibrosis, cirrhosis, necrosis  (Here we work under the assumption inflammation is unique to these stages)
NAFLD=[0]*len(DatPatLiv)
for i in range(len(DatPatLiv)):
    if DatPatLiv["necrosis"][i]==1:
        NAFLD[i]=5
    elif DatPatLiv["cirrhosis"][i]==1:
        NAFLD[i]=4
    elif DatPatLiv["fibrosis"][i]==1:
        NAFLD[i]=3
    elif DatPatLiv["inflammation"][i]==1:
        NAFLD[i]=2
    elif DatPatLiv["steatosis"][i]==1:
        NAFLD[i]=1
    else:
        NAFLD[i]=0

le = preprocessing.LabelEncoder()   #For converting label entries to integer entries, like female to 0 and male to 1.
Gender=le.fit_transform(list(data["Sex"]))
Age=le.fit_transform(list(data["Age.Bracket"]))
Death=le.fit_transform(list(data["Hardy.Scale"]))

#Put data back in one dataframe, remove obsoletes.
datsam={"Stage": NAFLD, "Gender": Gender, "Age": Age, "congestion": DatPatLiv["congestion"],
        "hyperplasia": DatPatLiv["hyperplasia"], "nodularity": DatPatLiv["nodularity"],
        "hemorrhage": DatPatLiv["hemorrhage"], "atrophy": DatPatLiv["atrophy"], "infarction": DatPatLiv["infarction"],
        "no_abnormalities": DatPatLiv["no_abnormalities"], "hepatitis": DatPatLiv["hepatitis"],
        "sclerotic": DatPatLiv["sclerotic"], "scarring": DatPatLiv["scarring"], "hyalinization": DatPatLiv["hyalinization"],
        "pigment": DatPatLiv["pigment"], "ischemic_changes": DatPatLiv["ischemic_changes"]}
RevisedData=pd.DataFrame(data=datsam)

#data = data[["G1","G2","G3","studytime","failures","absences"]]  #trim data to the attributes we want
#We wish to predict grade 3 from the other data.
predict="Fat.Percentage_liver"
X = np.array(RevisedData)  #data, but without G3
Y = np.array(data[predict])           #Only liver values.

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X,Y,test_size=0.1)
for i in range(len(y_train)):
    y_train[i]=int(round(y_train[i]))
for i in range(len(y_test)):
    y_test[i]=int(round(y_test[i]))
#lab_enc = preprocessing.LabelEncoder()
#print(len(x_train), len(y_train))
#y_train1 = lab_enc.fit_transform(y_train)
#x_train1 = lab_enc.fit_transform(x_train)
#print(x_train1, y_train1)
clf = svm.SVC(kernel="poly")
clf.fit(x_train, y_train)
print(x_train)
y_pred = clf.predict(x_test)

acc= metrics.accuracy_score(y_test, y_pred)

print(acc)


#splits data into training and test data, makes (0.1=10%) of the data test data, so we train
# the model on the majority of data, but have some unknown to test on after.
#linear = linear_model.LinearRegression()
#linear.fit(x_train, y_train)
#acc = linear.score(x_test, y_test)
#print(acc)
#prediction = linear.predict(x_test) #use model to predict y value corresponding to xtest

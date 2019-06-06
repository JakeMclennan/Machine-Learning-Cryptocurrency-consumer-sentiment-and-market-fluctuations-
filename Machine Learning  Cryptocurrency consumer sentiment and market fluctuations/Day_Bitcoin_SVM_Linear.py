import csv
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
import numpy as np
from sklearn import datasets, svm
from sklearn.metrics import mean_squared_error, r2_score, average_precision_score, precision_recall_curve, precision_score
import pandas as pd


Date_List = []
T1_List = []
T2_List = []
T3_List = []
T4_List = []
T5_List = []
PC_24_List = []
PC_48_List = []
PC_72_List = []
PC_24_UD_List = []

def up_down(number):
    if number > 0:
        return 1
    if number < 0:
        return -1
    if number == 0:
        return 0


def day_grab(data):
    with open(data, encoding = "UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rDate = row['Date']
            T1 = int(row['T1'])
            T2 = int(row['T2'])
            T3 = int(row['T3'])
            T4 = int(row['T4'])
            T5 = int(row['T5'])
            PC24 = float(row['Percent Change 24'])
            PC48 = float(row['Percent Change 48'])
            PC72 = float(row['Percent Change 72'])
            Date_List.append(rDate)
            T1_List.append(T1)
            T2_List.append(T2)
            T3_List.append(T3)
            T4_List.append(T4)
            T5_List.append(T5)
            PC_24_List.append(PC24)
            PC_48_List.append(PC48)
            PC_72_List.append(PC72)
            PC_24_UD_List.append(up_down(PC24))
day_grab("Bitcoin_Days_2016_and_2017.csv")




df = pd.DataFrame({
                    'Date' : Date_List,
                    'Government' : T1_List,
                    'Security' : T2_List,
                    'Acceptance' : T3_List,
                    'Opinion' : T4_List,
                    'Block Change' : T5_List,
                    'Pos_Or_Neg' : PC_24_UD_List,})

df = df.drop('Date', axis=1)
df = df[['Pos_Or_Neg','Government','Security','Acceptance','Opinion','Block Change']]
print(df)




y = np.array(df[['Pos_Or_Neg']])
x = np.array(df.drop(['Pos_Or_Neg'], axis=1))

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.33, stratify=y)

                                                                #Linear SVM

#Fit The plot
from sklearn.svm import LinearSVC

model = LinearSVC()
model.fit(x_train, y_train.ravel())


#Calculate Test Prediction
y_pred = model.predict(x_test)
print("Test Predition : " + str(model.score(x_test,y_test.ravel())))
print("MSE : " + str(mean_squared_error(y_test, y_pred)))
print("R squared : " + str(r2_score(y_test, y_pred)))


#Plot Confusion Matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

p = precision_score(y_test, y_pred, average='macro')
#p = precision_score(y_test, y_pred, average='micro')
#p = precision_score(y_test, y_pred, average='weighted')
#p = precision_score(y_test, y_pred, average=None)
print("precision :" + str(p))
print("Classification Prediction :")
#print(x_test)
my_predict = model.predict([[ -1, -1,  1,  1,  0]])
print(my_predict)











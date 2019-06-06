import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, metrics
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from sklearn.model_selection import cross_val_predict


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
PC_48_UD_List = []
PC_72_UD_List = []

def up_down(number):
    if number > 0:
        return 1
    if number < 0:
        return -1
    if number == 0:
        return 0
def name_get(num):
    if num == 1:
        return "Government Regulation"
    if num == 2:
        return "Security/Hacks"
    if num == 3:
        return "Acceptance"
    if num == 4:
        return "Opinion"
    if num == 5:
        return "Changes to the block chain"



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
            PC_48_UD_List.append(up_down(PC48))
            PC_72_UD_List.append(up_down(PC72))
day_grab("Bitcoin_Days_2016_and_2017.csv")



def UP_DOWN_24(t1,t2,t3,t4,t5):
    df = pd.DataFrame({
                        'Date' : Date_List,
                        'Government' : T1_List,
                        'Security' : T2_List,
                        'Acceptance' : T3_List,
                        'Opinion' : T4_List,
                        'Block Change' : T5_List,
                        'Pos_Or_Neg' : PC_24_UD_List,
                        'Percent Change 24' : PC_24_List})
    df = df.drop('Date', axis=1)
    df = df[['Pos_Or_Neg','Government','Security','Acceptance','Opinion','Block Change']]

    X = df.drop('Pos_Or_Neg', axis=1)
    y = df[['Pos_Or_Neg']]
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
    from sklearn.linear_model import LinearRegression
    regression_model_24 = LinearRegression()
    regression_model_24.fit(X_train, y_train)
    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    intercept = regression_model_24.intercept_[0]
    print("R squared Score:")
    score = regression_model_24.score(X_test, y_test)
    print(score)
    y_predict = regression_model_24.predict(X_test)
    regression_model_mse = mean_squared_error(y_predict, y_test)
    print("MSE :")
    print(regression_model_mse)
    Prediction = regression_model_24.predict([[t1,t2,t3,t4,t5]])
    j = Prediction[0][0]
    print( "Explained Variance")
    ev = metrics.explained_variance_score(y_test, y_predict, sample_weight=None, multioutput='uniform_average')
    print(ev)

    return (round(j,4))

    
def UP_DOWN_48(t1,t2,t3,t4,t5):
    df = pd.DataFrame({
                        'Date' : Date_List,
                        'Government' : T1_List,
                        'Security' : T2_List,
                        'Acceptance' : T3_List,
                        'Opinion' : T4_List,
                        'Block Change' : T5_List,
                        'Pos_Or_Neg' : PC_48_UD_List,
                        'Percent Change 48' : PC_48_List})
    df = df.drop('Date', axis=1)
    df = df[['Pos_Or_Neg','Government','Security','Acceptance','Opinion','Block Change']]



    X = df.drop('Pos_Or_Neg', axis=1)
    y = df[['Pos_Or_Neg']]
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
    from sklearn.linear_model import LinearRegression
    regression_model_48 = LinearRegression()
    regression_model_48.fit(X_train, y_train)
    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    intercept = regression_model_48.intercept_[0]
    #print("R squared Score:")
    score = regression_model_48.score(X_test, y_test)
    #print(score)
    y_predict = regression_model_48.predict(X_test)
    regression_model_mse = mean_squared_error(y_predict, y_test)
    #print("MSE")
    #print(regression_model_mse)
    Prediction = regression_model_48.predict([[t1,t2,t3,t4,t5]])
    j = Prediction[0][0]
    return (round(j,4))
    #print( "Explained Variance")
    ev = metrics.explained_variance_score(y_test, y_predict, sample_weight=None, multioutput='uniform_average')
    #print(ev)




def UP_DOWN_72(t1,t2,t3,t4,t5):
    df = pd.DataFrame({
                        'Date' : Date_List,
                        'Government' : T1_List,
                        'Security' : T2_List,
                        'Acceptance' : T3_List,
                        'Opinion' : T4_List,
                        'Block Change' : T5_List,
                        'Pos_Or_Neg' : PC_72_UD_List,
                        'Percent Change 48' : PC_72_List})
    df = df.drop('Date', axis=1)
    df = df[['Pos_Or_Neg','Government','Security','Acceptance','Opinion','Block Change']]
    print(df)

    X = df.drop('Pos_Or_Neg', axis=1)
    y = df[['Pos_Or_Neg']]
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
    from sklearn.linear_model import LinearRegression
    regression_model_72 = LinearRegression()
    regression_model_72.fit(X_train, y_train)
    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    intercept = regression_model_72.intercept_[0]
    print("R squared Score:")
    score = regression_model_72.score(X_test, y_test)
    print(score)
    y_predict = regression_model_72.predict(X_test)
    regression_model_mse = mean_squared_error(y_predict, y_test)
    print("MSE")
    print(regression_model_mse)
    Prediction = regression_model_72.predict([[1,0,0,0,0]]) 
    j = Prediction[0][0]
    print("Prediction " + str((round(j,4))))
    print( "Explained Variance")
    ev = metrics.explained_variance_score(y_test, y_predict, sample_weight=None, multioutput='uniform_average')
    print(ev)
    return (round(j,4))




#UP_DOWN_24(1,1,1,1,0)



            
            

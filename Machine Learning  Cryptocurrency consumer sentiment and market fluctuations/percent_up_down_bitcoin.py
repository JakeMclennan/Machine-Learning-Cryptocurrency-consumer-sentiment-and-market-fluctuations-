import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd


Date_List = []
Value_List = []
Type_List = []
Title_List = []
Percent_Change_List = []

def machine_learn_date_grab(data):
    
    #with open(data) as csvfile:
    with open(data, encoding = "UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rTitle = row['Title']
            if rTitle != 'VOID': # this gets rid of the void ones. we may need to tweak
                rDate = row['Date']
                rValue = int(row['Value'])
                rType = int(row['Type'])
                rPercent_Change = float(row['Percent Change'])
                if rType != "0":
                    if rType != "99":
                        Title_List.append(rTitle)
                        Date_List.append(rDate)
                        Value_List.append(rValue)
                        Type_List.append(rType)
                        Percent_Change_List.append(rPercent_Change)


machine_learn_date_grab("2017_and_2016_compiled_Final_no_Void.csv")



Date_List = []
Value_List = []
Type_List = []
Title_List = []
Percent_Change_List_48 = []
Percent_Change_List_72 = []



def machine_learn_date_grab_48_72(data):
    
    #with open(data) as csvfile:
    with open(data, encoding = "UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rTitle = row['Title']
            if rTitle != 'VOID': # this gets rid of the void ones. we may need to tweak
                rDate = row['Date']
                rValue = int(row['Value'])
                rType = int(row['Type'])
                rPercent_Change_48 = float(row['Percent Change 48'])
                rPercent_Change_72 = float(row['Percent Change 72'])
                if rType != "0":
                    if rType != "99":
                        Title_List.append(rTitle)
                        Date_List.append(rDate)
                        Value_List.append(rValue)
                        Type_List.append(rType)
                        Percent_Change_List_48.append(rPercent_Change_48)
                        Percent_Change_List_72.append(rPercent_Change_72)

machine_learn_date_grab_48_72("2017_and_2016_compiled_Final_w_48_72.csv")










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

def total_correct():
    print("--------Total Correct-----------")
    c = 0
    correct_count = 0
    incorrect_count = 0
    for p in Date_List:
        if Value_List[c] != 99:
            if float(Percent_Change_List[c]) > 0 and Value_List[c] == 1:
                correct_count = correct_count + 1
            elif float(Percent_Change_List[c]) < 0 and Value_List[c] == -1:
                correct_count = correct_count + 1
            else:
                incorrect_count = incorrect_count + 1
                print(Date_List[c], Value_List[c], Type_List[c], Percent_Change_List[c])



        c = c + 1
    print(" ")
    print(correct_count)
    print(incorrect_count)
    print(correct_count/c)
    print(c,"\n")



def type_correct(shock_type):
    name = name_get(shock_type)
    c = 0
    correct_count = 0
    incorrect_count = 0
    num_of_shocks = 0
    for p in Date_List:
        if Type_List[c] == shock_type:
            num_of_shocks = num_of_shocks + 1
            if Value_List[c] != 99:
                if float(Percent_Change_List[c]) > 0 and Value_List[c] == 1:
                    correct_count = correct_count + 1
                elif float(Percent_Change_List[c]) < 0 and Value_List[c] == -1:
                    correct_count = correct_count + 1
                else:
                    incorrect_count = incorrect_count + 1
                    if len(Date_List[c]) == 8:
                        adjusted_date = (Date_List[c]+"  ")
                    elif len(Date_List[c]) == 9:
                        adjusted_date = (Date_List[c]+" ")
                    elif len(Date_List[c]) == 10:
                        adjusted_date = (Date_List[c])
                    if Value_List[c] == 1:
                        value = str(" 1")
                    if Value_List[c] == -1:
                        value = str(-1)
                    if float(Percent_Change_List[c]) > 0:
                        pc = str(" " + str(Percent_Change_List[c]))
                    if float(Percent_Change_List[c]) < 0:
                        pc = str(Percent_Change_List[c])
                    Shock_info = ("Date: "+adjusted_date + " " + "Values: " + value+ " " + "Type: " +  str(Type_List[c])+ " " + pc)
                    #print("    ",Shock_info, Title_List[c])
                    
        c = c + 1

    return (round(correct_count/num_of_shocks,2))

def percent_change_total(shock_type):
    print("\n")
    name = name_get(shock_type)
    print("Type", shock_type, "Percent Change Totals:",name)
    c = 0
    pos_correct_count = 0
    neg_correct_count = 0
    incorrect_count = 0
    num_of_shocks = 0
    pos_pc = 0
    neg_pc = 0
    for p in Date_List:
        if Type_List[c] == shock_type:
            num_of_shocks = num_of_shocks + 1
            if Value_List[c] != 99:
                if float(Percent_Change_List[c]) > 0 and Value_List[c] == 1:
                    pos_correct_count = pos_correct_count + 1
                    pos_pc = pos_pc + float(Percent_Change_List[c])
                elif float(Percent_Change_List[c]) < 0 and Value_List[c] == -1:
                    neg_correct_count = neg_correct_count + 1
                    neg_pc = neg_pc + float(Percent_Change_List[c])

        c = c + 1

    if pos_correct_count != 0:
        print("     Amount per Positive: ", round(pos_pc/pos_correct_count,2))
    elif pos_correct_count == 0:
        print("     There were 0 positive!")
    if neg_correct_count != 0:
        print("     Amount per Negative: ", round(neg_pc/neg_correct_count,2))
    elif neg_correct_count == 0:
        print("     There were 0 negative!")

def type_correct_48(shock_type):
    name = name_get(shock_type)
    c = 0
    correct_count = 0
    incorrect_count = 0
    num_of_shocks = 0
    for p in Date_List:
        if Type_List[c] == shock_type:
            num_of_shocks = num_of_shocks + 1
            if Value_List[c] != 99:
                if float(Percent_Change_List_48[c]) > 0 and Value_List[c] == 1:
                    correct_count = correct_count + 1
                elif float(Percent_Change_List_48[c]) < 0 and Value_List[c] == -1:
                    correct_count = correct_count + 1
                else:
                    incorrect_count = incorrect_count + 1
                    if len(Date_List[c]) == 8:
                        adjusted_date = (Date_List[c]+"  ")
                    elif len(Date_List[c]) == 9:
                        adjusted_date = (Date_List[c]+" ")
                    elif len(Date_List[c]) == 10:
                        adjusted_date = (Date_List[c])
                    if Value_List[c] == 1:
                        value = str(" 1")
                    if Value_List[c] == -1:
                        value = str(-1)
                    if float(Percent_Change_List_48[c]) > 0:
                        pc = str(" " + str(Percent_Change_List_48[c]))
                    if float(Percent_Change_List_48[c]) < 0:
                        pc = str(Percent_Change_List_48[c])
                    Shock_info = ("Date: "+adjusted_date + " " + "Values: " + value+ " " + "Type: " +  str(Type_List[c])+ " " + pc)
                    #print("    ",Shock_info, Title_List[c])
                    
        c = c + 1

    return (round(correct_count/num_of_shocks,2))



def type_correct_72(shock_type):
    name = name_get(shock_type)
    c = 0
    correct_count = 0
    incorrect_count = 0
    num_of_shocks = 0
    for p in Date_List:
        if Type_List[c] == shock_type:
            num_of_shocks = num_of_shocks + 1
            if Value_List[c] != 99:
                if float(Percent_Change_List_72[c]) > 0 and Value_List[c] == 1:
                    correct_count = correct_count + 1
                elif float(Percent_Change_List_72[c]) < 0 and Value_List[c] == -1:
                    correct_count = correct_count + 1
                else:
                    incorrect_count = incorrect_count + 1
                    if len(Date_List[c]) == 8:
                        adjusted_date = (Date_List[c]+"  ")
                    elif len(Date_List[c]) == 9:
                        adjusted_date = (Date_List[c]+" ")
                    elif len(Date_List[c]) == 10:
                        adjusted_date = (Date_List[c])
                    if Value_List[c] == 1:
                        value = str(" 1")
                    if Value_List[c] == -1:
                        value = str(-1)
                    if float(Percent_Change_List_72[c]) > 0:
                        pc = str(" " + str(Percent_Change_List_48[c]))
                    if float(Percent_Change_List_72[c]) < 0:
                        pc = str(Percent_Change_List_72[c])
                    Shock_info = ("Date: "+adjusted_date + " " + "Values: " + value+ " " + "Type: " +  str(Type_List[c])+ " " + pc)
                    #print("    ",Shock_info, Title_List[c])
                    
        c = c + 1
    return (round(correct_count/num_of_shocks,2))



Gov_Dum = []
Sec_Dum = []
Acc_Dum = []
Opi_Dum = []
Blo_Dum = []
positive_or_negative = []

for i in Date_List:
    Gov_Dum.append(0)
    Sec_Dum.append(0)
    Acc_Dum.append(0)
    Opi_Dum.append(0)
    Blo_Dum.append(0)

k = 0
for p in Date_List:
    if Value_List[k] == -1:
        if Type_List[k] == 1:
            Gov_Dum[k] = -1
        if Type_List[k] == 2:
            Sec_Dum[k] = -1
        if Type_List[k] == 3:
            Acc_Dum[k] = -1
        if Type_List[k] == 4:
            Opi_Dum[k] = -1
        if Type_List[k] == 5:
            Blo_Dum[k] = -1
    if Value_List[k] == 1:
        if Type_List[k] == 1:
            Gov_Dum[k] = 1
        if Type_List[k] == 2:
            Sec_Dum[k] = 1
        if Type_List[k] == 3:
            Acc_Dum[k] = 1
        if Type_List[k] == 4:
            Opi_Dum[k] = 1
        if Type_List[k] == 5:
            Blo_Dum[k] = 1
    k = k + 1

z = 0
for p in Date_List:
    if Percent_Change_List[z] > 0:
        positive_or_negative.append(1)
    if Percent_Change_List[z] < 0:
        #positive_or_negative.append(0)
        positive_or_negative.append(-1)
    if Percent_Change_List[z] == 0:
        positive_or_negative.append(0)
#print(len(positive_or_negative))
    z = z + 1
df = pd.DataFrame({
                'Date' : Date_List,
                'Value': Value_List,
                'Type' : Type_List,
                'Percent_Change' : Percent_Change_List,
                'Title' : Title_List,
                'Government' : Gov_Dum,
                'Security' : Sec_Dum,
                'Acceptance' : Acc_Dum,
                'Opinion' : Opi_Dum,
                'Block Change' : Blo_Dum,
                'Pos_Or_Neg' : positive_or_negative})
df = df[df.Type != 99]
df = df.drop('Title', axis=1)
df = df.drop('Date', axis=1)
df = df.drop('Type', axis=1)
df = df.drop('Value', axis=1)
#df = df[['Date','Value','Type','Percent_Change','Government','Security','Acceptance','Opinion','Block Change' ]]
#df = df[['Percent_Change','Government','Security','Acceptance','Opinion','Block Change' ]]
df = df[['Pos_Or_Neg','Government','Security','Acceptance','Opinion','Block Change' ]]

#print(df)

#X = df.drop('Percent_Change', axis=1)
#y = df[['Percent_Change']]

X = df.drop('Pos_Or_Neg', axis=1)
y = df[['Pos_Or_Neg']]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

from sklearn.linear_model import LinearRegression



regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

##for idx, col_name in enumerate(X_train.columns):
##    coef = round(regression_model.coef_[0][idx],4)
##    if col_name == 'Security':
##        print("Coefficient of {} is     : {}".format(col_name, coef))
##    elif col_name == 'Opinion':
##        print("Coefficient of {} is      : {}".format(col_name, coef))
##    elif col_name == 'Acceptance':
##        print("Coefficient of {} is   : {}".format(col_name, coef))
##    elif col_name == 'Government':
##        print("Coefficient of {} is   : {}".format(col_name, coef))
##    elif col_name == 'Block Change': 
##        print("Coefficient of {} is : {}".format(col_name, coef))

intercept = regression_model.intercept_[0]
#print("\n")
#print("The intercept for our model is {}".format(round(intercept,4)))

#score = regression_model.score(X_test, y_test)
#print(score)

def t1_coef():
    for idx, col_name in enumerate(X_train.columns):
        coef = round(regression_model.coef_[0][idx],4)
        if col_name == 'Government':
            return coef
def t2_coef():
    for idx, col_name in enumerate(X_train.columns):
        coef = round(regression_model.coef_[0][idx],4)
        if col_name == 'Security':
            return coef
def t3_coef():
    for idx, col_name in enumerate(X_train.columns):
        coef = round(regression_model.coef_[0][idx],4)
        if col_name == 'Acceptance':
            return coef
def t4_coef():
    for idx, col_name in enumerate(X_train.columns):
        coef = round(regression_model.coef_[0][idx],4)
        if col_name == 'Opinion':
            return coef
def t5_coef():
    for idx, col_name in enumerate(X_train.columns):
        coef = round(regression_model.coef_[0][idx],4)
        if col_name == 'Block Change':
            return coef
        


#print("R squared Score:")
score = regression_model.score(X_test, y_test)
#print(score)

y_predict = regression_model.predict(X_test)

regression_model_mse = mean_squared_error(y_predict, y_test)
#print("MSE:")
#print(regression_model_mse)
def predic(t1,t2,t3,t4,t5):
    #Prediction = regression_model.predict([[1,0,0,0,0]])
    Prediction = regression_model.predict([[t1,t2,t3,t4,t5]])
    #Prediction = regression_model.predict([[1,t1,t2,t3,t4,t5]])
    j = Prediction[0][0]
    
    return (round(j,4))
    #print(Prediction)




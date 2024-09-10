# -*- coding: utf-8 -*-
"""Student_performance_prediction_using_machine learning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ou5jUuMIH3ifg7nny6Lk5QNraidKwwX0
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

df_por = pd.read_csv("/content/student-por.csv",sep=';')

df_por.head()

df_por.info()

def age(age):
    new_age=[]
    for i in age:
        if(i < 17):
            i=0
        elif (i < 19):
            i=1
        else:
            i=2
        new_age.append(i)
    return new_age

df_por['age']=age(df_por['age'])

sns.boxplot(x='age',y='G3',data=df_por)

df_por['school']=pd.get_dummies(df_por['school'],drop_first=True)

sns.boxplot(x='school',y='G3',data=df_por)      # 0 = GP and 1 = MS

df_por['sex'].value_counts()

sns.boxplot(x='sex',y='G3',data=df_por)

df_por['sex'] = pd.get_dummies(df_por['sex'],drop_first=True)

df_por['address'].value_counts()

sns.boxplot(x='address', y='G3', data=df_por) # specify x and y using keywords

df_por['address'] = pd.get_dummies(df_por['address'],drop_first=True)

df_por['famsize'].value_counts() # changed df to df_por

import seaborn as sns
import pandas as pd # Import pandas

# Assuming df_por is a pandas DataFrame and 'famsize' and 'G3' are valid columns
sns.boxplot(x='famsize', y='G3', data=df_por)

df_por.drop('famsize',axis=1,inplace=True)

df_por['Pstatus'].value_counts()

sns.boxplot(x='Pstatus',y='G3',data=df_por)

df_por.drop('Pstatus',axis=1,inplace=True)

sns.boxplot(x='Medu',y='G3',data=df_por)

df_por['Fedu'].value_counts()

sns.boxplot(x='Fedu',y='G3',data=df_por)

sns.boxplot(x='Fedu',y='G3',data=df_por)

df_por['Mjob'].value_counts()

sns.boxplot(x='Mjob',y='G3',data=df_por)

sns.boxplot(x='Fjob',y='G3',data=df_por)

"""# Students whose parents are teachers ,score better in exams.

#I will convert these categories into dummy variables later#
"""

df_por['reason'].value_counts()

sns.boxplot(x='reason', y='G3', data=df_por) # specify x and y using keywords

df_por['guardian'].value_counts()

sns.boxplot(x='guardian',y='G3',data=df_por)

sns.boxplot(x='traveltime',y='G3',data=df_por)



"""# Travel time to school doesn't affect much

"""

df_por.drop('traveltime',axis=1,inplace=True)

df_por['studytime'].value_counts()

sns.boxplot(x='studytime',y='G3',data=df_por)

df_por['failures'].value_counts()

sns.boxplot(x='failures',y='G3',data=df_por)

sns.boxplot(x='schoolsup', y='G3', data=df_por) # Pass x and y as keyword arguments

df_por['schoolsup']=pd.get_dummies(df_por['schoolsup'],drop_first=True)

sns.boxplot(x='famsup', y='G3', data=df_por) # Pass x and y as keyword arguments

df_por.drop('famsup',axis=1,inplace=True)

df_por['activities'].value_counts()

sns.boxplot(x='activities', y='G3', data=df_por) # Pass x and y as keyword arguments

df_por.drop('activities',axis=1,inplace=True)

df_por['higher'].value_counts()

sns.boxplot(x='higher', y='G3', data=df_por) # Pass 'higher' and 'G3' as keyword arguments

df_por['higher']=pd.get_dummies(df_por['higher'],drop_first=True)

df_por['internet'].value_counts()

df_por['internet']=pd.get_dummies(df_por['internet'],drop_first=True)

sns.boxplot(x='internet',y='G3',data=df_por)

df_por['health'].value_counts()

sns.boxplot(x='health', y='G3', data=df_por)

sns.jointplot(x='absences',y='G3',data=df_por,kind="reg")

def absences(n):
    new=[]
    for i in n:
        if (i <= 10):
            i=0
        elif(i <= 20):
            i=1
        else:
            i=2
        new.append(i)
    return new

df_por['absences']=absences(df_por['absences'])

df_por['absences'].value_counts()

sns.boxplot(x='absences', y='G3', data=df_por) # Use x and y arguments to specify the columns for the boxplot.

df_por.info()

df_por = pd.get_dummies(df_por,drop_first=True)

df_por.info()

from sklearn.model_selection import train_test_split

def result(score):
    new=[]
    for i in score:
        if (i<8):
            i=0     #Student fails
        else:
            i=1     #student passes
        new.append(i)
    return new

df_por['G3']=result(df_por['G3'])

X_train, X_test, y_train, y_test = train_test_split(df_por.drop(['G1','G2','G3'],axis=1), df_por['G3'], test_size=0.33, random_state=42)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train,y_train)

model.score(X_test,y_test)












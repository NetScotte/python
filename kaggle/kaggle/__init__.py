import pandas
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold
import numpy as np
import matplotlib.pyplot as plt

titanic = pandas.read_csv('../Kaggle_Titanic-master/train.csv')

titanic.loc[titanic['Sex'] == 'male', 'Sex'] = 0
titanic.loc[titanic['Sex'] == 'female', 'Sex'] =1
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] =0
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] =1
titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] =2
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].median())
# print(titanic['Pclass'].unique())
# print(titanic['Sex'].unique())
# print(titanic['Age'].unique())
# print(titanic['SibSp'].unique())
# print(titanic['Fare'].unique())
# print(titanic['Embarked'].unique())




predictors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

'''
alg = LinearRegression()
kf = KFold(titanic.shape[0], n_folds=3, random_state=1)

predictions = []
for train, test in kf:
    train_predictors = (titanic[predictors].iloc[train, :])
    train_target = titanic['Survived'].iloc[train]
    alg.fit(train_predictors, train_target)
    test_predictions = alg.predict(titanic[predictors].iloc[test, :])
    predictions.append(test_predictions)

predictions = np.concatenate(predictions, axis=0)
predictions[predictions > .4] = 1
predictions[predictions <= .4] = 0
accuracy = sum(predictions[predictions == titanic['Survived']]) / len(predictions)
print(accuracy)
'''
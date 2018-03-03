from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
import pandas
import numpy as np

titanic = pandas.read_csv('../Kaggle_Titanic-master/train.csv')

titanic.loc[titanic['Sex'] == 'male', 'Sex'] = 0
titanic.loc[titanic['Sex'] == 'female', 'Sex'] =1
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] =0
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] =1
titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] =2
titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].median())
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())

predictors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

#逻辑回归
alg = LogisticRegression(random_state=1)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic['Survived'], cv=3)
print(scores.mean())


'''
#线性回归
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


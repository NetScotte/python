import pandas
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier

titanic = pandas.read_csv('../Kaggle_Titanic-master/train.csv')

titanic.loc[titanic['Sex'] == 'male', 'Sex'] = 0
titanic.loc[titanic['Sex'] == 'female', 'Sex'] =1
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] =0
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] =1
titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] =2
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].median())

predictors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
alg = RandomForestClassifier(n_estimators=10, min_samples_split=2, min_samples_leaf=1,random_state=None)
kf = cross_validation.KFold(titanic.shape[0], n_folds=3, random_state=1)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic['Survived'], cv=kf)
print(scores.mean())
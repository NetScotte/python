import pandas
import re
from sklearn.feature_selection import SelectKBest, f_classif
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation

titanic = pandas.read_csv('../Kaggle_Titanic-master/train.csv')
titanic.loc[titanic['Sex'] == 'male', 'Sex'] = 0  # 类似于循环语句，遍历此列并修改值
titanic.loc[titanic['Sex'] == 'female', 'Sex'] = 1
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] = 0
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] = 1
titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] = 2
titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].median())
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())

'''
# define other Attribute
titanic['Family'] = titanic['SibSp'] + titanic['Parch']
titanic['NameLength'] = titanic['Name'].apply(lambda x: len(x))

#anasis name about mr , miss , mrs
def get_title(name):
    title_search = re.search(', ([A-Za-z]+)', name)  # 注意此处的空格，否则会匹配到第一个词
    if title_search:
        return title_search.group(1)
    return ''

titles = titanic['Name'].apply(get_title)
#print(pandas.value_counts(titles))
titles_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master':0.1, 'Dr':0.2, 'Rev':0.3, 'Major':0.3, 'Mlle':0.4, 'Col':0.5, 'Ms':0.6,\
                  'Jonkheer':0.7, 'Don':0.8, 'Lady':0.9, 'Mme':0.11, 'Capt':0.21, 'Sir':0.31, 'the':0.41}
for k, v in titles_mapping.items():
    titles[titles == k] = v                     #将所有mr,miss,mrs项修改为1，2，3
# print(pandas.value_counts(titles))
titanic['Title'] = titles

predictors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked','Family', 'NameLength', 'Title']
selector = SelectKBest(f_classif, k=5)
selector.fit(titanic[predictors],titanic['Survived'])
scores = -np.log10(selector.pvalues_)

plt.bar(range(len(predictors)),scores)
plt.xticks(range(len(predictors)),predictors,rotation='vertical')
plt.show(block=False)
'''

# 使用新属性进行机器学习
predictors = ['Pclass', 'Sex', 'Fare', 'NameLength', 'Title']
alg = RandomForestClassifier(n_estimators=10, min_samples_split=2, min_samples_leaf=1, random_state=None)
kf = cross_validation.KFold(titanic.shape[0], n_folds=3, random_state=1)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic['Survived'], cv=kf)
print(scores.mean())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 00:01:26 2019

@author: seoksah
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("survey_results_public.csv")
sns.set(rc={"figure.figsize":(21.7,8.27)})
#print(data.head())
#print(data.columns.values)
data.dropna(subset = ["LanguageWorkedWith"],inplace=True)
data.dropna(subset = ["ConvertedSalary"],inplace=True)
data["LanguageWorkedWith"] = data["LanguageWorkedWith"].str.split(";", n=1, expand=True)
data.drop(data.loc[data['ConvertedSalary'] < 20000].index, inplace=True)
data = data.groupby("LanguageWorkedWith").filter(lambda x: len(x) > 50)


salaryLanguage = data[["LanguageWorkedWith","ConvertedSalary"]]
salaryLanguage = salaryLanguage.groupby(["LanguageWorkedWith"], as_index = False).median()

salaryLanguage.sort_values(["ConvertedSalary"], inplace = True, ascending = False)
print(salaryLanguage)
#ax = sns.barplot(x = "ConvertedSalary", y ="LanguageWorkedWith", data = salaryLanguage, ci = None).figure.tight_layout()

ax = sns.countplot(y="LanguageWorkedWith", data = data, order = data["LanguageWorkedWith"].value_counts().index).figure.tight_layout()
plt.xlabel("Count")
#plt.xlabel("Salary ($)")
plt.ylabel("Programming Language")
plt.show(ax)

#print(data["LanguageWorkedWith"])
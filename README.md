# Popular Programming Languages
This is an example showing a statistical analysis using a Stack Exchange survey from 2018 focusing on the popular programming languages and their relation to salaries earned by the users of those languages.

Using pandas, the data was cleaned up to include only respondents that completed both the languages worked with and converted salaries columns. It was further cleaned up to include only languages with more than 50 users and salaries that were reported to be above $20,000. The data was then sorted in decreasing order for both the number of users of each language and then the median salary of each language. Median was used to avoid the effect of the outliers on the mean. 

The data was then visualized using two different barplots. One is a countplot for the number of users of each language in order to show what languages are most popular. The other is a barplot comparing the median salary of each language user. 

The results are shown below:

![alt text](https://github.com/SeokSah/stackOverFlowData/blob/master/languageCountUpdate.png)
![alt text](https://github.com/SeokSah/stackOverFlowData/blob/master/salaryLanguage.png)

Data taken from https://www.kaggle.com/stackoverflow/stack-overflow-2018-developer-survey

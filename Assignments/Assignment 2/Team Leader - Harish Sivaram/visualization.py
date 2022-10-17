sns.distplot(ds['EstimatedSalary'],hist=True)
sns.relplot(x='Age',y='Balance',data=ds)
#categorical data
sns.catplot(x='Geography',y='CreditScore',data=ds)
sns.relplot(x='Age',y='Balance',hue='Geography',data=ds)
#categorical data
sns.boxplot(x='Exited',y='CreditScore',hue='Gender',data=ds)
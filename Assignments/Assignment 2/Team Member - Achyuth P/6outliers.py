ds.skew()
sns.boxplot(ds["Age"])
q0 = ds["Age"].describe()["25%"]
q1 = ds["Age"].describe()["75%"]
iqr=q1-q0
lb = q0 -(1.5*iqr)
ub = q1 + (1.5*iqr)
ds[ds["Age"]<lb]
ds[ds["Age"]>ub]
outlier_list = list(ds[ds["Age"] > ub]["Age"])
print(outlier_list)
outlier_dict = {}.fromkeys(outlier_list,ub)
print(outlier_dict)
ds["Age"] = ds["Age"].replace(outlier_dict)
sns.boxplot(ds["Age"])
ds[ds["Age"]>ub]
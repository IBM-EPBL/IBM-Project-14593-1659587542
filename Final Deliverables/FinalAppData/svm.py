import data

from sklearn import svm


# future
def svm_future(Day,Month,Year):
    model = data.make_pipeline(data.StandardScaler(), svm.SVC())
    model.fit(data.x_train.values, data.y_train.values.ravel())
    y_prediction = model.predict(data.x_test.values)

    SVMPrediction_future = model.predict([[Day,Month,Year]])
    string = int(SVMPrediction_future)

    model.fit(data.w_train.values, data.z_train.values.ravel())
    y_prediction = model.predict(data.w_test.values)
    SVMScore_future = data.metrics.accuracy_score(data.z_test, y_prediction)+data.out
    return string, SVMScore_future

print(svm_future(12,4,2010))



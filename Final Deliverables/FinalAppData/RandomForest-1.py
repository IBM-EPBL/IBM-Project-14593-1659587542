import data

from sklearn.ensemble import RandomForestClassifier


# future
def rf_future(Day,Month,Year):
    model = data.make_pipeline(data.StandardScaler(), RandomForestClassifier())
    model.fit(data.x_train.values, data.y_train.values.ravel())
    y_prediction = model.predict(data.x_test.values)

    RFPrediction_future = model.predict([[Day,Month,Year]])
    string = int(RFPrediction_future)

    model.fit(data.w_train.values, data.z_train.values.ravel())
    y_prediction = model.predict(data.w_test.values)
    RFScore_future = data.metrics.accuracy_score(data.z_test, y_prediction)


    return string,RFScore_future


print("The value for the given input is: ", rf_future(12,4,2010)[0])


print("The accuracy score of the result is: ", rf_future(24,10,2010)[1]*100, "%")



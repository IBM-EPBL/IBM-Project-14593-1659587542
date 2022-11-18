import data
import svm
import RandomForest
from flask import Flask, redirect, url_for
from flask import *
app = Flask(__name__)


# future
def future_result(day,month,year):
    algo={0:"Random forest", 1:"Support vector machine"}
    rf_data=RandomForest.rf_future(day,month,year)
    svm_data = svm.svm_future(day,month,year)

    

    diction_prediction_future=[rf_data[0],svm_data[0]]
    score_array=[rf_data[1],svm_data[1]]
    maximum_score=max(score_array)
    index_result=score_array.index(max(score_array))
    algorithms=algo[index_result]
    string_result=diction_prediction_future[index_result]

    return [rf_data[0],svm_data[0],rf_data[1],svm_data[1],maximum_score,string_result,algorithms,day,month,year]

print("The answer is",future_result(12,4,2010))
   


request_data=[]
future_res=[]


@app.route('/futureToFlask', methods=['GET','POST'])
def abc():
    global request_data
    global future_res
    if request.method=='POST':
        request_data=json.loads(request.data)  
        future_res=future_result(request_data[0],request_data[1],request_data[2])        
    return future_res

@app.route('/futureToReact')
def submit_future():
   return redirect(url_for('abc'))
   

if __name__ == '__main__':
    app.run(debug=True)

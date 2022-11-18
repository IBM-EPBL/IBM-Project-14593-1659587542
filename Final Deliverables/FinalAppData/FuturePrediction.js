import React, {useState,useEffect} from 'react';
import './FuturePrediction.css';
import Axios from 'axios';

function FuturePrediction() {

  const [prediction, setPrediction] = useState([]);
 

  useEffect(() => {
    fetch("/futureToReact").then((res) =>
        res.json().then((val) => {  
          setPrediction(val)   
          Axios.post("http://localhost:3001/detail",{day:val[7],month:val[8],year:val[9],prediction:val[5],algorithm:val[6],accuracyScore:val[4]*100})            
        })
    ); 
    
  }, []);


  
  return (
    <div class="bg-img-black App">
      <h1 class="blue-text">PREDICTION</h1>
      <h2>The predicted value of crude oil for the given date is <b>{prediction[5]}</b></h2>
      <h3>This prediction was made by the best suited <b>{prediction[6]}</b> algorithm for this instance with the highest accuracy score of <b>{prediction[4]*100} %</b></h3>
      <br></br>
      <hr></hr>
      <br></br>
      <h1 class="wrong">ANALYSIS REPORT</h1>
      <table class="table-center">
        <tr>
          <th class="pred-th"><h2>Algorithm used</h2></th>
          <th class="pred-th"><h2>Prediction</h2></th>
          <th class="pred-th"><h2>Accuracy score (%)</h2></th>
        </tr>

        <tr>
          <td class="pred-td"><h3>Random forest</h3></td>
          <td class="pred-td"><h3>The predicted value is {prediction[0]}</h3></td>
          <td class="pred-td"><h3>{prediction[2]*100}</h3></td>
        </tr>

        <tr>
          <td class="pred-td"><h3>Support vector machine</h3></td>
          <td class="pred-td"><h3>The predicted value is {prediction[1]}</h3></td>
          <td class="pred-td"><h3>{prediction[3]*100}</h3></td>
        </tr>
      </table>
    </div>
  );
  setPrediction([])
}

export default FuturePrediction


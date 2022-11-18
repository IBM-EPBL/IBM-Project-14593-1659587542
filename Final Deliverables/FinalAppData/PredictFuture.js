import React,{useEffect, useState} from 'react'
import { AiFillEyeInvisible,AiFillEye } from "react-icons/ai";
import { Link,useNavigate } from 'react-router-dom';
import Axios from 'axios';
import './PredictFuture.css';


function PredictFuture() {
  let navigate=useNavigate();
  const [day,setDay]=useState(0)
  const [month,setMonth]=useState(0)
  const [year,setYear]=useState(0)

  const blockInvalidChar = e => {
    if (['e', 'E', '+', '-'].includes(e.key) || e.target.value.length>=5) {
      e.preventDefault();
    }
  }
  const [clicked,setClicked]=useState(false)
  

  const onSubmitFuture = event => {
    setClicked(true)
    event.currentTarget.disabled = true;
    fetch('/futureToFlask',{
      method: 'POST',
      body: JSON.stringify([day,month,year])
    }).then(response => response.json()
      .then(data => ({ data, response })))
      .then(({ data, response }) =>  {
        console.log(data)
    })

    setTimeout(()=> {
      navigate('/futurePrediction');
      setClicked(false)
     }, 4000);
  };

  return (
    <div>
      <div class="bg-img-login bg-img-future">
        <div class="future-container register-container">
          <form>
            <div class="crude-title title-position-login">Crude 7 Predictor</div>
            <div class="future-title crude-title title-position-login">Crude value predictor</div>  
            <br></br>
            <label>Enter day</label>
            <br></br>
            <input class="gray-background" type="number" min="0" step="1" onKeyDown={blockInvalidChar} placeholder='Joining year' onChange={(e)=>{
              setDay(e.target.value)
            }} required />
            <br></br>
            <label>Enter month</label>
            <br></br>
            <input class="gray-background" type="number" min="0" max="2022" step="1" onKeyDown={blockInvalidChar} placeholder='Joining year' onChange={(e)=>{
              setMonth(e.target.value)
            }} required />
            <br></br>
            <label>Enter year</label>
            <br></br>
            <input class="gray-background" type="number" min="0" max="2022" step="1" onKeyDown={blockInvalidChar} placeholder='Joining year' onChange={(e)=>{
              setYear(e.target.value)
            }} required />
            <br></br>
            
            <br></br><br></br><br></br>
          </form>
          {!clicked ?  <button onClick={onSubmitFuture} type ="submit" disabled={!day || !month || !year} class="login-btn submit-btn">Predict</button> : <h3 class="blue-text">Loading.....</h3>}
        </div>
      </div>
    </div>
  )
}

export default PredictFuture
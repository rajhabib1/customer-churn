fetch('https://customer-churn-51ou.onrender.com', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        SeniorCitizen: document.getElementById('SeniorCitizen').value,
        tenure: document.getElementById('tenure').value,
        MonthlyCharges: document.getElementById('MonthlyCharges').value,
        TotalCharges: document.getElementById('TotalCharges').value,
        gender: document.getElementById('gender').value,
        Partner_Yes: document.getElementById('Partner_Yes').value,
        Dependents_Yes: document.getElementById('Dependents_Yes').value,
        Contract: document.getElementById('Contract').value,
        PaymentMethod: document.getElementById('PaymentMethod').value,
        PhoneService: document.getElementById('PhoneService').value,
        MultipleLines: document.getElementById('MultipleLines').value,
        InternetService: document.getElementById('InternetService').value,
        OnlineSecurity: document.getElementById('OnlineSecurity').value,
        OnlineBackup: document.getElementById('OnlineBackup').value,
        DeviceProtection: document.getElementById('DeviceProtection').value,
        TechSupport: document.getElementById('TechSupport').value,
        StreamingTV: document.getElementById('StreamingTV').value,
        StreamingMovies: document.getElementById('StreamingMovies').value,
        PaperlessBilling: document.getElementById('PaperlessBilling').value
    })
})
.then(response => response.json())
.then(data => {
    document.getElementById('prediction-result').innerText = data.prediction;
})
.catch(error => {
    console.error('Error:', error);
    document.getElementById('prediction-result').innerText = 'An error occurred. Please try again.';
});

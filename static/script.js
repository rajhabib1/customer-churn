document.getElementById('churn-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = {
        SeniorCitizen: document.getElementById('SeniorCitizen').value,
        tenure: document.getElementById('tenure').value,
        MonthlyCharges: document.getElementById('MonthlyCharges').value,
        TotalCharges: document.getElementById('TotalCharges').value,
        // Add the rest of your form fields here
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        alert(`Prediction: ${data.prediction}`);
    })
    .catch((error) => {
        alert('An error occurred. Please try again.');
        console.error('Error:', error);
    });
});
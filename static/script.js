document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Gather form data
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    // Send POST request to the /predict endpoint
    fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})

    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(result => {
        // Display the result
        document.getElementById('prediction-result').innerText = `Prediction: ${result.prediction}`;
    })
    .catch(error => {
        document.getElementById('prediction-result').innerText = 'An error occurred. Please try again.';
        console.error('Error:', error);
    });
});
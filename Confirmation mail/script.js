function sendEmail() {
    // Retrieve form values
    const toEmail = document.getElementById("toEmail").value;
    const subject = document.getElementById("subject").value;
    const message = document.getElementById("message").value;

    // Send the form data to the Flask server using fetch
    fetch('/send-email', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ toEmail, subject, message }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Email sent successfully!");
        } else {
            alert("Error sending email. Please try again.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert(`An unexpected error occurred: ${error.message}`);
    });
    
}

const form = document.getElementById('submit-to-google-sheet');
const span = document.getElementById('span');

form.addEventListener('submit', async (event) => {
  // Prevent default form submission to avoid a page reload
  event.preventDefault();

  // Create the form data object
  const formData = new FormData(form);

  // Perform form validation (optional)
  // If validation fails, handle errors and prevent submission

  try {
    // Simulate a backend fetch (replace with your actual fetch logic)
    const response = await fetch('/your-backend-endpoint', {
      method: 'POST',
      body: formData
    });

    // Check for successful response (replace with your own logic)
    if (response.ok) {
      // Show success message
      span.textContent = 'Data successfully submitted!';
      // Additional UI updates (optional)

      // Reset the form (optional)
      form.reset();
    } else {
      // Handle error response
      span.textContent = 'An error occurred. Please try again.';
    }
  } catch (error) {
    // Handle network or other errors
    span.textContent = 'An unexpected error occurred. Please try again later.';
  }
});



// Form validation 

  
  const phoneInput = document.getElementById('phone');
  const emailInput = document.getElementById('email');

  form.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    // Phone number validation
    if (!phoneInput.value.match(/^\d{3}-\d{3}-\d{4}$/)) {
      alert("Invalid phone number format. Please use ###-###-#### format.");
      return false; // Prevent form submission
    }

    // Email validation
    if (!emailInput.value.match(/\S+@\S+\.\S+/)) {
      alert("Invalid email address format. Please enter a valid email address.");
      return false; // Prevent form submission
    }

    // Form is valid, submit it
    form.submit();
  });


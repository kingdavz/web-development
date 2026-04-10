
// Get elements
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const messageInput = document.getElementById("message");

// Message elements
const nameMsg = document.getElementById("nameMsg");
const emailMsg = document.getElementById("emailMsg");
const passwordMsg = document.getElementById("passwordMsg");
const messageMsg = document.getElementById("messageMsg");

// Validation functions
function validateName() {
    if (nameInput.value.trim().length < 3) {
        showError(nameMsg, "Name must be at least 3 characters");
        return false;
    } else {
        showSuccess(nameMsg, "Looks good!");
        return true;
    }
}

function validateEmail() {
    const pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!pattern.test(emailInput.value)) {
        showError(emailMsg, "Enter a valid email");
        return false;
    } else {
        showSuccess(emailMsg, "Valid email");
        return true;
    }
}

function validatePassword() {
    if (passwordInput.value.length < 6) {
        showError(passwordMsg, "At least 6 characters required");
        return false;
    } else {
        showSuccess(passwordMsg, "Strong password");
        return true;
    }
}

function validateMessage() {
    if (messageInput.value.trim() === "") {
        showError(messageMsg, "Message cannot be empty");
        return false;
    } else {
        showSuccess(messageMsg, "Message looks good");
        return true;
    }
}

// Helper functions
function showError(element, msg) {
    element.textContent = msg;
    element.className = "message error";
}

function showSuccess(element, msg) {
    element.textContent = msg;
    element.className = "message success";
}

// Live validation (on input)
nameInput.addEventListener("input", validateName);
emailInput.addEventListener("input", validateEmail);
passwordInput.addEventListener("input", validatePassword);
messageInput.addEventListener("input", validateMessage);

// Prevent submit if invalid
document.getElementById("contactForm").addEventListener("submit", function(e) {
    if (!validateName() || !validateEmail() || !validatePassword() || !validateMessage()) {
        e.preventDefault();
    }
});

const form = document.getElementById("contactForm");
const successBox = document.getElementById("successMessage");

form.addEventListener("submit", function(e) {
    e.preventDefault();

    const isNameValid = validateName();
    const isEmailValid = validateEmail();
    const isPasswordValid = validatePassword();
    const isMessageValid = validateMessage();

    if (isNameValid && isEmailValid && isPasswordValid && isMessageValid) {
        // Get user's name
        const userName = nameInput.value.trim();

        // Hide form
        form.style.display = "none";

        // Show success message
        successBox.style.display = "block";
        successBox.textContent = `Thank you, ${userName}! Your message has been sent.`;
    }
});
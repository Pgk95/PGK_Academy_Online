document.addEventListener("DOMContentLoaded", function() {
    const passwordInput = document.getElementById("password");

    passwordInput.addEventListener("input", function() {
        passwordInput.setAttribute("placeholder", "Enter your Password here");
    });

    passwordInput.addEventListener("invalid", function() {
        passwordInput.setCustomValidity("");
        passwordInput.setAttribute("placeholder", "Incorrect Password");
    });
});

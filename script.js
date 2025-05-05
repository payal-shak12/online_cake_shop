document.addEventListener("DOMContentLoaded", function () {
    const orderButtons = document.querySelectorAll(".order-btn");

    orderButtons.forEach(button => {
        button.addEventListener("click", function () {
            let cakeName = this.getAttribute("data-name");
            let cakePrice = this.getAttribute("data-price");

            let quantity = prompt(`How many ${cakeName}s would you like?`, "1");

            if (quantity && !isNaN(quantity) && quantity > 0) {
                let totalPrice = quantity * cakePrice;
                alert(`🎉 Your order for ${quantity} ${cakeName}(s) has been placed!\nTotal Price: ₹${totalPrice}`);
            } else {
                alert("Please enter a valid quantity.");
            }
        });
    });
});



// Signup Form Validation
document.addEventListener("DOMContentLoaded", function () {
    let signupForm = document.querySelector("form");
    if (signupForm) {
        signupForm.addEventListener("submit", function (event) {
            let username = document.querySelector("input[name='username']").value;
            let email = document.querySelector("input[name='email']").value;
            let password = document.querySelector("input[name='password']").value;

            if (username === "" || email === "" || password === "") {
                alert("⚠️ Please fill out all fields!");
                event.preventDefault();
            } else {
                alert("✅ Signup successful!");
            }
        });
    }
});

// Login Form Validation
document.addEventListener("DOMContentLoaded", function () {
    let loginForm = document.querySelector("form");
    if (loginForm) {
        loginForm.addEventListener("submit", function (event) {
            let email = document.querySelector("input[name='email']").value;
            let password = document.querySelector("input[name='password']").value;

            if (email === "" || password === "") {
                alert("⚠️ Please enter your email and password!");
                event.preventDefault();
            } else {
                alert("✅ Login successful!");
            }
        });
    }
});

// Mobile Menu Toggle
document.addEventListener("DOMContentLoaded", function () {
    let menu = document.querySelector(".nav-menu");
    let menuToggle = document.createElement("button");
    menuToggle.textContent = "☰";
    menuToggle.classList.add("menu-toggle");

    document.querySelector(".navbar").prepend(menuToggle);

    menuToggle.addEventListener("click", function () {
        menu.classList.toggle("active");
    });
});

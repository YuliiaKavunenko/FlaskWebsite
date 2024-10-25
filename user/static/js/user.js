document.addEventListener("DOMContentLoaded", function () {
    var goodRegModal = document.getElementById("success-registration-window")
    var registrationButton = document.getElementById("confirm-registration")
    var nextAuthButton = document.getElementById("next-authorization")

    var authorizationForm =  document.getElementById("authorization-form")
    var registrationForm = document.getElementById("registration-form")

    var authorizationButton = document.getElementById("confirm-authorization")
    var AuthModal = document.getElementById("modal-authorization-window")
    // var successAuthModal = document.getElementById("success-authorization-window")

    // var goodAuthModal


    registrationButton.addEventListener("click", function (event) {
        event.preventDefault();
        goodRegModal.style.display = "block"
    });

    nextAuthButton.addEventListener("click", function(event){
        goodRegModal.style.display = "none"
        registrationForm.style.display = "none"
        authorizationForm.style.display = "block"
    })
    authorizationButton.addEventListener("click", function(event){
        AuthModal.style.display = "block"
        event.preventDefault()
    })


});

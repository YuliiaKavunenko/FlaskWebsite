document.addEventListener("DOMContentLoaded", function () {
    var registrationButton = document.getElementById("confirm-registration");
    var successRegModal = document.getElementById("success-registration-window");
    var proceedButton = document.getElementById("next-authorization");
    var registrationForm = document.getElementById("registration-form");

    registrationButton.addEventListener("click", function (event) {
        event.preventDefault();
        successRegModal.style.display = "block";
    });

    proceedButton.addEventListener("click", function () {
        successRegModal.style.display = "none";
        registrationForm.submit();
    });
});

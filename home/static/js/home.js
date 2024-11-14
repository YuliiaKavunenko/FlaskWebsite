document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".message-exit-button").forEach(button => {
        button.addEventListener("click", function(event) {
            event.preventDefault();
            document.getElementById("message-window").style.display = "none";
        });
    });
});
// This function runs when the page is fully loaded
document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function (event) {

            const name = document.querySelector("input[name='name']").value;
            const rating = document.querySelector("select[name='rating']").value;

            // Simple validation
            if (name.trim() === "" || rating === "") {
                alert("Please fill all required fields!");
                event.preventDefault(); // stop form submission
            } else {
                alert("Thank you! Your feedback has been submitted.");
            }
        });
    }

});

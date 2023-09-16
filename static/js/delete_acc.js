document.addEventListener("DOMContentLoaded", function() {
    const deleteButton = document.getElementById("delete-account-button");

    deleteButton.addEventListener("click", function() {
        // display a confirmation dialog
        const confirmation = confirm("Are you sure you want to delete your account? this action cannot be undone.")

        // if user confirms, proceed with account deletion
        if (confirmation) {
            
        }
    })
})
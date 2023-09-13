const enrollDateElement = document.getElementById('enroll-date');

function updateEnrollDate() {
    const currentDate = new Date();
    const formattedDate = currentDate.toDateString();
    enrollDateElement.textContent = 'Enroll Date: ${formattedDate}';
}

updateEnrollDate();

setInterval(updateEnrollDate, 1000);
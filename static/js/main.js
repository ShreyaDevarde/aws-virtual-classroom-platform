console.log(
    "Virtual Classroom Loaded Successfully"
);

// Auto close alerts

setTimeout(() => {

    const alerts =
        document.querySelectorAll(".alert");

    alerts.forEach(alert => {

        alert.remove();

    });

}, 4000);
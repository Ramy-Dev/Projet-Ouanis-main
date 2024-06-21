// custom_admin.js

document.addEventListener('DOMContentLoaded', function() {
    console.log("Custom admin JS loaded!");

    // Function to toggle dark mode
    window.toggleDarkMode = function() {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem('dark-mode', document.body.classList.contains('dark-mode'));
    };

    // Apply dark mode if previously enabled
    if (localStorage.getItem('dark-mode') === 'true') {
        document.body.classList.add('dark-mode');
    }
});

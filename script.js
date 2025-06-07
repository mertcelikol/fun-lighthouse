
function bookNow(service) {
    if (service === 'Paintball') {
        window.location.href = 'paintball.html';
    } else {
        window.location.href = 'waiver.html';
    }
}

function toggleMenu() {
      document.getElementById('nav-links').classList.toggle('active');
    }
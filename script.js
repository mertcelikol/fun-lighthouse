
function bookNow(service) {
    if (service === 'Go-Kart') {
        window.location.href = 'go-kart.html';
    } else {
        window.location.href = 'waiver.html';
    }
}

function toggleMenu() {
      document.getElementById('nav-links').classList.toggle('active');
    }
let sidebars = document.querySelectorAll('.sidebar');
let cards = document.querySelectorAll('.player-card');
let closeButtons = document.querySelectorAll('.button-close');

for(let i = 0; i < cards.length; i++) {
    cards[i].addEventListener('click', function() {
        for(let j = 0; j < sidebars.length; j++ ) {
            sidebars[j].classList.remove('active');
        }
        sidebars[i].classList.add('active');
    });
}

for(let i = 0; i < closeButtons.length; i++) {
    closeButtons[i].addEventListener('click', function() {
        for(let j = 0; j < sidebars.length; j++ ) {
            sidebars[j].classList.remove('active');
        }
    });
}
let sidebars = document.querySelectorAll('.sidebar');
let cards = document.querySelectorAll('.player-card');
let closeButtons = document.querySelectorAll('.button-close');

if( cards ) {
    for(let i = 0; i < cards.length; i++) {
        cards[i].addEventListener('click', function() {
            for(let j = 0; j < sidebars.length; j++ ) {
                sidebars[j].classList.remove('active');
            }
            sidebars[i].classList.add('active');
        });
    }
}

if( closeButtons ) {
    for(let i = 0; i < closeButtons.length; i++) {
        closeButtons[i].addEventListener('click', function() {
            for(let j = 0; j < sidebars.length; j++ ) {
                sidebars[j].classList.remove('active');
            }
        });
    }
}

let allGamesTable = document.querySelectorAll('table tr');

if( allGamesTable ) {
    for(let i = 0; i < allGamesTable.length; i++) {
        let lastLoser = allGamesTable[i].querySelector('td:last-of-type span:last-of-type');

        if( lastLoser ) {
            html = lastLoser.innerHTML;
            html = html.replace(", ", "");

            lastLoser.innerHTML = html;
        }
    }
}

let modalToggle = document.querySelector('#toggle-modal');

if( modalToggle ) {
    modalToggle.addEventListener('click', function() {
        let body = document.querySelector('body');
        let modal = document.querySelector('.modal-section');

        modal.classList.add('active');
        body.classList.add('modal-open');
    });
}

let closeModalButton = document.querySelector('#close-modal');

if( closeModalButton ) {
    closeModalButton.addEventListener('click', function() {
        let body = document.querySelector('body');
        let modal = document.querySelector('.modal-section');

        modal.classList.remove('active');
        body.classList.remove('modal-open');
    });
}

// Auto Selecting Winner and Runner Up in Participants Field
let winnerField = document.querySelector('#id_winner');
let runnerUpField = document.querySelector('#id_runner_up');
let participantsCheckboxes = document.querySelectorAll('.checkbox-wrapper .checkbox');

if( winnerField ) {
    winnerField.addEventListener('change', function() {
        //console.log(`Winner Changed: ${winnerField.value}`);
        let winner_id = winnerField.value;

        for(let i=0; i < participantsCheckboxes.length; i++ ) {
            //console.log(participantsCheckboxes[i].children.participants.value);
            if( participantsCheckboxes[i].children.participants.value === winner_id ) {
                //console.log(`${participantsCheckboxes[i].children.participants.value} matches!`);
                participantsCheckboxes[i].children.participants.checked = true;
            }
        }
    });
}

if( runnerUpField ) {
    runnerUpField.addEventListener('change', function() {
        let runner_up_id = runnerUpField.value;

        for(let i=0; i < participantsCheckboxes.length; i++ ) {
            //console.log(participantsCheckboxes[i].children.participants.value);
            if( participantsCheckboxes[i].children.participants.value === runner_up_id ) {
                //console.log(`${participantsCheckboxes[i].children.participants.value} matches!`);
                participantsCheckboxes[i].children.participants.checked = true;
            }
        }
    });
}
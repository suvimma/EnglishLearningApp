document.addEventListener('DOMContentLoaded', function () {
    let currentCardIndex = 0;
    const words = JSON.parse(document.getElementById('words-data').textContent);

    function displayFlashcard(index) {
        const cardFront = document.getElementById('english-word');
        const cardBack = document.getElementById('polish-word');
        cardFront.innerText = words[index].english_word;
        cardBack.innerText = words[index].polish_word;
        cardFront.style.display = 'flex';
        cardBack.style.display = 'none';
    }

    function flipCard() {
        const cardFront = document.getElementById('english-word');
        const cardBack = document.getElementById('polish-word');
        if (cardBack.style.display === 'none') {
            cardBack.style.display = 'flex';
            cardFront.style.display = 'none';
        } else {
            cardBack.style.display = 'none';
            cardFront.style.display = 'flex';
        }
    }

    function nextCard() {
        currentCardIndex = (currentCardIndex + 1) % words.length;
        displayFlashcard(currentCardIndex);
        updateProgress();
    }

    function prevCard() {
        currentCardIndex = (currentCardIndex - 1 + words.length) % words.length;
        displayFlashcard(currentCardIndex);
        updateProgress();
    }

    function shuffleFlashcards() {
        currentCardIndex = Math.floor(Math.random() * words.length);
        displayFlashcard(currentCardIndex);
        updateProgress();
    }

    function updateProgress() {
        const progressText = document.getElementById('progress-text');
        progressText.innerText = `${currentCardIndex + 1}/${words.length}`;
    }

    document.getElementById('flashcard').addEventListener('click', flipCard);
    document.getElementById('next-button').addEventListener('click', nextCard);
    document.getElementById('prev-button').addEventListener('click', prevCard);
    document.getElementById('shuffle-button').addEventListener('click', shuffleFlashcards);

    displayFlashcard(currentCardIndex);
    updateProgress();
});

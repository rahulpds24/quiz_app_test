const quizData = [
    {
        question: 'What is the correct form of the verb in this sentence: She ___ to the store every Saturday.',
        a: 'go',
        b: 'goes',
        c: 'gone',
        d: 'going',
        correct: 'b'
    },
    {
        question: 'Which sentence is grammatically correct?',
        a: 'He don’t like apples.',
        b: 'He doesn’t likes apples.',
        c: 'He doesn’t like apples.',
        d: 'He not like apples.',
        correct: 'c'
    },
    {
        question: 'Choose the correct word: Each of the boys ___ playing soccer.',
        a: 'is',
        b: 'are',
        c: 'were',
        d: 'be',
        correct: 'a'
    },
    {
        question: 'Identify the error: She have a great time at the party.',
        a: 'have',
        b: 'great',
        c: 'time',
        d: 'party',
        correct: 'a'
    }
];

const quiz = document.getElementById('quiz');
const submitButton = document.getElementById('submit');

function loadQuiz() {
    const currentQuizData = quizData[currentQuiz];
    questionEl.innerText = currentQuizData.question;
    answerEls.forEach((answerEl) => {
        answerEl.checked = false;
    });
    currentQuizData.a;
    answerEls[0].nextElementSibling.innerText = currentQuizData.a;
    answerEls[1].nextElementSibling.innerText = currentQuizData.b;
    answerEls[2].nextElementSibling.innerText = currentQuizData.c;
    answerEls[3].nextElementSibling.innerText = currentQuizData.d;
}

function getSelected() {
    let answer;
    answerEls.forEach((answerEl) => {
        if (answerEl.checked) {
            answer = answerEl.id;
        }
    });
    return answer;
}

let currentQuiz = 0;
let score = 0;

loadQuiz();

submitButton.addEventListener('click', () => {
    const answer = getSelected();
    if (answer) {
        if (answer === quizData[currentQuiz].correct) {
            score++;
        }
        currentQuiz++;
        if (currentQuiz < quizData.length) {
            loadQuiz();
        } else {
            quiz.innerHTML = `<h2>You scored ${score} out of ${quizData.length}</h2>`;
        }
    }
});
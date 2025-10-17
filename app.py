const quizData = [
    {
        question: 'What is the plural of "child"?',
        a: 'Childs',
        b: 'Children',
        c: 'Childes',
        d: 'Childrens',
        correct: 'b',
    },
    {
        question: 'Which sentence is correct?',
        a: 'He go to the store.',
        b: 'He goes to the store.',
        c: 'He gone to the store.',
        d: 'He going to the store.',
        correct: 'b',
    },
    {
        question: 'What is the past tense of "run"?',
        a: 'Runned',
        b: 'Ran',
        c: 'Running',
        d: 'Runs',
        correct: 'b',
    },
    {
        question: 'Choose the correct form: "She ___ to the party yesterday."',
        a: 'go',
        b: 'gone',
        c: 'went',
        d: 'going',
        correct: 'c',
    }
];

const quiz = document.getElementById('quiz');
const answerEls = document.querySelectorAll('.answer');
const questionEl = document.getElementById('question');
const a_text = document.getElementById('a_text');
const b_text = document.getElementById('b_text');
const c_text = document.getElementById('c_text');
const d_text = document.getElementById('d_text');
const submitBtn = document.getElementById('submit');

let currentQuiz = 0;
let score = 0;

loadQuiz();

function loadQuiz() {
    deselectAnswers();
    const currentQuizData = quizData[currentQuiz];
    questionEl.innerText = currentQuizData.question;
    a_text.innerText = currentQuizData.a;
    b_text.innerText = currentQuizData.b;
    c_text.innerText = currentQuizData.c;
    d_text.innerText = currentQuizData.d;
}

function deselectAnswers() {
    answerEls.forEach(answerEl => answerEl.checked = false);
}

function getSelected() {
    let answer;
    answerEls.forEach(answerEl => {
        if (answerEl.checked) {
            answer = answerEl.id;
        }
    });
    return answer;
}

submitBtn.addEventListener('click', () => {
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
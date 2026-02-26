const btn = document.getElementById('btn');
const greeting = document.getElementById('greeting');
const messages = ['Hello World!', 'Hello there!', 'Welcome!', 'Greetings!'];
let index = 0;

btn.addEventListener('click', () => {
    index = (index + 1) % messages.length;
    greeting.textContent = messages[index];
});

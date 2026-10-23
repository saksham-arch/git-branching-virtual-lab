const button = document.querySelector('#counter');
let count = 0;
button.addEventListener('click', () => { button.textContent = `Count: ${++count}`; });

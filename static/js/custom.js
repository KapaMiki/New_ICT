const inputArr = document.querySelectorAll('.subscribe input');
const subscribeTextarea = document.querySelectorAll('.subscribe textarea')[0];

inputArr[1].placeholder = 'Имя и фамилия';
inputArr[2].placeholder = 'Почта';
inputArr[3].placeholder = 'Телефон';

subscribeTextarea.placeholder = 'Ваш вопрос';
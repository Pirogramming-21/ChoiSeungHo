// 0~9 사이의 중복되지 않는 3개의 난수를 생성하는 함수
function generateUniqueRandomNumbers() {
    let numbers = [];
    while (numbers.length < 3) {
      let randomNumber = Math.floor(Math.random() * 10);
      if (!numbers.includes(randomNumber)) {
        numbers.push(randomNumber);
      }
    }
    return numbers;
  }
  
  // 답 미리보기
  let answer = generateUniqueRandomNumbers();
  console.log(answer);
  
 
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' && attempts > 0) {
      document.getElementsByClassName('submit-button')[0].click();
    }
  });
  
  // 입력칸 간 자동 이동을 위한 함수
  function autoFocus(current, next) {
    if (current.value.length === 1) {
      next.focus();
    }
  }
  

  document.getElementById('number1').addEventListener('input', () => {
    autoFocus(document.getElementById('number1'), document.getElementById('number2'));
  });
  
  document.getElementById('number2').addEventListener('input', () => {
    autoFocus(document.getElementById('number2'), document.getElementById('number3'));
  });
  
  // 남은 시도 횟수 초기화
  let attempts = 10;
  document.getElementById('attempts').textContent = attempts;
  
  // 숫자 확인 및 결과 처리 함수
  function check_numbers() {
    let number1 = document.getElementById('number1').value;
    let number2 = document.getElementById('number2').value;
    let number3 = document.getElementById('number3').value;
  
    if ((number1 === '' || number2 === '' || number3 === '')) {
      document.getElementById('number1').value = '';
      document.getElementById('number2').value = '';
      document.getElementById('number3').value = '';
      document.getElementById('number1').focus();
      return;
    }
  
    let inputs = [parseInt(number1), parseInt(number2), parseInt(number3)];
    let strike = 0;
    let ball = 0;
  
    for (let i = 0; i < inputs.length; i++) {
      if (inputs[i] === answer[i]) {
        strike++;
      } else if (answer.includes(inputs[i])) {
        ball++;
      }
    }
  
    const resultDisplay = document.querySelector('.result-display');
    const resultDiv = document.getElementById('results');
    const resultText = document.createElement('div');
    resultText.classList.add('check-result');
    resultDiv.appendChild(resultText);
  
    setTimeout(() => {
      resultDisplay.scrollTop = resultDisplay.scrollHeight;
    }, 0);
  
    if (strike === 0 && ball === 0) {
      resultText.innerHTML = `
        <div class="left">${number1} ${number2} ${number3}</div>
        :
        <div class="right">
          <div class="out num-result">O</div>
        </div>
      `;
    } else {
      resultText.innerHTML = `
        <div class="left">${number1} ${number2} ${number3}</div>
        :
        <div class="right">
          ${strike} <div class="strike num-result">S</div>
          ${ball} <div class="ball num-result">B</div>
        </div>
      `;
    }
  
    attempts--;
    document.getElementById('attempts').innerText = attempts;
  
    if (strike === 3) {
      document.getElementById('game-result-img').src = './success.png';
      document.getElementsByClassName('submit-button')[0].style.display = 'none';
    } else if (attempts <= 0) {
      document.getElementById('game-result-img').src = './fail.png';
      document.getElementsByClassName('submit-button')[0].style.display = 'none';
    }
  
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
    document.getElementById('number1').focus();
  }
  
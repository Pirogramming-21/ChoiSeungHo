let timer;
let milliseconds = 0;

const display = document.getElementById('display');
const startButton = document.getElementById('start');
const stopButton = document.getElementById('stop');
const resetButton = document.getElementById('reset');
const recordList = document.getElementById('record-list');
const selectAllCheckbox = document.getElementById('select-all');
const deleteSelectedButton = document.getElementById('delete-selected');
const deleteAllButton = document.getElementById('delete-all');

function formatTime(ms) {
    let totalSeconds = Math.floor(ms / 1000);
    let minutes = String(Math.floor(totalSeconds / 60)).padStart(2, '0');
    let seconds = String(totalSeconds % 60).padStart(2, '0');
    let milliseconds = String(ms % 1000).padStart(3, '0').slice(0, 2);
    return `${minutes}:${seconds}:${milliseconds}`;
}

function updateDisplay() {
    display.textContent = formatTime(milliseconds);
}

function startTimer() {
    if (!timer) {
        timer = setInterval(() => {
            milliseconds += 10;
            updateDisplay();
        }, 10);
    }
}

function stopTimer() {
    if (timer) {
        clearInterval(timer);
        timer = null;
        addRecord();
    }
}

function resetTimer() {
    stopTimer();
    milliseconds = 0;
    updateDisplay();
}

function addRecord() {
    const recordItem = document.createElement('li');
    recordItem.innerHTML = `<input type="checkbox" class="record-checkbox"> ${formatTime(milliseconds)}`;
    recordList.appendChild(recordItem);
    updateSelectAllCheckbox();
}

function updateSelectAllCheckbox() {
    const allChecked = Array.from(document.querySelectorAll('.record-checkbox')).every(cb => cb.checked);
    selectAllCheckbox.checked = allChecked;
}

startButton.addEventListener('click', startTimer);
stopButton.addEventListener('click', stopTimer);
resetButton.addEventListener('click', resetTimer);

selectAllCheckbox.addEventListener('change', () => {
    const checkboxes = document.querySelectorAll('.record-checkbox');
    checkboxes.forEach(cb => cb.checked = selectAllCheckbox.checked);
});

recordList.addEventListener('change', () => {
    updateSelectAllCheckbox();
});

deleteSelectedButton.addEventListener('click', () => {
    const selectedRecords = document.querySelectorAll('.record-checkbox:checked');
    selectedRecords.forEach(cb => cb.parentElement.remove());
    updateSelectAllCheckbox();
});

deleteAllButton.addEventListener('click', () => {
    recordList.innerHTML = '';
    selectAllCheckbox.checked = false;
});

updateDisplay();

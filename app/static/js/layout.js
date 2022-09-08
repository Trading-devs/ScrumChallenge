const coinsContainer = document.querySelector(".coins");
const containerTable = document.querySelector(".container-table");
const countdownTimer = document.querySelector(".timer");
let currency;

coinsContainer.addEventListener("click", function (e) {
  e.preventDefault();
  const target = e.target.closest(".coin");
  if (!target) return;
  updateUrl(target);
});

const updateUrl = function (newCurrency) {
  const path = newCurrency.querySelector(".coin__link").getAttribute("href");
  location.href = `/${path}`;
};

const countDownHandler = function (timeLeft) {
  // Set time to 5 minutes
  let time = timeLeft;
  countdownTimer.textContent = "";

  const tick = function () {
    const min = String(Math.trunc(time / 60)).padStart(2, 0);
    const second = String(Math.trunc(time % 60)).padStart(2, 0);
    // In each call, print the remaining time to UI
    countdownTimer.textContent = `${min}:${second}`;
    // Decrese 1s
    time--;

    // When 0 seconds, refresh the timer
    if (time < 0) {
      document.location.reload(true);
      time = 300;
    }
  };

  // Call the timer every second
  tick();
  const timer = setInterval(tick, 1000);
  return timer;
};

countDownHandler(timeLeft);

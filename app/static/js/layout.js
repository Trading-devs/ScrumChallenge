const coinsContainer = document.querySelector(".coins");
const containerTable = document.querySelector(".container-table");
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
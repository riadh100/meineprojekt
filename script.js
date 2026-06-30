document.addEventListener("DOMContentLoaded", () => {
  updateClock();
  setInterval(updateClock, 1000);

  initSearch();
  animateStats();
  initButtons();
});

function updateClock() {
  const clock = document.getElementById("clock");
  if (!clock) return;

  const now = new Date();

  clock.textContent = now.toLocaleTimeString("de-DE", {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
}

function initSearch() {
  const searchInput = document.querySelector(".top-actions input");
  if (!searchInput) return;

  searchInput.addEventListener("input", () => {
    const value = searchInput.value.toLowerCase();
    const cards = document.querySelectorAll(".module-card, .stat-card");

    cards.forEach((card) => {
      const text = card.textContent.toLowerCase();

      if (text.includes(value)) {
        card.style.display = "";
      } else {
        card.style.display = "none";
      }
    });
  });
}

function animateStats() {
  const stats = [
    {
      selector: ".stat-card:nth-child(1) strong",
      value: 12540,
      prefix: "+",
      suffix: " €",
    },
    {
      selector: ".stat-card:nth-child(2) strong",
      value: 128,
      prefix: "",
      suffix: "",
    },
    {
      selector: ".stat-card:nth-child(3) strong",
      value: 6,
      prefix: "",
      suffix: "",
    },
    {
      selector: ".stat-card:nth-child(4) strong",
      value: 24,
      prefix: "",
      suffix: "",
    },
  ];

  stats.forEach((stat) => {
    const element = document.querySelector(stat.selector);
    if (!element) return;

    animateNumber(element, stat.value, stat.prefix, stat.suffix);
  });
}

function animateNumber(element, target, prefix = "", suffix = "") {
  let current = 0;
  const duration = 900;
  const steps = 30;
  const increment = target / steps;
  const interval = duration / steps;

  const timer = setInterval(() => {
    current += increment;

    if (current >= target) {
      current = target;
      clearInterval(timer);
    }

    element.textContent =
      prefix + Math.round(current).toLocaleString("de-DE") + suffix;
  }, interval);
}

function initButtons() {
  const dashboardButton = document.querySelector(".hero-card button");

  if (dashboardButton) {
    dashboardButton.addEventListener("click", () => {
      alert("AI Empire Pro V9 Dashboard ist aktiv ✅");
    });
  }

  const moduleLinks = document.querySelectorAll(".module-card a");

  moduleLinks.forEach((link) => {
    link.addEventListener("click", () => {
      console.log("Öffne Modul:", link.getAttribute("href"));
    });
  });
}

const quoteText = document.getElementById('quote-text');
const quoteAuthor = document.getElementById('quote-author');
const newQuoteButton = document.getElementById('new-quote');

newQuoteButton.addEventListener('click', getQuote);

async function getQuote() {
  const response = await fetch('https://api.quotable.io/random');
  const data = await response.json();
  quoteText.innerText = data.content;
  quoteAuthor.innerText = `- ${data.author}`;
}

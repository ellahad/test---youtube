document.getElementById('sentiment-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var text = document.getElementById('text').value;
    fetch('/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: 'text=' + encodeURIComponent(text)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = 'Sentiment: ' + data.result;
    });
});

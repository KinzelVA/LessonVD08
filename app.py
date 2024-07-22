import requests
from flask import Flask, render_template

app = Flask(__name__)

def get_random_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def index():
    quote = get_random_quote()
    if quote:
        content = quote['content']
        author = quote['author']
    else:
        content = "Unable to fetch quote at this time."
        author = ""
    return render_template('index.html', content=content, author=author)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello Word</h1>"

@app.route('/about')
def about():
    return "<h1> This is About Page </h1>

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/hello")
def hello():
    return render_template('hello.html')

@app.route("/layout")
def layout():
    return render_template('layout.html')
    
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

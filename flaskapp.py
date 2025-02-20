from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return f'''
        <h1>Welcome to the Home Page</h1>
        <p>Go to the <a href="{url_for('hello')}">Hello Page</a></p>
        <p>Go to the <a href="{url_for('hello', city='New York')}">Hello New York Page</a></p>
    '''

@app.route("/hello")
@app.route("/hello/<city>")
def hello(city=None):
    if city is None or city == "":
        return "<h1>Hello!</h1>"
    else:
        return f"<h1>Hello, {city}!</h1>"
    

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

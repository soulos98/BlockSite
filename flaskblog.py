from flask import Flask
app = Flask(__name__) # __name__ is just the name of the module

@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Hello World!<h1>"

@app.route("/about")
def about():
    return "<h1>This is my about page<h1>"

if __name__ == '__main__':
    app.run(debug=True)
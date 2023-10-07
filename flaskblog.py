from flask import Flask, render_template
app = Flask(__name__) # __name__ is just the name of the module

posts = [
    {
        'author': 'Jose A. Garcia',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted': 'October 7, 2023'
    },
    {
        'author': 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted': 'April 21, 2023'        
    }
]
@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    app.run(debug=True)
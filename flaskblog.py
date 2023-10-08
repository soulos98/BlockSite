from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
# __name__ is just the name of the module
app = Flask(__name__, template_folder='templates/',
            static_folder='templates/static/')

app.config['SECRET_KEY'] = '4a28bc28e85ac9c6ac127878de8b84f7'

posts = [
    {
        'author': 'Jose A. Garcia',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 7, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2023'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts, title='home')


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

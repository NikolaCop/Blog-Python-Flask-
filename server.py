from flask import Flask, render_template, redirect, request
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nikola#!22'

@app.route('/')
def home():
    return 'Hello World'

@app.route('/about')
def about():
    return 'The About Page'

@app.route('/blog')
def blog():
    posts = [{'title': 'Technology in 2021', 'author': 'Nikola C.'},
             {'title': 'Why Porsche makes the best Automobiles', 'author': 'Nikola Also.'}]
    return render_template('blog.html', author='Nikola Cop', sunny=False, posts=posts)

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is Blog ' + blog_id

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run()


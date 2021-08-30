from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run()


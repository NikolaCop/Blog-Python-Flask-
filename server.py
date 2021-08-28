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
    return render_template('blog.html', author = 'Nikola', blogName = 'Test Blog')

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is Blog ' + blog_id

if __name__ == '__main__':
    app.run()

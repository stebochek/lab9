from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_projects.db'
db = SQLAlchemy(app)


class Article():
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, primary_key=True, nullable=False)
    link = db.Column(db.String, primary_key=True, nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']
        link = request.form['link']

        article = Article(title=title, link=link)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return "Пока"
    else:
        return render_template('index.html')


@app.route('/posts')
def posts():
    articles = Article.query.all()
    return render_template('posts.html')

app.run()
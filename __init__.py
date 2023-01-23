import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from seed_groups_data import Group

base_dir = os.path.dirname(__file__)

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(base_dir, 'data2.db')}"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f'{self.name}'


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, group_id, name):
        self.group_id = group_id
        self.name = name


class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __init__(self, bill_id, description, amount):
        self.bill_id = bill_id
        self.description = description
        self.amount = amount


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/bills")
def bills():
    bills = Bill.query.all()
    return render_template("bills.html", bills=bills)


# @app.route("/bills/<int:id>")
# def bills(id):
#     bills = Bill.query.get(id)
#     return render_template("bills.html", bills=bills)


@app.route("/groups")
def groups():
    groups = Group.query.all()
    return render_template("groups.html", groups=groups)

# @app.route('/article/add', methods=['GET', 'POST'])
# def add_article():
#     form = ArticleForm(request.form)
#     if request.method == 'POST' and form.validate():
#         article = Articles(form.author.data.id,
#                            form.title.data, form.text.data)
#         for tag in form.tags.data:
#             article.tags.append(Tags.query.get(tag.id))
#         db.session.add(article)
#         db.session.commit()
#         flash('Forma išsaugota sėkmingai')
#         return redirect('/')
#     return render_template('addArticle.html', form=form)


if __name__ == "__main__":
    app.run(port=8000, debug=True)

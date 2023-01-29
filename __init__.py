import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vfv822fvfv26f5dfadsrfasdr54e6rae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data_base.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'register'
login_manager.login_message_category = 'info'

# users_groups = db.Table('users_groups', db.metadata,
#                         db.Column('group_id', db.Integer,
#                                   db.ForeignKey('group.id')),
#                         db.Column('user_id', db.Integer, db.ForeignKey('user.id')))


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column("First Name", db.String(100), nullable=False)
#     email = db.Column("Email", db.String(100),
#                       unique=True, nullable=False)
#     password = db.Column("Password", db.String(100),
#                          unique=True, nullable=False)
#     groups = db.relationship(
#         'Group', secondary=users_groups, back_populates="users")


# class Group(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     users = db.relationship(
#         'User', secondary=users_groups, back_populates="groups")

#     def __init__(self, name):
#         self.name = name


# class Bill(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     amount = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(100), nullable=False)
#     group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
#     group = db.relationship("Group")

# def __init__(self, group_id, amount, description):
#     self.group_id = group_id
#     self.amount = amount
#     self.description = description


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     db.create_all()
#     if current_user.is_authenticated:
#         return redirect(url_for('login'))
#     form = forms.RegistrationForm()
#     if form.validate_on_submit():
#         encrypted_password = bcrypt.generate_password_hash(
#             form.password.data).decode('utf-8')
#         user = User(
#             first_name=form.name.data, email=form.email.data, password=encrypted_password)
#         db.session.add(user)
#         db.session.commit()
#         flash('You have successfully registered!', 'success')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)


# @app.route("/", methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('groups', id=current_user.id))
#     form = forms.LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(
#             email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             login_user(user)
#             return redirect(url_for('groups', id=user.id))
#         else:
#             flash('Login failed. Check your email and password', 'danger')
#     return render_template('login.html', title='Login', form=form)


# @app.route("/groups/<int:id>", methods=['GET', 'POST'])
# @login_required
# def groups(id):
#     db.create_all()
#     current_user = User.query.get(id)
#     groups = Group.query.all()
#     form = forms.AddGroupForma()
#     if form.validate_on_submit():
#         adding_group = Group.query.get(form.group_id.data)
#         current_user.groups.append(adding_group)
#         db.session.add(current_user)
#         db.session.commit()
#         flash('Group added successfully!', 'success')
#         return redirect(url_for('groups', id=current_user.id))
#         # 2nd option
#         # return redirect(request.url)
#     return render_template('groups.html', groups=groups, current_user=current_user, form=form)


# @app.route("/bills")
# @login_required
# def bills():
#     bills = Bill.query.all()
#     return render_template("bills.html", bills=bills)


# @app.route("/bill/<int:id>", methods=['GET', 'POST'])
# @login_required
# def bill(id):
#     db.create_all()
#     group = Group.query.get(id)
#     bills = Bill.query.all()
#     form = forms.AddBillForma()
#     if form.validate_on_submit():
#         bill = Bill(group_id=group.id, amount=form.amount.data,
#                     description=form.description.data)
#         db.session.add(bill)
#         db.session.commit()
#         flash('Bill added successfully!', 'success')
#         return redirect(url_for('bill', id=group.id))
#         # 2nd option
#         # return redirect(request.url)
#     return render_template('bill.html', group=group, bills=bills, form=form)


# @app.route("/logout", methods=['GET', 'POST'])
# def logout():
#     logout_user()
#     return redirect(url_for('login'))


# @app.errorhandler(404)
# def not_found(error):
#     return render_template('not_found.html'), 404


# @app.errorhandler(500)
# def server_error(error):
#     return render_template('server_error.html'), 500


if __name__ == "__main__":
    app.run(port=8000, debug=True)

import os
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user, logout_user, login_user, UserMixin, login_required
import forms

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

users_groups = db.Table('users_groups', db.metadata,
                        db.Column('group_id', db.Integer,
                                  db.ForeignKey('group.id')),
                        db.Column('vartotojas_id', db.Integer, db.ForeignKey('vartotojas.id')))


class Vartotojas(db.Model, UserMixin):
    __tablename__ = "vartotojas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String(100), nullable=False)
    el_pastas = db.Column("El. pašto adresas", db.String(100),
                          unique=True, nullable=False)
    slaptazodis = db.Column("Slaptažodis", db.String(100),
                            unique=True, nullable=False)
    groups = db.relationship(
        'Group', secondary=users_groups, back_populates="vartotojai")


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    vartotojai = db.relationship(
        'Vartotojas', secondary=users_groups, back_populates="groups")

    def __init__(self, name):
        self.name = name


class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relationship("Group")

    # def __init__(self, group_id, amount, description):
    #     self.group_id = group_id
    #     self.amount = amount
    #     self.description = description


@login_manager.user_loader
def load_user(vartotojo_id):
    return Vartotojas.query.get(int(vartotojo_id))


@app.route("/register", methods=['GET', 'POST'])
def register():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = forms.RegistracijosForma()
    if form.validate_on_submit():
        koduotas_slaptazodis = bcrypt.generate_password_hash(
            form.slaptazodis.data).decode('utf-8')
        vartotojas = Vartotojas(
            vardas=form.vardas.data, el_pastas=form.el_pastas.data, slaptazodis=koduotas_slaptazodis)
        db.session.add(vartotojas)
        db.session.commit()
        flash('You have successfully registered!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('groups', id=current_user.id))
    form = forms.PrisijungimoForma()
    if form.validate_on_submit():
        user = Vartotojas.query.filter_by(
            el_pastas=form.el_pastas.data).first()
        if user and bcrypt.check_password_hash(user.slaptazodis, form.slaptazodis.data):
            login_user(user)
            return redirect(url_for('groups', id=user.id))
        else:
            flash('Login failed. Check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/groups/<int:id>", methods=['GET', 'POST'])
@login_required
def groups(id):
    db.create_all()
    prisijunges_vartotojas = Vartotojas.query.get(id)
    groups = Group.query.all()
    form = forms.AddGroupForma()
    if form.validate_on_submit():
        pridedama_group = Group.query.get(form.group_id.data)
        prisijunges_vartotojas.groups.append(pridedama_group)
        db.session.add(prisijunges_vartotojas)
        db.session.commit()
        flash('Group saved successfully!', 'success')
        return redirect(url_for('groups', id=prisijunges_vartotojas.id))
        # 2nd option
        # return redirect(request.url)
    return render_template('groups.html', groups=groups, prisijunges_vartotojas=prisijunges_vartotojas, form=form)


@app.route("/bills")
@login_required
def bills():
    bills = Bill.query.all()
    return render_template("bills.html", bills=bills)


@app.route("/bill/<int:id>", methods=['GET', 'POST'])
@login_required
def bill(id):
    db.create_all()
    group = Group.query.get(id)
    bills = Bill.query.all()
    form = forms.AddBillForma()
    if form.validate_on_submit():
        bill = Bill(group_id=group.id, amount=form.amount.data,
                    description=form.description.data)
        db.session.add(bill)
        db.session.commit()
        flash('Bill saved successfully!', 'success')
        return redirect(url_for('bill', id=group.id))
        # 2nd option
        # return redirect(request.url)
    return render_template('bill.html', group=group, bills=bills, form=form)


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(port=8000, debug=True)

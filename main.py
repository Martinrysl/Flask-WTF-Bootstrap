from flask import Flask, render_template, redirect, url_for, request
from wtforms import PasswordField, SubmitField, EmailField, IntegerField, FormField, Form, validators
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length, ValidationError
from wtforms.validators import InputRequired, Email
from flask import Flask
from flask_bootstrap import Bootstrap


class SignUpForm(FlaskForm):
    email = EmailField(label='Email',
                       validators=[DataRequired(), Email(granular_message=True, check_deliverability=True)])

    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(max=50, min=3, message='Password must have at least  characters')
    ])
    submit = SubmitField('Log In')


app = Flask(__name__)
app.secret_key = 'codex'
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = SignUpForm()
    if form.validate_on_submit():
        if form.email.data == 'martinreyez34@gmail.com' and form.password.data == 'conejitoloco':
            print(form.email.data)
            print(form.password.data)
            return redirect('/success')
        else:
            print(form.email.data)
            print(form.password.data)
            return render_template('denied.html')
    return render_template('login.html', form=form)


@app.route("/success")
def success():
    return render_template('success.html')


@app.route("/denied")
def denied():
    return render_template('denied.html')


@app.route("/fast")
def fast():
    form = SignUpForm()
    return render_template('fast.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)


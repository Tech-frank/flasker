from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)


app.config['SECRET_KEY'] = 'kkii'
#form class
class NamerForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')

def index():    
    
    return render_template('index.html')

@app.route('/user/<name>')

def user(name):
    return render_template('user.html', name = name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 400

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

        flash("Form Submitted Succesfully!")
    return render_template('name.html', name=name, form=form,)

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/inicio')
def inicio():
    return render_template('index.html', title='Inicio') 


@app.route('/Ingresar', methods=['GET', 'POST'])
def ingresar():
    form = LoginForm()
    if form.validate_on_submit(): #Checks if everything is ok with the form
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('inicio'))
    return render_template('login.html', title='Ingresar', form=form)
    

@app.route('/Registrate')
def registrate():
    return render_template('registrate.html', title='Registrate')


@app.route('/Telas')
def telas():
    return render_template('telas.html', title='Telas')


@app.route('/Nosotros')
def nosotros():
    return render_template('nosotros.html', title='Nosotros')

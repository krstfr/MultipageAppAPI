from flask import render_template, request, redirect, url_for
import requests
from app import app
#from the app folder import the app instance from the __init__ file
from .forms import LoginForm, RegisterForm
#from the forms in the same directory that I live in
from .models import User
from flask_login import login_user, logout_user, current_user, login_required

#Routes
@app.route('/', methods=['GET'])
@login_required
def index():
#this index function will be passed through the route function
    return render_template('index.html.j2')

@app.route('/students', methods=['GET'])
@login_required
def students(): 
    the_students = ["Thu", "Leo", "Sydney", "Josh", "Chris", "Fernando", "Benny", "Vicky", "Bradley"]
    return render_template('students.html.j2', students=the_students)

@app.route('/pokemon', methods=['GET', 'POST'])
@login_required
def pokemon():
    if request.method == 'POST':
        name = request.form.get('name')
        url = f"https://pokeapi.co/api/v2/pokemon/{name}" 
        response = requests.get(url)
        if response.ok:
            try:
                data = response.json()
            except:
                error_string =f'There is no pokemon named {name}'
                return render_template("pokemon.html.j2", error= error_string)
            # pokemon_data = []
            # for data in data:
            pokemon_data={ # renamed pokemon data
                "Name" : data['forms'][0]['name'],
                "Ability": data['abilities'][0]['ability']['name'],
                "Base Experience" : data['base_experience'], # Fixed typo in name
                "Sprite URL" : data['sprites']['front_shiny']
                }
                # pokemon_data.append(pokemon_data_dict)
            return render_template("pokemon.html.j2", data =pokemon_data)
        else: 
            error_string ="Something is Wrong"
            render_template("pokemon.html.j2", error = error_string)
    return render_template("pokemon.html.j2")

@app.route('/logout', methods=['GET'])
@login_required
def logout(): 
    if current_user is not None:
        logout_user()
        return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            new_user_data={
                "first_name":form.first_name.data.title(),
                "last_name":form.last_name.data.title(),
                "email":form.email.data.lower(),
                "password":form.password.data
            }
            new_user_object = User()
            new_user_object.from_dict(new_user_data)
        except:
            error_string="There was a problem creating your account. Please try again"
            return render_template('register.html.j2', form=form, error=error_string)
        #Give the user some feedback that says registered successfully
        return redirect(url_for('login'))
    return render_template('register.html.j2', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        #Do Login Stuff
        email = form.email.data.lower()
        password = form.password.data
        u = User.query.filter_by(email=email).first()
        if u is not None and u.check_hashed_password(password): 
            login_user(u)
            # Give User Feedback of success
            return redirect(url_for('index'))
        else:
            #Give User Invalid password combo error
            return redirect(url_for('login'))

    return render_template('login.html.j2',form=form ) 



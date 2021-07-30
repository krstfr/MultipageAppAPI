from flask import render_template, request
import requests
from app import app
#from the app folder import the app instance from the __init__ file
from .forms import LoginForm
#from the forms in the same directory that I live in

#Routes
@app.route('/', methods=['GET'])
def index():
#this index function will be passed through the route function
    return render_template('index.html.j2')

@app.route('/students', methods=['GET'])
def students(): 
    the_students = ["Thu", "Leo", "Sydney", "Josh", "Chris", "Fernando", "Benny", "Vicky", "Bradley"]
    return render_template('students.html.j2', students=the_students)

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        #Do Login Stuff
        email = form.email.data.lower()
        password = form.password.data
        if email in app.config.get('REGISTERED_USERS', {}).keys() and\
            password == app.config.get('REGISTERED_USERS', {}).get(email).get('password'):
            #Login Success
                return f"Login Successful Welcome {app.config.get('REGISTERED_USERS', {}).get(email).get('name')}" 
        error_string = "Incorrect Email/Password Combo"
        return render_template("login.html.j2", form =form ,error = error_string)
    return render_template('login.html.j2',form=form ) 

@app.route('/pokemon', methods=['GET', 'POST'])
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
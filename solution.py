
# {% extends 'base.html' %}
# {% block content %}
#  <h1>Pick A Pokemon</h1>
#  <form action="/pokemon" method="POST">
#   <div class="mb-3">
#     <label for="Name" class="form-label">Name</label>
#     <input type="text" name = "name" class="form-control" id="name">
#   </div>
#   <button type="submit" class="btn btn-primary">Submit</button>
# </form>
#     {% if error %}
#         <small style="color:red;">{{error}}</small>
#     {% else %}
#         <small style="color:blue;">There was no error</small>
#     {% endif %}
# <!--table for pokemon data--> 
#     {% if data %}
#         <table class="table table-striped table-hover">
#   <thead>
#     <tr>
#         <th scope="col">Name</th>
#         <th scope="col">Ability</th>
#         <th scope="col">Base Experience</th>
#         <th scope="col">Sprite URL</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#         <th scope="row">{{data['Name']}}</th>
#         <td>{{data['Ability']}}</td>
#         <td>{{data['Base Experience']}}</td>
#         <td>{{data['Sprite URL']}}</td>
#     </tr>
#   </tbody>
# </table>
#     {% endif %}
# {% endblock %}







# @app.route('/pokemon', methods=['GET', 'POST'])
# def pokemon():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         url = f"https://pokeapi.co/api/v2/pokemon/{name}" 
#         response = requests.get(url)
#         if response.ok:
#             try:
#                 data = response.json()
#             except:
#                 error_string =f'There is no pokemon named {name}'
#                 return render_template("pokemon.html.j2", error= error_string)
#             # pokemon_data = []
#             # for data in data:
#             pokemon_data={ # renamed pokemon data
#                 "Name" : data['forms'][0]['name'],
#                 "Ability": data['abilities'][0]['ability']['name'],
#                 "Base Experience" : data['base_experience'], # Fixed typo in name
#                 "Sprite URL" : data['sprites']['front_shiny']
#                 }
#                 # pokemon_data.append(pokemon_data_dict)
#             return render_template("pokemon.html.j2", data =pokemon_data)
#         else: 
#             error_string ="Something is Wrong"
#             render_template("pokemon.html.j2", error = error_string)
#     return render_template("pokemon.html.j2")


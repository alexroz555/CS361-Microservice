# CS361-Microservice
Microservice (ingredient lookup) for Alby's World web application
In order to run the main application code with this microservice, first type "main.py" to run the main code in a terminal. Then
in a separate terminal, type "microservice.py", which will open the microservice in a separate port (which the main program will
later call upon).

To request data from the microservice, main.py needs to call the microservice file, like this call that I included in my copy of main.py to access the microservice:

```python
@app.route("/lookup-ingredients", methods=['GET','POST'])
def lookup_ingredients():
    ingredient = None
    ingredient_safety = None
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        microservice_url = 'http://127.0.0.1:5001/lookup-ingredients'
        response = requests.post(microservice_url, data={'ingredient':ingredient})
        ingredient_safety = response.text
    return render_template("ing_page.html", ingredient=ingredient, safety_info=ingredient_safety)
```
The microservice file will then return the data with this call:
```python
@app.route("/lookup-ingredients", methods=['POST'])
def lookup_ingredients():
    ingredient = request.form['ingredient'].lower()
    ingredient_safety = read_safety_info().get(ingredient, "Ingredient not found")
    return ingredient_safety
```

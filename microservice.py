from flask import Flask, render_template, request, redirect, url_for
import csv

def read_safety_info():
    safety_info = {}
    try:
        with open('food.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ingredient = row['Ingredient'].lower()
                safety = row['Safety']
                if safety == "Safe":
                    safety_info[ingredient] = "Safe for dogs to eat"
                if safety == "Toxic":
                    safety_info[ingredient] = "This ingredient is toxic to dogs"
                if safety == "Dairy":
                    safety_info[ingredient] = "Dairy products are usually safe for dogs to eat but should be limited to avoid digestive issues"
                if safety == "Limit":
                    safety_info[ingredient] = "This ingredient is usually safe for dogs to eat but should be limited in their diet"
                if safety == "Peanut":
                    safety_info[ingredient] = "Peanut butter, preferably without added salt or sugar, is safe for dogs to eat as long as it doesn't contain xylitol"
                if safety == "Tomato":
                    safety_info[ingredient] = "Tomatoes are safe for dogs to eat but green tomatoes are toxic"
                if safety == "Cashew":
                    safety_info[ingredient] = "Only roasted cashews are safe for dogs to eat, raw cashews are toxic"
    except Exception as e:
        print("error reading csv file")
    return safety_info
app = Flask(__name__)

#send information to main program
@app.route("/lookup-ingredients", methods=['POST'])
def lookup_ingredients():
    ingredient = request.form['ingredient'].lower()
    ingredient_safety = read_safety_info().get(ingredient, "Ingredient not found")
    return ingredient_safety

#go back to previous page
@app.route("/newRecipe", methods=['GET','POST'])
def return_home():
    if request.method == 'GET':
        return render_template("newRecipe.html")
    elif request.method == 'POST':
        return redirect(url_for('new_recipe'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)

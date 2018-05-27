from bottle import route, run, request, post
from pymongo import MongoClient

database = MongoClient()

db = database.shipdroid

recipes = db.recipes


@post("/recipe")
def add_to_db():
	post_data = request.body.read()

	recipe_data = {
		"product": post_data.product,
		"content": post_data.content
	}

	recipes.insert_one(recipe_data)

	return "Recipe successfully added. &nbsp; Product: {product}, Content: {content}".format(product = post_data.product, content = post_data.content)
	print("Recipe successfully added. &nbsp; Product: {product}, Content: {content}".format(product = post_data.product, content = post_data.content))

run(host='localhost', port=1818, debug=True)
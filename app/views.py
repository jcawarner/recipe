from django.shortcuts import render
import requests
import json

def home(request):


	return render(request, "home.html", {})


def search(request):

	url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

	if request.method == 'POST':
		recipe_search = request.POST['food']

		querystring = {"query":recipe_search,"number":"10","type":"main course"}

		headers = {
		    'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8",
		    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
		    }

		response = requests.request("GET", url, headers=headers, params=querystring)
		recipes = json.loads(response.content)

		return render(request, 'search.html', {'recipes':recipes})
	else:
		return render(request, 'search.html', {})


def get_recipe(request):

	if request.method == 'POST':
		new_recipe = request.POST['recipe']

		url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + new_recipe + "/information"



		headers = {
		    'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8",
		    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
		    }

		response = requests.request("GET", url, headers=headers)
		recipe_info = json.loads(response.content)


		return render(request, 'get_recipe.html', {'recipe_info':recipe_info})

	else:
		return render(request, 'get_recipe.html', {})


def random(request):

	url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random?number=1"

	headers = {
	    'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8",
	    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
	    }

	response = requests.request("GET", url, headers=headers)
	recipeinfo = json.loads(response.content)
	
	return render(request, "random.html", {'recipeinfo':recipeinfo})



	


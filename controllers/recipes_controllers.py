import os

from flask import render_template, request
import requests

SPOONACULAR_API_KEY = os.environ.get('SPOONACULAR_API_KEY')

def search_recipes_in_api():
    search_input = request.args.get('search_input')
    print(f"Search imput is {search_input}")
    api_url = f'https://api.spoonacular.com/recipes/complexSearch?query={search_input}&apiKey={SPOONACULAR_API_KEY}'
    print(f"API url is {api_url}")
    response = requests.get(api_url).json()
    print(response)
    search_results = response['results']
    return render_template('/recipes/search.html', search_results = search_results)

def view_recipe_info_in_api(id):
    api_url = f'https://api.spoonacular.com/recipes/{id}/information?apiKey={SPOONACULAR_API_KEY}'
    recipe_info = requests.get(api_url).json()
    return render_template('/recipes/recipe_description.html', recipe_info = recipe_info)
from selenium import webdriver
import json
import requests

def get_recipe(ingredients):
    url = 'https://api.spoonacular.com/recipes/findByIngredients'
    params = {
        'ingredients': ingredients,
        'number': 1,
        'ranking': 1,
        'apiKey': 'MY_API_KEY'
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    print('You are missing: ' + ''.join([data[0]['missedIngredients'][i]['name'] for i in range(data[0]['missedIngredientCount'])]))
    id = data[0]['id']
    response = requests.get(f'https://api.spoonacular.com/recipes/{id}/information', params={'apiKey': 'MY_API_KEY'})
    data = json.loads(response.text)
    return data['sourceUrl']

def open_recipe(recipe_url):
    global driver
    driver = webdriver.Chrome()
    driver.get(recipe_url)

ingredients = input('Enter a list of food ingredients separated by commas: ')
ingredients = ingredients.split(",")
url = get_recipe(ingredients)
open_recipe(url)

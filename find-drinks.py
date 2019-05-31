#!/usr/bin/env python3

# Get the simplified recipes
L = [r.split('\n') for r in open('simple.txt', 'r').read().strip().split('\n\n')]
L = sorted(L)
recipes = []
for recipe in L:
    recipes.append(dict(name=recipe[0], type=recipe[1], ingredients=recipe[2:]))

# Get the ingredients
ingredients = set()
for recipe in recipes:
    for ing in recipe['ingredients']:
        ingredients.add(ing)
print('Got', len(recipes), 'recipes using',
      len(ingredients), 'ingredients from simple.txt')

# Write the ingredients
f = open('ingredients.out', 'w')
for ing in sorted(ingredients):
    f.write(ing + '\n')
f.close()

# Read the ingredients I have
try:
    my_ingredients = open('my-ingredients.txt', 'r').read().strip().split('\n')
except FileNotFoundError:
    my_ingredients = []
print('Got', len(my_ingredients), 'ingredients from my-ingredients.txt')

# Show unknown ingredients
unknown_ingredients = [i for i in my_ingredients if i not in ingredients]
if len(unknown_ingredients) > 0:
    print("Found", len(unknown_ingredients), "unknown ingredient(s):",
          ', '.join(unknown_ingredients))

# Find all valid drinks
print('Finding recipes you can make...\n')
drinks = []
for recipe in recipes:
    recipe['missing'] = {i for i in recipe['ingredients']
                         if i not in my_ingredients}
    if len(recipe['missing']) == 0:
        drinks.append(recipe)
types = {drink['type'] for drink in drinks}
for type in sorted(types):
    print(type.upper() + 'S:')
    for drink in drinks:
        if drink['type'] == type:
            print('  ' + drink['name'] + ' - ' + ', '.join(drink['ingredients']))

# Find enabling ingredients
to_buy = {}
for recipe in recipes:
    if len(recipe['missing']) == 1:
        to_buy[next(iter(recipe['missing']))] = []
for recipe in recipes:
    if len(recipe['missing']) == 1:
        to_buy[next(iter(recipe['missing']))].append(recipe['name'])
print('\nGOOD INGREDIENTS TO BUY:')
for tb in sorted(to_buy, key=(lambda i: [-len(to_buy[i]), i])):
    print('  (' + str(len(to_buy[tb])) + ') ' + tb + ' - ' + ', '.join(to_buy[tb]))


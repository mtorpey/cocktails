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

# Helper function for computing covers
def all_covers(sets, size):
    """Return the sets of size no more than `size` that cover as many of `sets` as possible"""
    unique_sets = []
    [unique_sets.append(s) for s in sets if len(s) <= size and s not in unique_sets]
    unions = unique_sets.copy()
    covers = []
    i = 0
    while i < len(unions):
        covers.append(0)
        for s in sets:
            if s.issubset(unions[i]):
                covers[i] += 1
        for s in unique_sets:
            u = unions[i].union(s)
            if len(u) <= size and u not in unions:
                unions.append(u)
        i += 1
    if unions == []:
        return []
    return sorted(unions, key=lambda s: (-covers[unions.index(s)], len(s), list(s)))

def best_covers(sets, size):
    unions = all_covers(sets, size)
    best_unions = []
    lastcover = None
    for u in unions:
        cover = 0
        for s in sets:
            if s.issubset(u):
                cover += 1
        if lastcover == None or cover == lastcover:
            best_unions.append(u)
            lastcover = cover
        else:
            break
    return best_unions

incomplete_recipes = [recipe for recipe in recipes if len(recipe['missing']) > 0]
missing_sets = [recipe['missing'] for recipe in incomplete_recipes]

# Find enabling ingredients
print("\nIF YOU'RE BUYING ONE INGREDIENT:")
best = all_covers(missing_sets, 1)
for s in best:
    allows = [recipe['name'] for recipe in incomplete_recipes
              if all([ing in s for ing in recipe['missing']])]
    print('  (' + str(len(allows)) + ') ' + ', '.join(sorted(s)) + ' - ' + ', '.join(allows))

# Find ingredient sets
print("\nIF YOU'RE BUYING TWO INGREDIENTS:")
best = best_covers(missing_sets, 2)
for s in best:
    allows = [recipe['name'] for recipe in incomplete_recipes
              if all([ing in s for ing in recipe['missing']])]
    print('  (' + str(len(allows)) + ') ' + ', '.join(sorted(s)) + ' - ' + ', '.join(allows))

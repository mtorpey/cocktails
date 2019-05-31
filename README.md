# Cocktail recipe script

- `recipes.txt`: fragments of cocktail recipes scraped from the IBA website
- `simple.txt`: cocktail recipes in the form `name type ingredients blankline`
- `my-ingredients.txt`: a list of cocktail ingredients you have at home
- `find-drinks.py`: Python script that tells you what drinks you can make and
  what ingredients you should buy
    
To use, create a `my-ingredients.txt` file with all your cocktail ingredients on
separate lines, then call `./find-drinks.py` or `python3 find-drinks.py`.  It
will tell you what drinks you can make, as well as what single ingredients you
can buy to allow new drinks.  It will also notify you of any ingredients it
doesn't recognise (case sensitive).

- `ingredients.out`: a list of recognised ingredients (generated whenever you
  run `find-drinks.py`)

Requires Python 3.

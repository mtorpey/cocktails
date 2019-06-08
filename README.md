# Cocktail recipe script

- `human recipes.txt`: fragments of cocktail recipes scraped from the IBA website
- `recipes/*.txt`: cocktail recipes in the form `name type ingredients blankline`
- `find-drinks.py`: Python script that tells you what drinks you can make and
  what ingredients you should buy
    
To use, create a `my-ingredients.txt` file with all your cocktail ingredients on
separate lines, then call `./find-drinks.py` or `python3 find-drinks.py`.  It
will tell you what drinks you can make, as well as what ingredients you
can buy to allow new drinks.  It will also notify you of any ingredients it
doesn't recognise (case sensitive).

- `ingredients.out`: a list of recognised ingredients (generated whenever you
  run `find-drinks.py`) - you might want to copy ingredients from here when you
  make `my-ingredients.txt`

Requires Python 3.

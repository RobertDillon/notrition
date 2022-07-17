from http import HTTPStatus
from recipe_scrapers import scrape_me
import notion
import sys

if len(sys.argv) <= 1:
    print('No recipe URL passed as a parameter, re-run with a valid recipe link.')
    exit(1)
else:
    recipeUrl = sys.argv[1]

def startNotriton(recipeUrl):
    try:
        scraper = scrape_me(recipeUrl, wild_mode=True)
    except Exception as e:
        print("The website the recipe is from isn't supported right now.")
        exit(1)

    print("Website scraped successfully.")

    response = notion.createRecipe(scraper.image(), str(scraper.total_time()), scraper.site_name(), scraper.canonical_url(), scraper.title(), scraper.ingredients(), scraper.instructions())

    if(response == HTTPStatus.CREATED or response == HTTPStatus.OK):
        print(scraper.title() + " recipe from " + scraper.site_name() + " successfully added to Notion!")
    else:
        print("Error creating recipe: " + recipeUrl)

startNotriton(recipeUrl)
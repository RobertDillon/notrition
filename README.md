# Notrition
Python script to save recipes directly to a Notion database with the following details:
- Recipe photo is used as the Page cover photo
- Recipe name is used as the page name
- Cook time as a property
- URL as a property
- Website name as a property
- Body of the page contains Ingredients and Steps
- Absolutely *no* five paragraph long **life stories from the author

## Setup
This guide requires that you have a basic understanding of editing and running Python code.

### Notion
First, for this script to work, you need to have a Notion database with the valid fields required by the script. I have a template available for duplication [here](https://www.notion.so/robdillon94/Recipes-93832977de0e41d78938a7178364d141). You can build and add to this, but make sure not to remove any existing columns.

Second, you need to make an Integration in Notion. Notion has a good tutorial on this [here](https://developers.notion.com/docs/getting-started). Remember to save your super secret integration token and keep it somewhere safe! You’ll need this later.

Finally, you’ll need to give your new integration access to the page. You can do this by going to your recipe page and adding your integration from the Share option.

### Python
- Open notion.py
    - Update *token* with the integration token you saved from earlier
    - Update *database_id* with the ID of your recipe database.
        - Guide on how to find this is [here](https://stackoverflow.com/questions/67728038/where-to-find-database-id-for-my-database-in-notion).

## Running
- Run recipe.py with a single parameter: your recipe URL
- Bon appétit!

## Scraping Library
I used [a great recipe scraper](https://github.com/hhursev/recipe-scrapers) as part of this project. Their ReadMe contains a list of websites it supports.



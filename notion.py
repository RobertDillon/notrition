from http import HTTPStatus
import json
from this import s
import requests

token = ''
database_id = ''

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def createRecipe(coverPhotoUrl, cookingTime, websiteName, recipeUrl, recipeTitle, ingredients, instructions):
   print("Building Notion API request")
   payload = {
   "parent": {
      "database_id": database_id
   },
   "cover": {
      "type": "external",
      "external": {
         "url": coverPhotoUrl
      }
   },
   "properties": {
      "Cook Time ⏰ ": {
         "type": "rich_text",
         "rich_text": [
            {
               "type": "text",
               "text": {
                  "content": cookingTime
               }
            }
         ]
      },
      "Website 💻 ": {
         "type": "rich_text",
         "rich_text": [
            {
               "type": "text",
               "text": {
                  "content": websiteName
               }
            }
         ]
      },
      "Link 🔗": {
         "type": "url",
         "url": recipeUrl
      },
      "Recipe Name 🔠": {
         "type": "title",
         "title": [
            {
               "type": "text",
               "text": {
                  "content": recipeTitle
               }
            }
         ]
      }
   },
   "children": [
      {
         "object": "block",
         "type": "column_list",
         "column_list": {
            "children": [
               {
                  "object": "block",
                  "type": "column",
                  "column": {
                     "children": [
                        {
                           "type": "heading_1",
                           "heading_1": {
                              "rich_text": [
                                 {
                                    "type": "text",
                                    "text": {
                                       "content": "🥘 Ingredients"
                                    }
                                 }
                              ],
                              "color": "default"
                           }
                        }
                     ]
                  }
               },
               {
                  "object": "block",
                  "type": "column",
                  "column": {
                     "children": [
                        {
                           "type": "heading_1",
                           "heading_1": {
                              "rich_text": [
                                 {
                                    "type": "text",
                                    "text": {
                                       "content": "🖊 Instructions"
                                    }
                                 }
                              ],
                              "color": "default"
                           }
                        },
                        {
                           "type": "paragraph",
                           "paragraph": {
                              "rich_text": [
                                 {
                                    "type": "text",
                                    "text": {
                                       "content": instructions
                                    }
                                 }
                              ],
                              "color": "default"
                              }
                           }
                        ]
                     }
                  }
               ]
            }
         }
      ]
   }

   for ingredient in ingredients:
      payload["children"][0]["column_list"]["children"][0]["column"]["children"].append(
      {
            "type": "bulleted_list_item",
            "bulleted_list_item": {
               "rich_text": [{
               "type": "text",
               "text": {
                  "content": ingredient
               }
               }]
            }
      },
   )

   print("API payload successfully created")
   print("Beginning API call")

   url = "https://api.notion.com/v1/pages"
   r = requests.post(url, data=json.dumps(payload), headers=headers)

   if(r.status_code == HTTPStatus.CREATED or r.status_code == HTTPStatus.OK):
      print("Notion API returned a successful response")
   elif(r.status_code == HTTPStatus.INTERNAL_SERVER_ERROR):
      print("Notion API returned a 500 error")
      print(r.text)
   else:
      print("Response code of " + str(r.status_code) + "returned from Notion API")
      print(r.text)

   return r.status_code
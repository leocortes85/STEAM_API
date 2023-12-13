from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import api_funct as ft

import importlib
importlib.reload(ft)


app = FastAPI()


@app.get(path="/", 
         response_class=HTMLResponse,
         tags=["Home"])
def home():
    '''
    Home page showing an intro.

    Returns:
    HTMLResponse: HTML response that displays the introduction.
    '''
    return ft.Intro()



@app.get(path = '/PlayTimeGenre',
          description = """ <font color="blue">
                        INSTRUCTIONS<br>
                        1. Click "Try it out".<br>
                        2. Enter the genre in the box below.<br>
                        3. Scroll to "Responses body" to see the release year with the most hours played for the specified genre
                        </font>
                        """,
         tags=["Queries"])

def PlayTimeGenre(genre: str = Query(..., 
                                description="Genre", 
                                example="Adventure")):
        
       return ft.PlayTimeGenre(genre)



@app.get(path = '/UserForGenre',
          description = """ <font color="blue">
                        INSTRUCTIONS<br>
                        1. Click "Try it out".<br>
                        2. Enter the genre in the box below.<br>
                        3. Scroll to "Responses body" to see user with the most hours played and the list of hours played per year for that user
                        </font>
                        """,
         tags=["Queries"])
def UserForGenre(genre: str = Query(..., 
                                description="Genre", 
                                example='Action')):                
    return ft.UserForGenre(genre)



@app.get(path = '/UsersRecommend',
          description = """ <font color="blue">
                        INSTRUCTIONS<br>
                        1. Click "Try it out".<br>
                        2. Enter the year in the box below.<br>
                        3. Scroll to "Responses body" to see a top game and its recommendation count
                        </font>
                        """,
         tags=["Queries"])

def UsersRecommend(year: int = Query(..., 
                                description="The target year for filtering reviews", 
                                example='2014')):                
    return ft.UsersRecommend(year)



@app.get(path = '/UsersNotRecommend',
          description = """ <font color="blue">
                        INSTRUCTIONS<br>
                        1. Click "Try it out".<br>
                        2. Enter the year in the box below.<br>
                        3. Scroll to "Responses body" to see a top game and its not recommendation count
                        </font>
                        """,
         tags=["Queries"])

def UsersNotRecommend(year: int = Query(..., 
                                description="The target year for filtering reviews", 
                                example='2014')):                
    return ft.UsersNotRecommend(year)



@app.get(path = '/sentiment_analysis',
          description = """ <font color="blue">
                        INSTRUCTIONS<br>
                        1. Click "Try it out".<br>
                        2. Enter the year in the box below.<br>
                        3. Scroll to "Responses body" to see the counts of reviews for each sentiment category.
                        </font>
                        """,
         tags=["Queries"])
def sentiment_analysis(year: int = Query(..., 
                                description="The target year for filtering reviews", 
                                example='2014')):
    return ft.sentiment_analysis(year)



@app.get(path = '/similar_user_recs',
          description = """ <font color="blue">
                        INSTRUCTIONS<br>
                        1. Click "Try it out".<br>
                        2. Enter the user in the box below.<br>
                        3. Scroll to "Responses body" to see a list of the most recommended items for the user based on the rating of similar users.
                        </font>
                        """,
         tags=["Queries"])
def similar_user_recs(user: str = Query(..., 
                                description="User id in the Steam Platform", 
                                example='Terenator')):
    return ft.user_similarity(user)



@app.get(path = '/get_recommendations_by_id',
          description = """ <font color="blue">
                        INSTRUCTIONS<br>
                        1. Click "Try it out".<br>
                        2. Enter the item id in the box below.<br>
                        3. Scroll to "Responses body" to see a list of the most recommended similarity items.
                        </font>
                        """,
         tags=["Queries"])
def get_recommendations_by_id(item_id: int = Query(..., 
                                description="Item id in the Steam Platform", 
                                example='219760')):
    return ft.item_similarity(item_id)
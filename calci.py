
import json
import requests
import webbrowser
import wolframalpha
def calci(ui):
# Taking input from user
# App id has to be taken from wolfarm alpha website
    app_id = "******************"
# Instance of wolf ram alpha
# client class
    client = wolframalpha.Client(app_id)
# Stores the response from
# wolf ram alpha
    res = client.query(ui)
# Includes only text from the response
    answer = next(res.results).text
    print(answer)

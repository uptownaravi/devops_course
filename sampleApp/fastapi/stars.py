from fastapi import FastAPI
from pydantic import BaseModel
import requests


class TemplateData(BaseModel):
    data: str
    template: dict


app = FastAPI()


@app.get("/health")
def read_root():
    return {"health": "okay"}


@app.get("/userDetails/{data}")
def getpublicrepo(data: str):
    # Construct the API url with the user name
    url = f"https://api.github.com/users/{data}"
    # Send a GET request to the API and get the response
    response = requests.get(url)
    print(response)
    stars = ""
    repos = ""
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the response as a JSON object
        responsejson = response.json()
        # Get the stars value from the data
        publicrepo = responsejson["public_repos"]
        # Return the stars value
    return f"github user {data} has {publicrepo} publicrepo"


@app.get("/followers/{data}")
def getfollowers(data: str):
    # Construct the API url with the user name
    url = f"https://api.github.com/users/{data}"
    # Send a GET request to the API and get the response
    response = requests.get(url)
    print(response)
    stars = ""
    repos = ""
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the response as a JSON object
        responsejson = response.json()
        # Get the stars value from the data
        followers = responsejson["followers"]
        # Return the stars value
    return f"github user {data} is having {followers} followers"

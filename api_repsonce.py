import requests

# Function to get the response from the api
def getResponce():
    url = "https://animechan.xyz/api/random"
    response = requests.get(url.format()).json()
    response = response['quote'] + " - " + response['character'] + " from " + response['anime']
    return response
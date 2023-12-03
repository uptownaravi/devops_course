# Import requests library
import requests

# Define a function to get the stars of a GitHub user


def get_stars(user):
    # Construct the API url with the user name
    url = f"https://api.github.com/users/{user}"
    # Send a GET request to the API and get the response
    response = requests.get(url)
    print(response)
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the response as a JSON object
        data = response.json()
        # Get the stars value from the data
        stars = data["public_gists"] + data["public_repos"]
        repos = data["public_gists"]
        # Return the stars value
        return stars
    else:
        # Return None if the response is not OK
        return None


# Test the function with some examples
print(get_stars("torvalds"))  # 12
print(get_stars("guido"))  # 10
print(get_stars("uptownaravi"))  # None

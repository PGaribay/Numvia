import requests

url = "https://numbersapi.p.rapidapi.com/90/trivia"

querystring = {"fragment": "true", "notfound": "floor", "json": "true"}

headers = {
	"X-RapidAPI-Key": "68b907eb71msh431ec6ff46df5cdp1170b9jsn5dc4a211d44a",
	"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())


# V2
# add back and next button below results
# back button -1 to existing numsearch
# next button +1 to existing numsearch
# possible to add random value if back/next button clicked without existing numsearch
# V3
# add date on dropdown list
# add a function for the month and day variable to generate the url for date search

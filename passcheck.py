import requests




def request_api_data(query_char):
    url="https://api.pwnedpasswords.com/range/"+ "CBFDA"
    res=requests.get(url)
    if res.status !=200:
        raise RuntimeError("Error fetching: {res.status}, check the api and try again")

def pwned_api_check(password):



    pass
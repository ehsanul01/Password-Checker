import requests

import hashlib
import sys

def request_api_data(query_char):
    url="https://api.pwnedpasswords.com/range/"+ query_char
    res=requests.get(url)
    if res.status_code != 200:

        raise RuntimeError(f"Error fetching: {res.status_code}, check the API and try again")

    return res

def read_res(hash,hash_check):
    has=(line.split(':') for line in hash.text.splitlines())
    for h, count in has:

        if h == hash_check:
            return count
    return 0
        
def pwned_api_check(password):
    s1pass= hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = s1pass[:5],s1pass[5:]
    respons= request_api_data(first5_char)
    return read_res(respons, tail)




def main(args):
    for passo in args:
        count= pwned_api_check(passo)
        if count:
            print(f'{passo} was found {count} time.. you should change your pass word')
        else:
            print(f'{passo} was NOT found. carry on!')
    return "done!"
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
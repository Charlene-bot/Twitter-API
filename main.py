#importing all dependencies
import numpy as np
import requests 
import base64

#variables for accessing twitter API
consumer_key='x8jpWWhmWACKYs7IJXE0LxFmy'
consumer_secret_key='Wi4Je6SUIL7bth96V8Ck6pKQ2sfN9zg7owLEG8a9q6dGVp1gnE'
access_token='833710124950761474-GzKhrFLWvAM64KrIAgTXIHGVMf0JuPH'
access_token_secret='cvPbtjldb2TIG2ywE27GSr1tq147Lb9SPHMVKkS2Noaor'

#Reformat the keys and encode them
key_secret = '{}:{}'.format(consumer_key, consumer_secret_key).encode('ascii')
# Transform from bytes to bytes that can be printed
b64_encoded_key = base64.b64encode(key_secret)
#Transform from bytes back into Unicode
b64_encoded_key = b64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)
auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}
auth_data = {
    'grant_type': 'client_credentials'
}
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
print(auth_resp.status_code)
access_token = auth_resp.json()['access_token']

post_params = {
    'status': 'Hello World',
}
post_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
}
post_url = 'https://api.twitter.com/1.1/statuses/update.json'   
post_resp = requests.post(post_url,headers=post_headers,params=post_params)


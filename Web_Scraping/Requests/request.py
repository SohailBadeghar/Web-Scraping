import requests
# Send get request
r = requests.get('https://www.google.com')
# Check response type
print(type(r))
# Check status code
print(r.status_code)
# Check response content type
print(type(r.text))
# Check response content
print(r.text)
# Check cookies
print(r.cookies)
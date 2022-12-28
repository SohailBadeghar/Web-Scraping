
'''
    GET method is used to retrieve information from the given server using a given URI.
'''

import requests


r = requests.get('http://httpbin.org/get')

# print(help(r))


print(r.status_code)

print(r.headers)


# # print text of request it responce contetnt in unicode.
print(r.text)


'''
If you want to add request parameters, for example, add two request parameters,
where the name value is Sohail and the age value is 24. It can be written as:

'''

data = {
    'name': 'Sohail',
    'age': 24
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)

# you can see here the which parameter we are passing in the url.
print(r.url)


'''
Python’s requests module provides in-built method called post() for making a POST request to a specified URL.

'''
payload = {'username': 'SohailBadeghar', 'Password': 'Password'}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.json())
r_dict = r.json()
print(r_dict['form'])


'''
Basic Authentication using the request.
'''

r = requests.get('http://httpbin.org/basic-auth/SohailBadeghar/pass123',
                 auth=('SohailBadeghar', 'pass123'))
print(r.status_code)
print(r.text)


'''
Response  that we can get perform Sending some  Requestes.
'''

r = requests.get('http://httpbin.org/get')
# Response content type
print(type(r.text), r.text)
# Response content
print(type(r.content), r.content)
# Status code
print(type(r.status_code), r.status_code)
# Response headers
print(type(r.headers), r.headers)
# Cookies
print(type(r.cookies), r.cookies)
# URL
print(type(r.url), r.url)
# Response history
print(type(r.history), r.history)


'''
We can use of session objects by setting a cookie to a URL and then making a request again to check if the cookie is set. 
'''
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

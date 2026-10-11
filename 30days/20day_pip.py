#WebBrowser - opening websites

import webbrowser, requests
# url_lists = [
#     'http://www.python.org',
#     'https://www.linkedin.com/in/asabeneh/',
#     'https://github.com/Asabeneh',
#     'https://twitter.com/Asabeneh',
# ]
# for url in url_lists:
#     webbrowser.open_new_tab(url)

#Requests - URL reading
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
print(response.text)

url2 = 'https://restcountries.eu/rest/v2/all'
response2 = requests.get(url2)
print(response2)
print(response2.status_code) 
#countries = response2.json()
#print(countries[:1])

#Exercise 1
romeo_and_julia = 'http://www.gutenberg.org/files/1112/1112.txt'
response_romeo = requests.get(romeo_and_julia)
print(response_romeo)
#WebBrowser - opening websites

import webbrowser, requests, string
from collections import Counter
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
response_romeo.encoding='utf-8'
text = response_romeo.text
text_lower = text.lower()
clean_text = text_lower.translate(str.maketrans("", "", string.punctuation))
words = clean_text.split()
words_count = Counter(words)
most_10_common = words_count.most_common(10)

print(most_10_common)


#for word in response_romeo
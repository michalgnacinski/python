import pandas as pd

#DataFrame - Tablica
print(pd.DataFrame({'Yes' : [50, 21], 'No' : [131,2]}))

print(pd.DataFrame({'Bob' : ['I liked it.', 'It was awful'], 
                    'Sue' : ['Pretty good', 'Bland']},
                    index=['Product A', 'Product B']))

#Series - lista
print(pd.Series([1,2,3,4,5]))

print(pd.Series(
    [30, 35, 40],
    index=['2015 Sales', '2016 Sales', '2017 Sales'],
    name='Product A'
))

wine_reviews = pd.read_csv("./assets/pandas_data.csv")
print(wine_reviews)
print(wine_reviews.shape)
print(wine_reviews.head)
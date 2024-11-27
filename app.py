"""

#02.1

print("Hello World")

#02.2
import pandas as pd

data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
print(data_frame)

#04

data = pd.Series([23,45,7,34,6,63,36,78,54,34])
print(data)

#04.1
print(pd.date_range("2021-05-01", "2021-05-12"))

#04.2

def divide(n): return n / 2

my_series = pd.Series([2, 4, 6, 8, 10])

print(my_series.apply(divide))

#05 DataFrames

data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]

data_frame = pd.DataFrame(data, columns=["Brand", "Model", "Color"])
print(data_frame)

#05.1 DataFrame Dict
import pandas as pd

data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    }
]



data_frame = pd.DataFrame(data)
new_row = ["Tesla", "Model S", "Red"]
data_frame.loc[len(data_frame)] = new_row
print(data_frame)

#05.2 DA

import pandas as pd

data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
print(data_frame.iloc[133, 6])

#05.3 DataFrame Head

print(data_frame.head(3))

#05.4 DataFrame Tail

import pandas as pd

data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
print(data_frame.tail(3))


# 05.5 Print Columns

import pandas as pd

data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")

print(data_frame[['Name', 'Type 1']][0:10])


# 05.6 Loc Function

print(data_frame.loc[data_frame['Attack'] > 80])

# 05.7 Filter and Count

print(len(data_frame.loc[data_frame['Legendary'] == True]))

import pandas as pd

data_frame = pd.read_csv(".learn/assets/us_baby_names_right.csv")
print(data_frame.head(5))


#06.1 Remove Column

import pandas as pd

data_frame = pd.read_csv(".learn/assets/us_baby_names_right.csv")

data_frame = data_frame.drop(labels = "Unnamed: 0", axis = 1)
print(data_frame.head(5))
"""

#06.2 Value Counts

import pandas as pd

data_frame = pd.read_csv(".learn/assets/us_baby_names_right.csv")

print(data_frame['Gender'].value_counts())

#06.3 Group By

import pandas as pd

data_frame = pd.read_csv(".learn/assets/us_baby_names_right.csv")
names = data_frame.groupby("Name")
print(len(names.sum()))

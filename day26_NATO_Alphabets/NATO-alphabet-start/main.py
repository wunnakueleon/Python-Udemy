# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)


# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}



#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

import pandas

data = pandas.read_csv("day26_NATO_Alphabets/NATO-alphabet-start/nato_phonetic_alphabet.csv")

data_dict = data.to_dict()
alpha_dict = {data_dict['letter'][index]:data_dict['code'][index] for index in range(0, 26)}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input(str("What is the code?")).upper()
user_code = list(user_input)
print(user_code)
for x in user_code:
    if x != " ":
        print(f"{alpha_dict[x]} ", end="")








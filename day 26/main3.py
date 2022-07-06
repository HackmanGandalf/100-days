# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# data = pandas.read_csv("100-days-of-code/day 26/nato_phonetic_alphabet.csv")

# df = pandas.DataFrame(data)

# phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}

# word = input("Enter a word: ").upper()
# letters_in_word = [phonetic_dict[letter] for letter in word]

# print(letters_in_word)

data = pandas.read_csv("100-days-of-code/day 26/nato_phonetic_alphabet.csv")

df = pandas.DataFrame(data)
phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
#print(phonetic_dict)
def generate_phonetic():
    word = input("Enter a word: ").upper()
    #word_list = [letter for letter in word]
    try:
        coded = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only alphabets allowed")
        generate_phonetic()
    else:
        print(coded)
    
generate_phonetic()

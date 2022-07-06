placeholder = "[name]"

with open("Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
 

with open("Input/Letters/starting_letter.txt") as letters:
    letter = letters.read()
    for name in names:
        stripped_names = name.strip()
        new_letter = letter.replace(placeholder, stripped_names)
        with open(f"Output/ReadyToSend/letter_to_{stripped_names}.docx", "w") as completed:
            completed.write(new_letter)
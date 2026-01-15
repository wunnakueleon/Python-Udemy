#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt", mode="r") as list_names, open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    list = list_names.readlines()
    letter = starting_letter.read()

    for each_name in list:
        name = each_name.strip()
        new_letter = letter.replace("[name]", name)
        new_file = f"Output/ReadyToSend/{name}.txt"
        with open(new_file, mode="w") as create_new_letters:
            create_new_letters.write(new_letter)
    #     print(new_letter)

    # print(list)




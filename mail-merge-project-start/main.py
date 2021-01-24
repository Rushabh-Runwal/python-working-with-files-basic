#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Names/invited_names.txt') as n:
    names = n.read()

with open('Input/Letters/starting_letter.docx') as c:
    content = c.read()
print(content)
for each in names.split('\n'):
    l_for_each = content.replace('[name]', each )
    with open(f'Output/ReadyToSend/letter_to_{each}.docx','w') as l:
        l.write(l_for_each)




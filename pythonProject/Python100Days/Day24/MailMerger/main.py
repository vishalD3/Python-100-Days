
PLACEHOLDER = "[name]"
with open("../MailMerger/Input/Names/invited_names.txt") as name_files:
    names = name_files.readlines()
    #print(names)

with open("../MailMerger/Input/Letters/starting_letter.txt") as letter_files:
   letter_content = letter_files.read()
   #print(letter_content)
   for name in names:
       stripped_name = name.strip()
       new_letter_content = letter_content.replace(PLACEHOLDER,stripped_name)
       #print(new_letter_content)
       with open(f"../MailMerger/Output/ReadyToSend/letter_for_{stripped_name}.docx",mode="w") as completed_letter:
           completed_letter.write(new_letter_content)


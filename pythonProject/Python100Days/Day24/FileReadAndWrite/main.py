# file = open("data.txt")
# content = file.read()
# print(content)
# file.close()

# with open("data.txt") as file:
#     content = file.read()
#     print(content)

# with open("data.txt","w") as file:
#     content = file.write("new text has been entered.")


with open("data.txt","a") as file:
    content = file.write("\n text has been apended")
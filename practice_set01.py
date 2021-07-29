letter = '''Dear <|NAME|>,
greeting from coderhub. I am very happy to tell you about your selection\nhave a good day.

Thanks and Regards
Adam chris
Date:<|DATE|>
'''
name = input("Enter your name\n")
date = input("Enter date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)

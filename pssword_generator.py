import random
passlen = int(input("enter the length of password\n"))
s = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*?"
p = "".join(random.sample(s, passlen))
print(p)

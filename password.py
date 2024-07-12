import random



passwd=int(input("Enter the length of the password"))



c="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$5^7*()?4" 

output="".join(random.sample(c,passwd))

print(output)

import random
s = int(input())
cha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz/"''".{}()[]1234567890'
get_pass= random.sample(cha,s)
password = ''
for i in range(len(get_pass)):
  password += get_pass[i]
print(password)   

        

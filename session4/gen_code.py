import random
def gen_password(length):
     """
     this function can generate password of any length
     """

     characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
     password=""
     for _  in range (length):
          password += random.choice(characters)
     return password
gen_password(8)
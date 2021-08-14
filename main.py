from strgen import StringGenerator
import random
import os
password_gen = StringGenerator(r'[a-zA-Z0-9_]{8}').render_set(10000)

def generate_password(passwordFor:str = 'No Name Given'):
    password = random.choice(list(password_gen))
    with open('password.txt', 'a') as f:
        f.write(f'\n{passwordFor}: {password}')
    if os.path.exists('/password.txt'):
        return f'Password: {password}'
    else:
        return f'Password: {password}, also created password.txt which will save all password you create'
    
print(generate_password())
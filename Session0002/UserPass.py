user01 = 'reza'
user02 = 'majid'
pass01 = '1234'
pass02 = '4321'

internaluser = input('please enter your username :')
internalpass = input('please enter your password :')

if (internaluser == user01) and (internalpass == pass01):
    print(f'Welcome {user01}')
elif (internaluser == user02) and (internalpass == pass02):
    print(f'Welcome {user02}')
else:
    print('Username os Password is invalid')

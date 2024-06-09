#!/usr/bin/env python
# coding: utf-8

# In[1]:


def atm_simulation():
    balance=10000
    correct_pin=1234
    print('''
    ***** welcome to ATM Machine Simulator *****
    ''')
    pin=int(input('enter your Pin:'))
    if pin!=correct_pin:
        print('incorrect pin')
        print('thank you')
        return
    while True:
        print('''
        options you can exercise are:
        1) Balance
        2) withdraw
        3) Deposite
        4) Exit
        ''')
        choose=int(input('Select your Transaction from the above options: '))
        if choose==1:
            print(f'Available A/C Balance Is {balance}')
        elif choose==2:
            withdraw=int(input('enter Amount: '))
            if withdraw<=balance:
                balance-=withdraw
                print(f'your Available balance is {balance}')
            else:
                print('Insufficient Balance')
        elif choose==3:
            amount=int(input('Enter amount: '))
            balance+=amount
            print(f'New Balance is {balance}')
        elif choose==4:
            print('Thank you!')
            break
        else:
            print('No Selected Transaction')
    return
atm_simulation()
    
    
    


# In[ ]:





# A simple class based code in python for a Bank employee

data={}
defaultBankPassword = 123456

## This Program can be used by a Bank manager to manually input user data into the server
## provided the user can provide given details
class bank:
    # Add Account details of a user having their name, account balance and a password at the bank
    # and return the account number assigned to the users
    def add():  
        while True:
            name=input('Enter your name: ')
            bal=int(input('Enter your balance :$ '))
            password=int(input('Set your password (req length = 6) : '))
            bank.add.x=[]
            bank.add.x.insert(0,name)
            bank.add.x.insert(1,bal)
            if len(str(password)) == 6:
                bank.add.x.insert(2,password)
            else:
                print("Password length insufficient, Account not added!!")
            bank.add.y=1101
            if bank.add.y in data:
                bank.add.y=bank.add.y+1
            else:bank.add.y==bank.add.y
            data.update({bank.add.y:bank.add.x})
            c=input('Add more accounts?(yes/no) ')
            if c=='yes':
                continue
            else:
                print("==========Account number assigned=========")
                for i in data.keys():
                    print(data.get(i)[0], ":", i)
                print("==========================================")
                break
                
    # The user can change their balance if the password matches
    def change_bal():
        global data
        print("==============Balance=====================")
        enter=int(input('enter your account number: '))
        temp=enter
        j=data.keys()
        if enter in j:
            a=int(input('enter your password: '))
            pasw=data[enter][2]
            if a==pasw:
                b=input('enter your new balance :$ ')
                data[enter][1]=b
                print("Balance changed successfully")
                print("==========================================")
            else: print('wrong password')
        else: 
            print('sorry wrong password') 
            print('try again')
    
    # The user can publish all the relevent details of all accounts
    # bank manager password should pass
    def publishData():
        pas = int(input("Enter the user password: "))
        print("================Data======================")
        if pas == defaultBankPassword:
            f=data.keys()
            details=int(input('Enter your account number: '))
            if details in f:
                s=data.get(details)
                print('Name:',s[0])
                print('Bank id:',details)
                print('Bank balance',s[1])
                print("==========================================")


            else:
                print('try again')
        else:
            print("Password didnt match !!")

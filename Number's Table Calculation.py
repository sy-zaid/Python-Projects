def table():
    x=eval(input('Enter any table you want to calculate:'))
    ran=eval(input('Enter table range: '))
    for i in range(ran+1):
        print(x,'x',i,'=',i*x)

table()
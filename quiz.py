#a=10
#b=34
#c=100
#print(a+b+c)


#age = int(input('how old are you'))

#if age > 17:
    #print('you can buy this game')
#else:
    #print('you are to young')


#height = float(input('how tall are you'))

#if height > 5.5:
    #print('you can ride')
#else:
   # print('sorry, not tall enough sorry')

#a_list = ['apple','cookies', 'etc....',]


def myfunction( name, age):
    if age > 18:
        print('hi ' + name)
        print('are you on your way to college?')
    else:
        print('hi ' + name)
        print('are you still in high school?')

name= input('whats your name')

age = int(input('how old are you'))

myfunction(name, age)
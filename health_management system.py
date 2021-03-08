import time
def time():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime
import datetime
def gettime():
    return datetime.datetime.now()

def input_data():
    print('enter 1 for food and 2 excersise')
    food_excersise = int(input('enter the option'))
    read_write = int(input('press 1 to read and 2 to write'))
    name = int(input('enter 1 for appaji,2 for amma,3 for rohith,4 for rohan'))
    if name==1:
        if food_excersise==1:
            if read_write==1:
                with open('siddaraju-food.txt') as sfr:
                    sfr1=sfr.read()
                    print(sfr1)
            elif read_write==2:
                with open('siddaraju-food.txt','a') as sfw:
                    sfw.write(str(input('enter the food taken'+time())))
                    print('succesfully added')
        elif food_excersise==2:
            if read_write == 1:
                with open('siddaraju-exersise.txt') as ser:
                    ser1 = ser.read()
                    print(ser1)
            elif read_write == 2:
                with open('siddaraju-exersise.txt', 'a') as sew:
                    sew.write( str(input('enter the excersise done'+time())))
                    print('succesfully added')

    if name==2:
        if food_excersise==1:
            if read_write==1:
                with open('chethana-food.txt') as cfr:
                    cfr1=cfr.read()
                    print(cfr1)
            elif read_write==2:
                with open('chethana-food.txt','a') as cfw:
                    cfw.write(str(input('enter the food taken'+time())))
                    print('succesfully added')
        elif food_excersise==2:
            if read_write == 1:
                with open('chethana-exersise.txt') as cer:
                    cer1 = cer.read()
                    print(cer1)
            elif read_write == 2:
                with open('chethana-exersise.txt', 'a') as cew:
                    cew.write( str(input('enter the excersise done'+time())))
                    print('succesfully added')


    if name==3:
        if food_excersise==1:
            if read_write==1:
                with open('rohith-food.txt') as rfr:
                    rfr1=rfr.read()
                    print(rfr1)
            elif read_write==2:
                with open('rohith-food.txt','a') as rfw:
                    rfw.write(str(input('enter the food taken'+time())))
                    print('succesfully added')
        elif food_excersise==2:
            if read_write == 1:
                with open('rohith-exersise.txt') as rer:
                    rer1 = rer.read()
                    print(rer1)
            elif read_write == 2:
                with open('rohith-exersise.txt', 'a') as rew:
                    rew.write( str(input('enter the excersise done'+time())))
                    print('succesfully added')

    if name==4:
        if food_excersise==1:
            if read_write==1:
                with open('rohan-food.txt') as rofr:
                    rofr1=rofr.readlines()
                    print(rofr1)
            elif read_write==2:
                with open('rohan-food.txt','a') as rofw:
                    rofw.write(str(input('enter the food taken'+time())))
                    print('succesfully added')
        elif food_excersise==2:
            if read_write == 1:
                with open('rohan-exersise.txt') as roer:
                    roer1 = roer.read()
                    print(roer1)
            elif read_write == 2:
                with open('rohan-exersise.txt', 'a') as roew:
                    roew.write( str(input('enter the excersise done'+time())))
                    print('succesfully added')


input_data()


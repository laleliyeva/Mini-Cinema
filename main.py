from human import *
from mall import *
from movie import *
from price import *



print('''
Please choose!:

    Worker - 1
    Normal Person - 2
''')

try:
    person_selection=int(input("Your choice: "))
except:
    exit("Invalid Value!")
if person_selection==1:
    print(Worker.who())
elif person_selection==2:
    print(NormalPerson.who())
else:
    exit('Wrong input! ')


ganjlik = Ganjlik('Ganjlik', 5, 9)
iyirmisekkiz=Iyirmi_sekkiz('28 May',4,5)
ganja=Ganja('Ganja',3,4)
deniz=Deniz('Neftciler',5,6)
aygun=Aygun('Sabunçu r., Sakit Qocayev 29',3,7)
print('''
Please choose mall!

Ganjlik Mall -  1
Iyirmi Sekkiz Mall -  2
Ganja Mall   -   3
Deniz Mall  -   4
Aygun Mall  -  5
''')

try:
    mall_selection=int(input('Please choosee the mall! '))
except:
    exit('Invalid value!')

if mall_selection==1:
    print(ganjlik.working_time())
    print(ganjlik.age_check(int(input('Enter your age : '))))
    print(ganjlik.check_vaccination(input('Do you have vaccinate about COVID (Active/Nonactive): ')))
    print(ganjlik.mall_info())
elif mall_selection==2:
    print(iyirmisekkiz.working_time())
    print(iyirmisekkiz.age_check(int(input('Enter your age : '))))
    print(iyirmisekkiz.check_vaccination(input('Do you have vaccinate about COVID (Active/Nonactive): ')))
    print(iyirmisekkiz.mall_info())
elif mall_selection==3:
    print(ganja.working_time())
    print(ganja.age_check(int(input('Enter your age : '))))
    print(ganja.check_vaccination(input('Do you have vaccinate about COVID (Active/Nonactive): ')))
    print(ganja.mall_info())
elif mall_selection==4:
    print(deniz.working_time())
    print(deniz.age_check(int(input('Enter your age : '))))
    print(deniz.check_vaccination(input('Do you have vaccinate about COVID (Active/Nonactive): ')))
    print(deniz.mall_info())
elif mall_selection==5:
    print(aygun.working_time())
    print(Aygun.age_check(int(input('Enter your age : '))))
    print(Aygun.check_vaccination(input('Do you have vaccinate about COVID (Active/Nonactive): ')))
    print(Aygun.mall_info())
else:
    exit("Wrong input!")

seans1=Hours('10:00','12:00')
seans2=Hours('12:00','14:00')
seans3=Hours('14:00','16:00')
seans4=Hours('16:00','18:00')
seans5=Hours('18:00',"20:00")
seans6=Hours('20:00','23:00')


lucy=Lucy('Lucy','Luc Besson','2015','Action/Adventure',90,6.4,[seans1,seans4],5)
artificial_intellegence=Artificial_intellegence('Artificial Intellegence','Steven Spielberg','2001','Sci-Fi',146,7.2,[seans2,seans4],7)
me_before_you=Me_before_you('Me Before You','Thea Sharrock','2016','Drama/Romance',106,7.4,[seans3,seans6],10)
forest_gump=Forest_gump('Forest Gump','Robert Zemeckis','1994','Drama/Romance',142,8.8,[seans2,seans5],12)
green_mile=The_Green_Mile('The Green Mile','Frank Darabont','1999','Crime/Drama',189,8.6,[seans1,seans4],20)
godfather=Godfather('The Godfather','Francis Ford Coppola','1972','Crime/Drama',175,9.2,[seans2,seans6],9)
fight_club=Fight_club('Fight Club','David Fincher','1999','Action/Adventure',139,8.8,[seans4,seans6],17)
inception=Inception('Inception','Christopher Nolan','2010','Action/Adventure',148,8.8,[seans4,seans6],20)
matrix=Matrix(' The Matrix','Lana Wachowski-Lilly Wachowski','1999','Action/Adventure',138,8.7,[seans1,seans6],15)
forsaj_9=Forsaj_9(' Forsaj 9','Justin Lin','2021','Action/Crime',143,5.2,[seans1,seans6],15)



print("""
-----------------
Lucy  -  1  

Artificial Intellegence  -  2

Me Before You  -  3

Forest Gump  -  4

Dear Friend  -  5

Forsaj 9  -  6

The Godfather  -  7

Fight Club  -  8

Inception  -  9

The Matrix  -  10

--------------------

""")


movie_selection = int(input("Choose a film (1-10): "))

if movie_selection==1:
    print(lucy.show_info())
    lucy.year_info()
    lucy.duration_info()
    lucy.rating_info()
    print('Choices: ')

    for i in range(len((lucy.hours))):
        print(str(i+1) +' ) ', str(lucy.hours[i].start_time), ' - ' + str(lucy.hours[i].end_time))

    seance_select=int(input('select:'))

    if seance_select==1:
        print(f'{lucy.name}: {lucy.hours[i-1].start_time}-{lucy.hours[i-1].end_time}')
    elif seance_select==2:
        print(f'{lucy.name}: {lucy.hours[i].start_time}-{lucy.hours[i].end_time}')

    print(f"Your movie's price is {lucy.price} ")

    buy_ticket = input("Do you want to buy a ticket?  (Yes/No): ")
    
    print('------------------------------------------')

    if buy_ticket=='Yes':

        money = int(input("Enter your current money : "))

        print("Your current money :", Money(money).get_money())

        Money(money).set_money(lucy) 

elif movie_selection==2:
    print(artificial_intellegence.show_info())
    artificial_intellegence.year_info()
    artificial_intellegence.duration_info()
    artificial_intellegence.rating_info()
    for i in range(len((artificial_intellegence.hours))):
        print(str(i+1) +' ) ', str(artificial_intellegence.hours[i].start_time), ' - ' + str(artificial_intellegence.hours[i].end_time))
    seance_select=int(input('select:'))
    if seance_select==1:
        print(f'{artificial_intellegence.name}: {artificial_intellegence.hours[i-1].start_time}-{artificial_intellegence.hours[i-1].end_time}')
    elif seance_select==2:
        print(f'{artificial_intellegence.name}: {artificial_intellegence.hours[i].start_time}-{artificial_intellegence.hours[i].end_time}') 
        print('------------------------------------------')
    print(f"Your movie's price is {artificial_intellegence.price} ")
    buy_ticket = input("Do you want to buy a ticket?  (Yes/No): ")
    print('------------------------------------------')
    if buy_ticket=='Yes':
        money = int(input("Enter your current money : "))
        print("Your current money :", Money(money).get_money())
        Money(money).set_money(artificial_intellegence) 
        
elif movie_selection==3:
    print(me_before_you.show_info())
    me_before_you.year_info()
    me_before_you.duration_info()
    me_before_you.rating_info()
    for i in range(len((me_before_you.hours))):
        print(str(i+1) +' ) ', str(me_before_you.hours[i].start_time), ' - ' + str(me_before_you.hours[i].end_time))
    seance_select=int(input('select:'))
    if seance_select==1:
        print(f'{me_before_you.name}: {me_before_you.hours[i-1].start_time}-{me_before_you.hours[i-1].end_time}')
    elif seance_select==2:
        print(f'{me_before_you.name}: {me_before_you.hours[i].start_time}-{me_before_you.hours[i].end_time}')
    print('------------------------------------------')
    print(f"Your movie's price is {me_before_you.price} ")

    buy_ticket = input("Do you want to buy a ticket?  (Yes/No): ")
    print('------------------------------------------')
    if buy_ticket=='Yes':
        money = int(input("Enter your current money : "))
        print("Your current money :", Money(money).get_money())
        Money(money).set_money(me_before_you) 
elif movie_selection==4:
    print(forest_gump.show_info())
    forest_gump.year_info()
    forest_gump.duration_info()
    forest_gump.rating_info()
    for i in range(len((forest_gump.hours))):
        print(str(i+1) +' ) ', str(forest_gump.hours[i].start_time), ' - ' + str(forest_gump.hours[i].end_time))
    seance_select=int(input('select:'))
    if seance_select==1:
        print(f'{forest_gump.name}: {forest_gump.hours[i-1].start_time}-{forest_gump.hours[i-1].end_time}')
    elif seance_select==2:
        print(f'{forest_gump.name}: {forest_gump.hours[i].start_time}-{forest_gump.hours[i].end_time}')
    print('------------------------------------------')
    print(f"Your movie's price is {forest_gump.price} ")

    buy_ticket = input("Do you want to buy a ticket?  (Yes/No): ")
    print('------------------------------------------')
    if buy_ticket=='Yes':
        money = int(input("Enter your current money : "))
        print("Your current money :", Money(money).get_money())
        Money(money).set_money(forest_gump) 
elif movie_selection==5:
    print(green_mile.show_info())
    green_mile.year_info()
    green_mile.duration_info()
    green_mile.rating_info()
    for i in range(len((green_mile.hours))):
        print(str(i+1) +' ) ', str(green_mile.hours[i].start_time), ' - ' + str(green_mile.hours[i].end_time))
    seance_select=int(input('select:'))
    if seance_select==1:
        print(f'{green_mile.name}: {green_mile.hours[i-1].start_time}-{green_mile.hours[i-1].end_time}')
    elif seance_select==2:
        print(f'{green_mile.name}: {green_mile.hours[i].start_time}-{green_mile.hours[i].end_time}')
    print('------------------------------------------')
    print(f"Your movie's price is {green_mile.price} ")

    buy_ticket = input("Do you want to buy a ticket?  (Yes/No): ")
    print('------------------------------------------')
    if buy_ticket=='Yes':
        money = int(input("Enter your current money : "))
        print("Your current money :", Money(money).get_money())
        Money(money).set_money(green_mile) 
elif movie_selection==6:
    print(forsaj_9.show_info())
    forsaj_9.year_info()
    forsaj_9.duration_info()
    forsaj_9.rating_info()
    for i in range(len((forsaj_9.hours))):
        print(str(i+1) +' ) ', str(forsaj_9.hours[i].start_time), ' - ' + str(forsaj_9.hours[i].end_time))
    seance_select=int(input('select:'))
    if seance_select==1:
        print(f'{forsaj_9.name}: {forsaj_9.hours[i-1].start_time}-{forsaj_9.hours[i-1].end_time}')
    elif seance_select==2:
        print(f'{forsaj_9.name}: {forsaj_9.hours[i].start_time}-{forsaj_9.hours[i].end_time}')
    print('------------------------------------------')
    print(f"Your movie's price is {forsaj_9.price} ")

    buy_ticket = input("Do you want to buy a ticket?  (Yes/No): ")
    print('------------------------------------------')
    if buy_ticket=='Yes':
        money = int(input("Enter your current money : "))
        print("Your current money :", Money(money).get_money())
        Money(money).set_money(forsaj_9) 
elif movie_selection==7:
    print(godfather.show_info())
    godfather.year_info()
    godfather.duration_info()
    godfather.rating_info()
    for i in range(len((godfather.hours))):
        print(str(i+1) +' ) ', str(godfather.hours[i].start_time), ' - ' + str(godfather.hours[i].end_time))
    seance_select=int(input('select:'))
    if seance_select==1:
        print(f'{godfather.name}: {godfather.hours[i-1].start_time}-{godfather.hours[i-1].end_time}')
    elif seance_select==2:
        print(f'{godfather.name}: {godfather.hours[i].start_time}-{godfather.hours[i].end_time}')
    print('------------------------------------------')
    print(f"Your movie's price is {godfather.price} ")

    buy_ticket = input("Do you want to buy a ticket?  (Yes/No): ")
    print('------------------------------------------')
    if buy_ticket=='Yes':
        money = int(input("Enter your current money : "))
        print("Your current money :", Money(money).get_money())
        Money(money).set_money(godfather) 
elif movie_selection==8:
    print(fight_club.show_info())
    fight_club.year_info()
    fight_club.duration_info()
    fight_club.rating_info()
    for i in range(len((fight_club.hours))):
        print(str(i+1) +' ) ', str(fight_club.hours[i].start_time), ' - ' + str(fight_club.hours[i].end_time))
    seance_select=int(input('select:'))
    if seance_select==1:
        print(f'{fight_club.name}: {fight_club.hours[i-1].start_time}-{fight_club.hours[i-1].end_time}')
    elif seance_select==2:
        print(f'{fight_club.name}: {fight_club.hours[i].start_time}-{fight_club.hours[i].end_time}')
    print('------------------------------------------')
    print(f"Your movie's price is {fight_club.price} ")
  
    buy_ticket = input("Do you want to buy a ticket?  (Yes/No): ")
    print('------------------------------------------')
    if buy_ticket=='Yes':
        money = int(input("Enter your current money : "))
        print("Your current money :", Money(money).get_money())
        Money(money).set_money(godfather) 
elif movie_selection==9:
    print(inception.show_info())
    inception.year_info()
    inception.duration_info()
    inception.rating_info()
    for i in range(len((inception.hours))):
        print(str(i+1) +' ) ', str(inception.hours[i].start_time), ' - ' + str(inception.hours[i].end_time))
    seance_select=int(input('select:'))
    if seance_select==1:
        print(f'{inception.name}: {inception.hours[i-1].start_time}-{inception.hours[i-1].end_time}')
    elif seance_select==2:
        print(f'{inception.name}: {inception.hours[i].start_time}-{inception.hours[i].end_time}')
    print('------------------------------------------')
    print(f"Your movie's price is {inception.price} ")
    
    buy_ticket = input("Do you want to buy a ticket?  (Yes/No): ")

    print('------------------------------------------')

    if buy_ticket=='Yes':
        money = int(input("Enter your current money : "))
        print("Your current money :", Money(money).get_money())
        Money(money).set_money(inception)
         
elif movie_selection==10:
    print(matrix.show_info())
    matrix.year_info()
    matrix.duration_info()
    matrix.rating_info()
    for i in range(len((matrix.hours))):
        print(str(i+1) +' ) ', str(matrix.hours[i].start_time), ' - ' + str(matrix.hours[i].end_time))
    seance_select=int(input('select:'))
    if seance_select==1:
        print(f'{matrix.name}: {matrix.hours[i-1].start_time}-{matrix.hours[i-1].end_time}')
    elif seance_select==2:
        print(f'{matrix.name}: {matrix.hours[i].start_time}-{matrix.hours[i].end_time}')
    else:
        print('wrong input')
    print('------------------------------------------')
    print(f"Your movie's price is {matrix.price} ")
   
    buy_ticket = input("Do you want to buy a ticket?  (Yes/No): ")
    print('------------------------------------------')
    if buy_ticket=='Yes':
        money = int(input("Enter your current money : "))
        print("Your current money :", Money(money).get_money())
        Money(money).set_money(matrix) 
    
else:
    print('Wrong input! ')

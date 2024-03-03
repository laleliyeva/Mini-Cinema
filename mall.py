# import datetime
from datetime import datetime

current_time = datetime.now().hour
opening_time = 23
closing_time = 12

class Mall:
    def __init__(self, location, floor, hall_count):
        self.location = location
        self.floor = floor
        self.hall_count = hall_count

    def working_time(self):
        if opening_time <= current_time < closing_time:
            return "The mall is open!"
        else:
            return("The mall is closed!")
    
    def age_check(self, a):
        if a>14:
            return 'Your age is suitable'
        else:
            exit("You must be at least 14 years old!")

    def check_vaccination(self,vaccination_status):
        if vaccination_status == "Active":
            return "You are vaccinated."
        else:
            exit('Cant vaccinated')


    
    def mall_info(self):
        return """
        Hello ! Welcome to mall !
        -
        Location:{}
        -
        Floor:{}
        -
        Hall Count:{}
        """.format(self.location,self.floor,self.hall_count)
    

class Ganjlik(Mall):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)


class Iyirmi_sekkiz(Mall):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)


class Ganja(Mall):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)


class Deniz(Mall):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)\


class Aygun(Mall):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)

    
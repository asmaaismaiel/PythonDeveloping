class person(object):
    pass
    name = "Samy"
    money = 1000
    mood = "habby"
    healthRate = 10

    def sleep(self, hours):
        pass
        if hours > 7:
            pass
            return "Happy !"
        elif hours < 7:
            pass
            return "Tired !"
        else:
            pass
            return "Lazy !"

    def eat(self, meals):
        pass
        if meals >= 3:
            pass
            return "100% hth"
        elif meals == 2:
            pass
            return "75% hth"
        else:
            pass
            return "50% hth"

    def buy(self, items):
        pass
        if items >= 1:
            pass
            self.money -= 10
            return self.money
        else:
            pass
            return "Are you monofy ?"


class employee(person):
    pass
    id = 1
    car = "Fiat"
    email = "samy@gmail.com"
    salary = 10000
    distanceToWork = 20

    def work(self, hours):
        pass
        if hours > 8:
            pass
            return "Tierd !"
        elif hours < 8:
            pass
            return "Lazy !"
        else:
            pass
            return "Happy !"

    def drive(self, distance):
        pass
        velocity = self.calcVelocity(distance, 10)
        return velocity

    def refuel(self, gasAmount=100):
        pass
        gasAmount += car.fuelRate
        return gasAmount

    def send(self, parameter_list):
        pass

    def mail(self, parameter_list):
        pass

    def calcVelocity(self, distance, velocity):
        pass
        self.velocity = distance/velocity
        return self.velocity


class office(object):
    pass
    name = "ITI"
    employees = ['Islam', 'Muhhamad', 'Ahmed', 'Ali', 'Hend', 'Mustafa']

    def getAllEmployees(self):
        pass
        return self.employees

    def getEmployee(self, id):
        pass
        if id <= self.employees.__len__():
            pass
            return self.employees[id]
        else:
            pass
            return "No Empoloyee with that ID"

    def hire(self, employee):
        pass
        if employee != None:
            pass
            return "Now he is hired"
        else:
            pass
            return "Now he is not hired"

    def fire(self, parameter_list):
        pass

    def calculateLateness(self, parameter_list):
        pass

    def deduct(self, parameter_list):
        pass

    def reward(self, parameter_list):
        pass


class car(object):
    pass
    name = "Fiat 128"
    fuelRate = 100
    velocity = 200

    def run(self, velocity, distance):
        pass
        self.fuelRate -= 5
        self.velocity = velocity
        if self.fuelRate <= 0:
            pass
            dis = self.stop(distance)
        self.stop(distance)
        return self.fuelRate

    def stop(self, distance):
        pass
        self.velocity = 0
        if distance <= 0:
            pass
            return "You arrived the destination !"
        else:
            pass
            return "Distance remaining {0}".format(distance)


samy = person()
# sleepy = samy.sleep(7)
# hungry = samy.eat(3)
# buyer = samy.buy(-2)
samy = employee()
# employer = samy.work(1)
# driver = samy.drive(1000)
# hasGas = samy.refuel(200)
car = car()
# carcora = car.run(50, 100)
# carcora = car.stop(654)
office = office()
numEmp = office.getEmployee(10)
isHire = office.hire(samy)
print(isHire)
# for index, Emb in enumerate(numEmp):
# pass
# print(Emb)

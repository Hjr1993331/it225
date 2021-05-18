from ticket import Ticket
import datetime

class Identification():
    def __init__(self, password, birthdate):
        self.password = password
        self.birthdate= birthdate
        self.date = datetime.date.today()
        self.time = datetime.time.strftime()

    def getPassword(self):
        return self.password

    def getBirthDate(self):
        return self.birthdate

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time                
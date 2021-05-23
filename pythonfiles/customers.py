from ticket import Ticket
from identification import Identification
import datetime

class Customer():
    def __init__(self, id, number):
        self.customerid = id
        self.customernumber= number
        self.customerdate = datetime.date.today()
        

    def getCustomerId(self):
        return self.customerid

    def getCustomerNumber(self):
        return self.customernumber

    def getCustomerDate(self):
        return self.customerdate
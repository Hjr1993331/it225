import unittest
import datetime
from identification import Identification
from ticket import Ticket
from customers import Customer

class TicketTest(unittest.TestCase):
    def setUp(self):
        self.ticket = Ticket('9998', 'N12')

    def test_ticketstring(self):
        self.assertEqual(str(self.ticket), '9998 ticket')    

    def test_getTicketName(self):
        self.assertEqual(self.ticket.getTicketName(), 'ticket')

    def test_setTicketName(self):
        self.ticket.setTicketName('ticket')
        self.assertEqual(self.ticket.getTicketName(),'ticket')     

    def test_getTicketSeat(self):
        self.assertEqual(self.ticket.getTicketSeat(), 'N12')


class IdentificationTest(unittest.TestCase):
    def setUp(self):
        self.identification = Identification('3176', 'N12')

    def test_GetPassword(self):
        self.assertEqual(self.identification.getPassword(), '3176') 

    def test_GetBirthDate(self):
        self.assertEqual(self.identification.getBirthDate(), 'N12') 

    def test_GetDate(self):
        self.assertEqual(self.identification.getDate(), datetime.date.today())         


class CustomerTest(unittest.TestCase):  
    def setUp(self):
        self.customers = Customer('1111', '919191')   

    def test_GetCustomerId(self):
        self.assertEqual(self.customers.getCustomerId(), '1111') 

    def test_GetCustomerNumber(self):
        self.assertEqual(self.customers.getCustomerNumber(), '919191') 

    def test_GetCustomerDate(self):
        self.assertEqual(self.customers.getCustomerDate(), datetime.date.today())                    
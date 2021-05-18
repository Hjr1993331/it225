class Ticket():
    def __init__(self, ticketid, ticketseat):
        self.ticketid = ticketid
        self.ticketseat = ticketseat
        self.ticketname = 'ticket'

    def getTicketId(self):
        return self.ticketid

    def getTicketSeat(self):        
        return self.ticketseat

    def getTicketName(self):
        return self.ticketname

    def setTucketName(self, ticketname):
        self.ticketname = ticketname

    def __str__(self):
        return self.ticketid + ' ' + self.ticketname        


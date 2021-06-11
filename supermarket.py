import numpy as np
import pandas as pd
import random
from customers import Customer


class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self, name, entry):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 420
        self.last_id = 1
        self.name = name
        self.entry = entry
        # opens at 7:00
        # closes at 21:51
       
    def __repr__(self):
        return f'{self.name} supermarket at {self.get_time()} with {len(self.customers)} customers.'
    

    def get_time(self):
        """current time in HH:MM format,
        """
        hours = self.minutes // 60  # integer division
        minutes = self.minutes % 60 # remainder/ modulo
        return f'{hours:02d}:{minutes:02d}:00'


    def is_open(self):  
        """
        supermarket closes after 15 hours, customer is allowed to come in before 21:51
        total minute from 7:00 to 21:51 is 1311 minutes  
        """ 
        return self.minutes < 1311


    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        for customer in self.customers:
            print(f'{self.get_time()},{customer.customer_id},{customer.state}')


    def next_minute(self):
        """propagates all customers to the next state.
        """
        self.minutes += 1
        # for every customer determine their next state
        for customer in self.customers:
            customer.next_state()
   

    def add_new_customers(self):
        """randomly creates new customers.
        """
        for cust in range(0,self.entry.iloc[420 - self.minutes]):
            state = random.choices(['dairy','drinks','fruit','spices'])
            new_customer = Customer(self.last_id, state[0])
            self.last_id += 1
            self.customers.append(new_customer)
    
    def remove_exitsting_customers(self):
        """removes every customer that is not active any more.
        """
        for customer in self.customers:
            if not customer.is_active():
                self.customers.remove(customer)
            # for each customer in the list
            # if the customer is not active then remove from list

## Writing a Customer class
import random
from Markov_clean import Get_Markov
# Create a class

P = Get_Markov()
# entry = 

class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """

    # Write a constructor

    def __init__(self, customer_id, state, matrix = P, budget=100):
        self.customer_id = customer_id
        self.state = state
        self.budget = budget
        self.matrix = matrix
    
    # Include a __repr__() method
    def __repr__(self):
        return f'<Customer {self.customer_id} in {self.state}>'

    # Add a method
    def next_state(self):
        '''
        Propagates the customer to the next state.
        Returns nothing.
        '''
        self.state = random.choices(['checkout','dairy','drinks','fruit','spices'],
                                   self.matrix.loc[self.state])
        
        self.state = self.state[0]
        #if self.state != 'checkout':
        #    self.state = random.choice(['dairy','drinks','fruit','spices','checkout'])
        return self.state
    
    def is_active(self):
        return self.state != 'checkout'
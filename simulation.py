from supermarket import Supermarket
from Markov import Get_Entry

entry = Get_Entry()
 
lidl = Supermarket(name='LIDL', entry = entry)


while lidl.is_open():

    # increase the time of the supermarket by one minute


    # generate new customers at their initial location
    # repeat from step 1
    lidl.add_new_customers()
    lidl.print_customers()
    lidl.next_minute()
    # remove churned customers from the supermarket
    lidl.remove_exitsting_customers()



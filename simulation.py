from supermarket import Supermarket

lidl = Supermarket(name='LIDL')

while lidl.is_open():

    # increase the time of the supermarket by one minute
    lidl.next_minute()

    # remove churned customers from the supermarket
    lidl.remove_exitsting_customers()

    # generate new customers at their initial location
    lidl.add_new_customers()

    # repeat from step 1
    print(lidl)

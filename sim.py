import sys
from random_variable_generator import dis

def sim(arrival_distribution, departure_distribution, n, simulation_total_time):
    # needed time to attend to all the customers
    stimated_time = sys.maxsize
    
    # time variable
    time = 0
    
    # sistem state variable
    sistem_state = [0 for i in range(0, n)]
    current_customers = [0 for i in range(0, n)]
    event_list = [sys.maxsize for i in range(0, n+1)] # the arrival time is the last element of the array
    
    # counter variables
    arrivalas_num = 0
    departures_num = 0
    
    arrival_time = dict()
    departure_time = dict()
        
    next_arrival = dis[arrival_distribution]()
    event_list[n] = next_arrival # first customer arrival
    
    index_menor_element = sistem_state.index(min(sistem_state))
    while(sistem_state[index_menor_element] < simulation_total_time):
        # index_menor_element = sistem_state.index(min(sistem_state))
        
        # case 1
        if index_menor_element == n:
            time = event_list[n] # update global time
            arrivalas_num = arrivalas_num + 1 # incress the customer that get into the simulation sistem
            current_customers[0] = current_customers[0] + 1 # incress number of cuatomers at server 1
            next_arrival = dis[arrival_distribution]() # generate the next arrival time
            event_list[n] = next_arrival # update event list
            
            if current_customers[0] == 1: # update departure_time at server 1 because is the first customer taht get into de server 1
                next_departure = dis[departure_distribution[0]]() # update the next departure
                event_list[0] = time + next_departure # update event list
                arrival_time(arrivalas_num, time) # update counter variables of the sistem
        
        else:
            # case 2
            time = event_list[index_menor_element] # advance in time
            current_customers[index_menor_element] = current_customers[index_menor_element] - 1 # update current customers at server i = index_menor_element - 1
            
            if current_customers[index_menor_element] == 0: # if there are no more customers at server i then the next departure time at server i is oo
                event_list[index_menor_element] = sys.maxsize
            else:
                next_departure = dis[departure_distribution[index_menor_element]]()
                event_list[index_menor_element] = next_departure
            
            
            if index_menor_element != n - 1: # is not the last server
                current_customers[index_menor_element + 1] = current_customers[index_menor_element + 1] + 1 # update current customers at server i + 1 = index_menor_element
                 
                if current_customers[index_menor_element + 1] == 1:
                    next_departure = dis[departure_distribution[index_menor_element + 1]]()
                    event_list[index_menor_element + 1] = time + next_departure
            else: # is the last server
                departures_num = departures_num + 1
                departure_time(departures_num, time)
                
        index_menor_element = sistem_state.index(min(sistem_state))
        
    if index_menor_element > simulation_total_time:
        if departures_num == arrivalas_num:
            stimated_time = min(0, time - simulation_total_time)
            print('needed time: ', stimated_time)
            print('total customers that get into the sistem: ', arrivalas_num)
            print('total customers that get out the sistem: ', departures_num)
            
        else:
            sistem_state[n] = sys.maxsize
            while departures_num < arrivalas_num:
                   # case 2
                time = event_list[index_menor_element] # advance in time
                current_customers[index_menor_element] = current_customers[index_menor_element] - 1 # update current customers at server i = index_menor_element - 1

                if current_customers[index_menor_element] == 0: # if there are no more customers at server i then the next departure time at server i is oo
                    event_list[index_menor_element] = sys.maxsize
                else:
                    next_departure = dis[departure_distribution[index_menor_element]]()
                    event_list[index_menor_element] = next_departure


                if index_menor_element != n - 1: # is not the last server
                    current_customers[index_menor_element + 1] = current_customers[index_menor_element + 1] + 1 # update current customers at server i + 1 = index_menor_element

                    if current_customers[index_menor_element + 1] == 1:
                        next_departure = dis[departure_distribution[index_menor_element + 1]]()
                        event_list[index_menor_element + 1] = time + next_departure
                else: # is the last server
                    departures_num = departures_num + 1
                    departure_time(departures_num, time)
                
                index_menor_element = sistem_state.index(min(sistem_state))
   
print([1, 2, 3, 4, 1].index(min([1, 2, 3, 4, 1])))
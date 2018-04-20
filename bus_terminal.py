#!/bin/puthon

import random

def simulate_bus_terminal(arrival_time, service_time):
    bus_count = len(arrival_time)
    bus_number = 0
    servise_start_time = [arrival_time[0]]
    service_end_time = [servise_start_time[bus_number] + service_time[bus_number]]
    queue_size = 0
    queue = [0]
    waiting_time =[0]
    Idle_Time = [0]

    while bus_number != bus_count-1:
        if arrival_time[bus_number+1] >= service_end_time[bus_number]:
            if queue_size > 0:
                queue_size -= 1

            servise_start_time.append(arrival_time[bus_number+1])
            waiting_time.append(0)
	    Idle_Time.append(0)
        else:
            queue_size += 1
            servise_start_time.append(service_end_time[bus_number])
            waiting_time.append(service_end_time[bus_number] - arrival_time[bus_number+1])
	    Idle_Time.append(service_end_time[bus_number]-arrival_time[bus_number+1])
        
        queue.append(queue_size)
        service_end_time.append(servise_start_time[bus_number+1] + service_time[bus_number+1])
        bus_number += 1


    print "bus_no.\tarriaval_time\tservice_time\tservice_start\tservice_end\twaiting_time\tqueue_size_after_arrival\tIdle_Time"

    for i in range(bus_count):
        print i+1,"\t",arrival_time[i],"\t\t",service_time[i],"\t\t",servise_start_time[i],"\t\t",service_end_time[i],"\t\t",waiting_time[i],"\t\t",queue[i],"\t\t\t\t",Idle_Time[i]   


if __name__ == "__main__":
    
    max_arrival = 5
    min_arrival = 2
    max_service = 6
    min_service = 0

    bus_count = 12

    inter_arrival_time = [12,4,18,2,23,02,1,2,3,9,9,4]
    arrival_time = map(lambda x:x+sum(inter_arrival_time[:inter_arrival_time.index(x)]), inter_arrival_time)
    service_time = [round(random.uniform(min_service, max_service), 2) for _ in range(bus_count)]

    simulate_bus_terminal(arrival_time, service_time)

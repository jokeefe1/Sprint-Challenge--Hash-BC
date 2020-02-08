#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        source = ticket.source
        destination = ticket.destination
        hash_table_insert(hashtable, source, destination)

    take_off = hash_table_retrieve(hashtable, "NONE") 
    route[0] = take_off 

    for i in range(1, length):
        final_approach = hash_table_retrieve(hashtable, take_off) 
        route[i] = final_approach
        take_off = final_approach

    return route


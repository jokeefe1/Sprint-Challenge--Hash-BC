#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    hash_table = HashTable(16)

    for i in range(length):
        hash_table_insert(hash_table, weights[i], i)
   
    for i in range(length):
        value = hash_table_retrieve(hash_table, limit - weights[i]) 
        if value is not None:
            if i > value: 
                return (i, value)
            else: 
                return (value, i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


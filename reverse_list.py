Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 5/11/2022
# Description: Takes a list and reverses the index order.
#


def reverse_list(vals):
    '''Takes a list and reverses the index order.'''
    for i in range(len(vals) // 2):
        vals[i], vals[len(vals)-i-1] = vals[len(vals)-i-1], vals[i]


#vals = [7, -3, 12, 9]
#reverse_list(vals)
#print(vals) # This should print [9, 12, -3, 7]
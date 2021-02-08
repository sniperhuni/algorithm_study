'''
Given an integer array, print all subarrays with zero-sum.
'''

def insert_to_dict(dict, key, value):

    '''
    if the is seen for the first time, initialize the list
    dict.setdefault(key, value)
    1. key
    2. value: if the key exists, this param has no effect
              if the key does not exists, this value becomes the key's value
    '''
    dict.setdefault(key, []).append(value)

def find_subarray(arr):

    # create empty dict

    dict ={}

    insert_to_dict(dict, 0, -1)

    sum = 0

    for i in range(len(arr)):

        # sum of elements so far
        sum += arr[i]

        '''
        If I found sum in dict, there must exist subarrays with zero sum
        reason)
        number(index i) + [ zero sum array] = number(index j)
        -> subarray with zero sum (j+1, j)
        '''
        if sum in dict:

            # This list includes a subarray with zero sum
            list = dict.get(sum)
            #print(list)

            '''
            for example,
            dict = { 3: [1,2]}

            now, we see 3 again at index 7, subarrays are arr[2:7], arr[3:7]
            '''
            for value in list:
                print('sublist is ({}, {})'.format(value+1, i))

        insert_to_dict(dict, sum, i)

        #print(dict)


array = [3,4,-7,3,1,3,1,-4,-2,-2]

find_subarray(array)

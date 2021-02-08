'''
Given an unsorted integer array, find a pair with a given sum in it
'''

def find_pair_with_given_sum(arr, num):

    result = {}

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):

            sum = arr[i] + arr[j]
            if sum == num:
                result[(i, j)] = sum

    return result


'''
Other solution - O(n) complexity: This is not by me.
I put some comments to write what I understood.
'''

def findpair(arr, num):

    # create an empty dict
    dict ={}

    for i, element in enumerate(arr):

        '''
        check if pair (element, sum-element) exists

        The python dictinary is a hashmap, its worst case is therefore O(n)
        But average time is O(1)
        '''

        if (sum - element) in dict:
            print('pair found at index', dict.get(sum-element), 'and', i)

        # store index of the current element in the dictinary
        dict[element] = i


arr = [8,7,2,5,3,1]
sum =10

print(find_pair_with_given_sum(arr, 10))

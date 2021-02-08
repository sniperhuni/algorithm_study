'''
Implementation of Queue with python

Further Study
1. With linked list
2. Prority queue with Heap
3. With Java & C
'''

class Myqueue:

    def __init__(self):

        # With underscore : Indicate that this is an internal use
        self._items = []

    '''Insert the specified element into the queue.
    If the task is successful, return true, if not it throws an exception
    '''
    def add(self, object):

        try:
            self._items.append(object)
            return True
        except:
            raise('Error occured')

    '''Insert the specified element into the queue.
    If the task is successful, return True, if not it returns False
    '''
    def offer(self, object):
        try:
            self._items.append(object)
            return True
        except:
            return False

    '''
    Returns the head of the queue.
    Throws an exception it the queue empty
    '''
    def element(self):

        try:
            return self._items[0]

        except IndexError:
            print('empty Queue')

    '''
    Returns the head of the que . Returns None if the queue is empty
    '''
    def peek(self):
        try:
            return self._items[0]

        except:
            return None

    '''
    Returns and removes the head of the queue. Throw an exception if the
    queue is empty
    '''
    def remove(self):

        try:
            return self._items.pop(0)
        except IndexError:
            print('Empty Queue')

    '''
    Returns and removes the head of the queue. Returns None if the
    queue is empty
    My opinion)
    Because this function has a return value, we can use this to check if our
    queue is empty.
    '''
    def poll(self):

        try:
            return self._items.pop(0)

        except:
            return None

    def __repr__(self):

        return f'Queue({self._items})'


queue = Myqueue()

queue.element()
print(queue.peek())

queue.offer(7)
queue.offer('friends')
queue.offer([1,2,3,4,5])

print(queue.poll())
print(queue.poll())
print(queue.poll())
print(queue.poll())

print(queue)

'''
Implementation Stack with pythonmy
'''

class Mystack:

    def __init__(self):

        self.items = []

    def push(self, object):

        self.items.append(object)

    def pop(self):

        try:
            return self.items.pop()
        except IndexError:
            print('POP from Empty Stack')

    def __len__(self):

        return len(self.items)

    '''
    Returns the object at the top of the stack without removing it
    '''
    def peek(self):

        return self.items[0]

    ''' To see how my stack looks like'''
    def __repr__(self):

        return f'Mystack({self.items})'


stack = Mystack()

stack.push('key')
stack.push(55)
stack.push(77)
stack.push('year')

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.peek())

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(len(stack))

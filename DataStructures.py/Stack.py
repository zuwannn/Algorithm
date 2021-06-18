# stack 

#create stack
def create_stack():
    stack = []
    return stack

#create empty stack
def check_empty(stack):
    return len(stack) == 0

# add item into stack
def push(stack, item):
    stack.append(item)
    print("push item: " + item)

# remove element from stack
def pop(stack):
    if check_empty(stack):
        return "stack is empty"
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("poped item: " + pop(stack))
print("poped item: " + pop(stack))
print("poped item: " + pop(stack))
print("stack after popping an element: " + str(stack))
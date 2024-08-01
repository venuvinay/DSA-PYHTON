class stack:
    def __init__(self):
        self.stack=[]
def push(stack_obj,data):
    stack_obj.stack.append(data)
    return stack_obj
def pop(stack_obj):
    stack_obj.stack.pop()
    return stack_obj
def peek(stack_obj):
    return stack_obj.stack[-1]
def isempty(stack_obj):
    if len(stack_obj.stack)==0:
        return "empty stack"
    return "not an empty stack"
o=stack()
l=[1,2,3,4,5,6,7]
for i in l:
    o=push(o,i)
print(o.stack)
o=pop(o)
print(o.stack)
v=peek(o)
print("peek element",v)
o=pop(o)
print(o.stack)
o=pop(o)
print(o.stack)
o=pop(o)
print(o.stack)
o=pop(o)
print(o.stack)
o=pop(o)
print(o.stack)
o=pop(o)
print(o.stack)
print(isempty(o))
o=push(o,700)
print(o.stack)
print(isempty(o))

    

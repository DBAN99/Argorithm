
# def recursive(data):
#     if data <0:
#         print("ended")
#     else:
#         print(data)
#         recursive(data-1)
#         print("rrr",data)
# print(recursive(4))



# data_stack = []
#
# data_stack.append(123)
# data_stack.append(4321)
#
# print(data_stack)
# data_stack.pop()
# print(data_stack)

stack = []
def push(da):
    stack.append(da)

def pop():
    data = stack[-1]
    del stack[-1]
    return data

for i in range(10):
    push(i)

print(stack)
print(pop())
print(stack)
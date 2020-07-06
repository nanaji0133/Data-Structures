# revering a string using stack method

# class Stack:
#     def __init__(self):
#         self.slist = []

#     def push(self,char):
#         return self.slist.append(char)

#     def pop(self):
#         return self.slist.pop()

#     def is_empty(self):
#         return self.slist == []

#     def peek(self):
#         if not self.is_empty():
#             return self.slist[-1]

from Stack import Stack 
# note: as we have already created stack we can import 
def reverse(s,string):
    rev_stng = ""
    for index in range(len(string)):
        char = string[index]
        s.push(char)
    while not s.is_empty():
        top = s.pop()
        rev_stng += top
    return rev_stng

s = Stack()
print(reverse(s,"nanaji"))


    # def reverse(self,string):
    #     index = 0
        
    #     while True:
    #         rev_stng = ""
    #         if index < len(string):
    #             char = string[index]
    #             Stack().push(char)
    #         else:
    #             top = Stack().pop()
    #             rev_stng += top
    #         index += 1
    #     return rev_stng


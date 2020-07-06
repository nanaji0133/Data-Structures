from Stack import Stack
def is_match(a,b):
    if a == "[" and b == "]":
        return True
    elif a == "{" and b == "}":
        return True
    elif a == "(" and b == ")":
        return True
    else:
        return False
''' this is also a correct code'''
# def prntsisbal(prnt):
#     s = Stack()
#     index = 0
#     is_balanced = True
#     while index < len(prnt) and is_balanced:
#         prnti = prnt[index]
#         if prnti in "{[(":
#             s.push(prnti)
#         else:
#             if prnti is s.is_empty():
#                 is_balanced = False
#             else:
#                 end = s.pop()
#                 if not is_match(prnti,end):
#                     is_balanced = False
#         index += 1
def prntsisbal(prnt):
    s = Stack()    
    for index in range(len(prnt)):
        prnti = prnt[index]
        if prnti in "{[(":
            s.push(prnti)
        else:
            if prnti is s.is_empty():
                return False
            else:
                end = s.pop()
                if not is_match(prnti,end):
                    return False
    if s.is_empty:
        return True
    else:
        return False
print(prntsisbal("[[[[{)]]]]"))

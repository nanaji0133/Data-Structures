'''how to return string n times from a python function, such that it is printed n times with space in between'''
# def fn(str,n):
#     global result
#     if n == 0:
#         return result.strip()
#     else:
#         result = result+" " + str
#         return fn(str,n-1)

# result = ""
# str = "I am a good boy"
# print(fn(str,5))

'''fibanoci series'''
# def fib(n):
#     if int(n) >= 3:
#         return fib(n-1) + fib(n-2)
#     else:
#         return 1
# print(fib(11))

# n = input("enter a string: ")
# print(len(input("enter a string: ")))

'''reverse a function'''
# def revfn(a): # a is array
#     for x in reversed(arr):
#         print(x, end=" ")

# def reverseList(A): 
#     start = 0
#     end = int(len(A)) - 1
#     while start < end: 
#         A[start], A[end] = A[end], A[start] 
#         start += 1
#         end -= 1
  
# # Driver function to test above function 
# A = [1, 2, 3, 4, 5, 6] 
# print(A) 
# reverseList(A) 
# print("Reversed list is") 
# print(A) 
# # This p
# from collections import Counter
# l = [1,2,3,4,1,2,6,7,3,8,1,2,3]
# d = Counter(l)
# max_d = max(x for x in d.values())
# count_maxd = list(x for x in d.values()).count(max_d)
# print(count_maxd)

# mat = [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,3],
#  [1,0,0,0]]

# s = ((sum(mat[i]),i) for i in range(len(mat)))
# print(s)

# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")
# x = zip(a, b)

# #use the tuple() function to display a readable version of the result
# print(list(x))

# l = []
# print(len(l))

# class Solution(object):
#     def calPoints(self, ops):
#         """
#         :type ops: List[str]
#         :rtype: int
#         """
#         s = []
#         for i in ops:

#             if i == "C":
#                 s.pop()
#             elif i == "D":
#                 s.append(2*s[-1])
#             elif i == "+":
#                 s.append(s[-1]+s[-2])
#             else:
#                 s.append(int(i))       
#         return sum(s)
# A = [1,2,3,4]
# l = [A[i:i+j] for i in range(0,len(A)) for j in range(1,len(A) - i + 1)]
# p = []
# print(l)
# for s in l:
#     if sum(s) >= 1222:
#         p.append(len(s))
# if p:
#     print(min(p))
# else:
#     print("no")
''' anagram '''
# s = "bab"
# t = "aba"
# while i < len(s):
#     if 
# print(t) '''
'''
for i in range(len(s)):
    if s[i] in t:
        t.remove(s[i])
print(len(t)) '''
# from collections import Counter
# s = "abzcabccref"
# l = len(s)
# print(sorted(s))
# print(sum((Counter(s[:l//2]) - Counter(s[l//2:])).values()))
'''
str = 'abc' + None
print(len(str))
'''
'''
def subseq(a):
    a_c = 0
    b_c = 0
    c_c = 0
    for i in a.strip():
        if i == "a":
            a_c = 1 + 2*(a_c)
        if i == "b":
            b_c = a_c + 2*(b_c)
        if i == "c":
            c_c = b_c + 2*(c_c)
    return c_c

print(subseq("abcabc")) '''
print([10**9 for i in range(4)])

        
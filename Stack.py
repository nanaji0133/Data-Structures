class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return self.items == []

    def top(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

# s = Stack()
# s.push("1")
# s.push("2")
# s.push("3")
# s.pop()
# s.pop()
# print(s.get_stack())
# print(s.is_empty())
# print(s.top())

# https://www.youtube.com/redirect?q=https%3A%2F%2Fgithub.com%2Fvprusso%2Fyoutube_tutorials%2Fblob%2Fmaster%2Fdata_structures%2Fstack%2Fstack.py&v=lVFnq4zbs-g&event=video_description&redir_token=I6e91AnXaVxLIZE5TpINRt2_ps98MTU3OTk4ODUyOEAxNTc5OTAyMTI4

def logger(msg):
    def log_msg():
        print(msg)
    return log_msg

l = logger("hi")
l()








# class Employee:
#     def __init__(self, name):
#         self.name = name

# class Developer(Employee):
#     def __init__(self, name, programming):
#         super().__init__(name)
#         self.programming = programming

# dev_1 = Developer("nanaji","python")
# emp = Employee("nanaji")
# print(dev_1.__dict__)
# print(emp)
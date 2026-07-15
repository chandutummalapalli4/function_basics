# greet(name) → Print Hello <name>
# student(name, age) → Print student details
# square(num) → Print the square of a number
# table(num) → Print the multiplication table of a number
# voting(name, age) → Print whether the person is eligible to vote

##---greet(name)---→ Print Hello <name>-- ##
def greet(name):
    print("Hello",name)
greet("Chandu")

##---- student(name, age)---→ Print student details--- ##
def student(name,age):
    print("Name:",name,"Age:",age)
student("Chandu",21)
student("Chatgpt",123)    

##---square(num)---→ Print the square of a number ---##
def square(num):
    print(num**2)
square(5)
square(10)

##---table(num)---→ Print the multiplication table of a number ---##
def table(num):
    for i in range(1,11):
        print(f"{num} X {i} = {i*num}")
table(11)
table(22)
table(10)   

##---voting(name, age) → Print whether the person is eligible to vote ---##
def voting(name,age):
    if age>=18:
        print(name,"Right vote")
    else:
        print(name,"Not eligible")
voting("Chandu",21)
voting("Rahul",13)        
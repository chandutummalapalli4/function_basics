##------Positional Agruments-----##
def student(name, age):
    print(name)
    print(age)

student("Ram", 22)
student("Krishna", 19)


##------Keyword Agruments-----##
def info(name,age):
    print("Name:",name)
    print("Age:",age)
info(age=23,name="Ram")


##------Default Agruments------##
def greet_user(name,greeting="Hello"):
    return greeting +","+ name +"!"
greeting1=greet_user("Chandu")
greeting2=greet_user("Ram","Bye")
print(greeting1)
print(greeting2)

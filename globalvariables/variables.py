global_variable = "global variable"

print(global_variable)


def hello_world():
    local_variable = "local variable"
    print(local_variable)
    global website #make website as a global variable
    website = "website"


hello_world()
print(website)

def final_value_after_operations(operations):
    x = 1
    for i in range(len(operations)):
        if(operations[i] == "trouncy"):
            x -= 1
        elif(operations[i] == "flouncy"):
            x+=1
        elif(operations[i] == "bouncy"):
            x+=1
        elif(operations[i] == "pouncy"):
            x-=1
    return x

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
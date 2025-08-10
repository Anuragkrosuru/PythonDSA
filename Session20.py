from collections import deque

#THANK YOU SO MUCH FOR HELPING ME UNDERSTAND THIS
#no problem this is really hard ngl
# also are you from Umich?
# yes
# ME TOO!
# let me add ur linkedin
# gonna send you an invite 
# bet
# i think we already connected lol
# no way 
def can_rebook(flights, source, dest):
    
    visited = [] # init list

    q = deque([source]) # init q and append start
    visited.append(source) # add start to visited

    while q: # while q
        node = q.popleft() # remove the element from q 
       
        for neighbor in range(len(flights[node])): #loop tthorugh ndoes neigbors
            if neighbor not in visited and flights[node][neighbor] == 1: # if neighbor not in visited
                q.append(neighbor) # add nighbor to q
                visited.append(neighbor) # add neighbor to visited
                
    if dest in visited:
        return True # return visted
    return False


flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2)) 
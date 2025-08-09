"""
JFK ----- LAX
|
|
DFW ----- ATL
"""
flights = {
    "LAX": ["JFK"],
    "JFK": ["LAX", "DFW"],
    "DFW": ["JFK", "ATL"], 
    "ATL": ["DFW"]        
}
# No starter code is provided for this problem
# Add your code here

print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])

def bidirectional_flights(flights):
    # node_dictionary = {}
    # for i, value in enumerate(flights):
    #     if i not in node_dictionary:
    #         node_dictionary[i] = value
    
    
    # for key in node_dictionary:
    #     # 0 1,2
    #     # if the value of the node is present in the dictionary
    #     if node_dictionary[key] in node_dictionary:

    #     # i -> values
    #     # values(i) -> i(values)r

    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True


flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))


def get_direct_flights(flights, source):
    from collections import defaultdict
    direct_flights = defaultdict(list)


    for i in range(len(flights)):
        for j in range(len(flights[0])):
            if flights[i][j] == 1:
                direct_flights[i].append(j)

    return direct_flights[source]



flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))


def get_adj_dict(flights):
    adj_dict = {}
    # iterature though each elemnt
    for a, b in flights:
        if a not in adj_dict:
            adj_dict[a] = [b]
        else:
            adj_dict[a].append(b)
    # a a key and b a value
        if b not in adj_dict:
            adj_dict[b] = [a]
        else:
            adj_dict[b].append(a)
    # make b a key and a a vluae
    return adj_dict

flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))
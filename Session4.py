def find_needle(haystack, needle):
    # Write your code here
    if len(haystack) < len(needle):
        return -1
    for i in range(len(haystack) - len(needle) + 1):  
        j = 0
        if haystack[i] == needle[0]:
            while j < len(needle):
                if haystack[i + j] != needle[j]:  
                    break
                j += 1
            if j == len(needle):
                return i  
    return -1


def test_find_needle():
    # Example 1
    assert find_needle("sadbutsad", "sad") == 0, "Test case 1 failed"
    
    # Example 2
    assert find_needle("leetcode", "leeto") == -1, "Test case 2 failed"
    
    # Example 3
    assert find_needle("mad", "madden") == -1, "Test case 3 failed"
    
    print("All test cases passed!")

# Run the test function
#test_find_needle()



def most_endangered(species_list):
    # store the lowest population
    endangered = species_list[0]
    #iterate throiugh the dicitonary
    for species in species_list:
        # update lowest pop
        if species["population"] < endangered["population"]:
            endangered = species
    return endangered["name"]



species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))

def count_endangered_species(endangered_species, observed_species):
    endangered = set(endangered_species)
    observed = observed_species
    count = 0

    for species in observed:
        if species in endangered:
            count += 1
    
    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  



def navigate_research_station(station_layout, observations):
    station = {}
    count = 0
    for i, char in enumerate(station_layout):
        station[char] = i
    start = 0
    for char2 in observations:
        count += abs(station[char2] - start)
        start = station[char2]
    return count



station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))



def prioritize_observations(observed_species, priority_species):
    priority = {}
    for i, species in enumerate(priority_species):
        priority[species] = i
    
    def sort_key(species):
        if species in priority:
            return (0, priority[species])
        else:
            return (1, species)
        
    return sorted(observed_species, key = sort_key)




observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

#print(prioritize_observations(observed_species1, priority_species1))
#print(prioritize_observations(observed_species2, priority_species2)) 



def distinct_averages(species_populations):
    s = []
    if len(species_populations) == 2:
        return 1
    if len(species_populations) < 2:
        return 0
    
    while len(species_populations) != 0:
        a = min(species_populations)
        b = max(species_populations)
        s.append((a+b)/2)
        species_populations.remove(a)
        species_populations.remove(b)
        
    l = set(s)
    return len(l)



species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 

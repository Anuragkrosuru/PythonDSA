def lineup(artists, set_times):
    artists_dict = {}
    
    for i in range(len(artists)):
        artists_dict[artists[i]] = set_times[i]

    return artists_dict


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

def get_artist_info(artist, festival_schedule):
    if festival_schedule.get(artist) != None:
        return festival_schedule[artist]

    


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  

def total_sales(ticket_sales):
    count = 0
    for ticket in ticket_sales:
        count += ticket_sales[ticket] 
    return count


ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

#print(total_sales(ticket_sales))

def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = {}
    for artist in venue1_schedule:
        if venue1_schedule[artist] == venue2_schedule.get(artist):
            conflicts[artist] = venue1_schedule[artist]

    return conflicts


venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

# print(identify_conflicts(venue1_schedule, venue2_schedule))

def best_set(votes):
    vote_count = {}
    for vote in votes:
        if votes[vote] in vote_count:
            vote_count[votes[vote]] += 1
        else:
            vote_count[votes[vote]] = 1
    return max(vote_count, key = vote_count.get)



votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))

def max_audience_performances(audiences):
    count = 0
    x = max(audiences)
    for i in range(len(audiences)):
         if x == audiences[i]:
             count += 1
    return x * count
   
        

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
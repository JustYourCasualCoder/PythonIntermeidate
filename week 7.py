building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601,
"Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}



print(building_heights.get("Shanghai Tower"))

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket",
412123: "Necklace", 298787: "Pasta Maker"}

print(raffle.pop(320291, "No Prize"))

print(raffle.pop(100000, "No Prize"))
print(raffle.pop(872921, "No Prize"))


test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84],
"Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

for student in test_scores.keys():
    print(student)



    

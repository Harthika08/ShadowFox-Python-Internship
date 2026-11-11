# Initial list
justice_league = [
    "Superman", "Batman", "Wonder Woman",
    "Flash", "Aquaman", "Green Lantern"
]
# 1. Count members
print("Total members:", len(justice_league))
print()

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Updated members:", justice_league)
print()

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After moving Wonder Woman:", justice_league)
print()

# 4. Place Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
position = justice_league.index("Aquaman")
justice_league.insert(position + 1, "Green Lantern")
print("After repositioning Green Lantern:", justice_league) 
print()

# 5. Replace the list
justice_league = [
    "Cyborg", "Shazam", "Hawkgirl",
    "Martian Manhunter", "Green Arrow"
]

# 6. Sort alphabetically
justice_league.sort()

# Display new leader
print("New Justice League:", justice_league)
print()
print("New Leader:", justice_league[0])
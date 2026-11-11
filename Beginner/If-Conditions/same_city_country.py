Australia = ["sydney","melbourne","brisbane","perth"]
UAE = ["dubai","abu dhabi","sharjah","ajman"]
India = ["mumbai","banglore","chennai","delhi"]
city1 = input("Enter a city name:").strip().lower()
city2 = input("Enter a city name:").strip().lower()
if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")
elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")
elif city1 in India and city2 in India:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")

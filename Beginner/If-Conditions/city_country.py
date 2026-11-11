Australia = ["sydney","melbourne","brisbane","perth"]
UAE = ["dubai","abu dhabi","sharjah","ajman"]
India = ["mumbai","banglore","chennai","delhi"]
city = input("Enter a city name:").strip().lower()
if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print("Enter valid city name")
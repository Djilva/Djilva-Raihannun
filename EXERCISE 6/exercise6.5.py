rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China"
}

print("River information:")

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nThe rivers included in the dictionary are:")

for river in rivers.keys():
    print(river)

print("\nThe countries included in the dictionary are:")

for country in rivers.values():
    print(country)
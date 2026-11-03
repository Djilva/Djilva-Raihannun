cities = {
    "Surakarta": {
        "country": "Indonesia",
        "population": "Around 580,000 people",
        "fact": "Known for its traditional batik."
    },

    "Bandung": {
        "country": "Indonesia",
        "population": "Around 2.5 million people",
        "fact": "Famous for its cool weather and fashion."
    },

    "Yogyakarta": {
        "country": "Indonesia",
        "population": "Around 375,000 people",
        "fact": "Known for its cultural heritage."
    }
}

for city, information in cities.items():
    print(f"City: {city}")
    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")
    print()
def city_country(city, country, population=0):
    """Return a city, country, and optional population."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"
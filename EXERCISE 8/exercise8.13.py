def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last

    return user_info


my_profile = build_profile(
    "Djilva",
    "Raihannun",
    age=18,
    city="Karanganyar",
    hobby="Reading"
)

print(my_profile)
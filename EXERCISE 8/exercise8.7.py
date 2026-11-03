def make_album(artist, title, num_songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if num_songs is not None:
        album["num_songs"] = num_songs

    return album


album1 = make_album("NewJeans", "Get Up")
album2 = make_album("Blur", "Parklife")
album3 = make_album("Olivia Rodrigo", "Sour", 16)

print(album1)
print(album2)
print(album3)
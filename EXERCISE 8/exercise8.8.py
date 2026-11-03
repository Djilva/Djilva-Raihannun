def make_album(artist, title):
    album = {
        "artist": artist,
        "title": title
    }
    return album


while True:
    print("\nEnter album information:")
    print("(Enter 'quit' to stop)")

    artist = input("Artist name: ")

    if artist == "quit":
        break

    title = input("Album title: ")

    if title == "quit":
        break

    album = make_album(artist, title)

    print(album)
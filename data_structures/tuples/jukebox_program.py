# Import from a Python file
from data_structures.tuples.jukebox import albums

choice = "-"
SONGS_LIST = 3
SONG_TITLE = 1

while True:
    print("PLEASE CHOOSE YOUR ALBUM (Invalid number quits program): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}:\t{} by {} ({})"
              .format(index + 1, title, artist, year))

    choice = int(input())

    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST]
    else:
        break

    print("PLEASE CHOOSE YOUR SONG: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}\t{}".format(track_number, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE]
        print("PLAYING '{}'".format(title))
    else:
        continue

    print("-" * 25)

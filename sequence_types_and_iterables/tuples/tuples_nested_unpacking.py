albums = [("Welcome to my nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))

for name, artist, year in albums:
    print("Album: {0}\nArtist: {1}\nYear: {2}"
          .format(name, artist, year))
    print("-" * 10)

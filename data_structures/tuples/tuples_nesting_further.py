albums = [("Welcome To My Nightmare", "Alice Cooper", 1975,
           (
               (1, "Welcome To My Nightmare"),
               (2, "Devil's Food"),
               (3, "The Black Widow"),
               (4, "Some Folks"),
               (5, "Only Women"),
               (6, "Department of Youth"),
               (7, "Cold Ethyl"),
               (8, "Years Ago"),
               (9, "Steven"),
               (10, "The Awakening"),
               (11, "Escape"),
           )
           ),
          ("Carter III", "Lil' Wayne", 2008,
           (
               (1, "3 Peat"),
               (2, "Mr. Carter"),
               (3, "A Milli"),
               (4, "Got Money"),
               (5, "Comfortable"),
               (6, "Dr. Carter"),
               (7, "Phone Home"),
               (8, "Tie My Hands"),
               (9, "Mrs. Officer"),
               (10, "Let The Beat Build"),
               (11, "Shoot Me Down"),
               (12, "Lollipop"),
               (13, "La La"),
               (14, "Pussy Monster"),
               (15, "You Ain't Got Nothin' On Me"),
               (16, "DontGetIt"),
           )
           ),
          ("Views", "Drake", 2018,
           (
               (1, "Keep the Family Close"),
               (2, "9"),
               (3, "U With Me?"),
               (4, "Feel No Ways"),
               (5, "Hype"),
               (6, "Weston Road Flows"),
               (7, "Redemption"),
               (8, "With You"),
               (9, "Faithful"),
               (10, "Still Here"),
               (11, "Controlla"),
               (12, "Grammys"),
               (13, "Childs Play"),
               (14, "Pop Style"),
               (15, "Too Good"),
               (16, "Summers Over Interlude"),
               (17, "Fire & Desire"),
               (18, "Views"),
           )
           ),
          ]

# Indexing into the nested tuples to get the name of the song "Lollipop"
lollipop = albums[1][3][11][1]
print(lollipop)

for title, artist, year, songs in albums:
    print(f"TITLE: {title}\nARTIST: {artist}\nYEAR: {year}\nSONGS:")
    for number, name in songs:
        print(f"\t{number}\t{name}")
    print("-" * 10)

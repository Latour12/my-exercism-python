def recite(start_verse, end_verse):
    lyrics = []
    days = ["zeroth", "first", "second",
            "third", "fourth", "fifth",
            "sixth", "seventh", "eighth",
            "ninth", "tenth",
            "eleventh", "twelfth"]
    gifts = ["null","a Partridge in a Pear Tree",
             "two Turtle Doves", "three French Hens",
             "four Calling Birds", "five Gold Rings",
             "six Geese-a-Laying", "seven Swans-a-Swimming",
             "eight Maids-a-Milking", "nine Ladies Dancing",
             "ten Lords-a-Leaping", "eleven Pipers Piping",
             "twelve Drummers Drumming"]
    for day in range(start_verse, end_verse+1):
        verse = f"On the {days[day]} day of Christmas my true love gave to me: "
        for gift in range(day, 0, -1):
            verse = verse + ("and " if (gift == 1 and day > 1) else "")
            verse = verse + gifts[gift]
            verse = verse + ("." if gift == 1 else ", ")

        lyrics.append(verse)
    return lyrics
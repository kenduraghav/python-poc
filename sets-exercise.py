sports_day = {"Alice", "Bob", "Charlie", "Diana"}
science_fair = {"Bob", "Eve", "Frank", "Charlie"}
art_competition = {"George", "Alice", "Frank", "Helen"}


print (f"Students participated in all events: {sports_day.intersection(science_fair).intersection(art_competition)  }")

only_one = (
    (sports_day - science_fair - art_competition) |
    (science_fair - sports_day - art_competition) |
    (art_competition - sports_day - science_fair)
)
print(f"Students participated in only one event: {only_one}")

print(f"Students participated only in sports day event:  {sports_day - (science_fair & art_competition) }")

combined_students = sports_day.union(science_fair, art_competition)

print(f"Combined Students in all Events : {combined_students}")

if "Zara" in combined_students:
    print("Zara is in the list of students who participated in at least one event.")
else:
    print("Zara is not in the list of students who participated in at least one event.")




import csv
file = open ("Books.csv", "w")
newrecord = "To Kill A Mockingbird, Harper Lee, 1960\n"
file.write (str (newrecord))
newrecord = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(newrecord))
newrecord = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write (str (newrecord))
newrecord = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write (str (newrecord))
newrecord = "Pride and Prejudice, Jane Austen, 1813\n"
file.write (str (newrecord))
file.close()
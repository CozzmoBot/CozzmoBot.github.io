from datetime import date

today = date.today()


f = open("E.pages", "a")
f.write("Visited on",today)
f.close()

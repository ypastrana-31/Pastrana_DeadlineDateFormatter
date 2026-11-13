from datetime import date

event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = date(year,month, day)

print("\nFormatted Output: ")
print("Event:", event_title.strip().upper())
print("Date:", event_date.strftime("%B %d, %Y"))
print("Year:", event_date.year)
print("Month:", event_date.strftime("%B"))
print("Day:", event_date.day)
print("Weekday:", event_date.strftime("%A"))

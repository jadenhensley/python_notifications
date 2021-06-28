from win10toast import ToastNotifier
from random import randint
from random import choice
import pathlib
import time
import csv
from PIL import Image

with open('Quotes.csv', 'r') as csv_quotes:
    csv_reader = csv.DictReader(csv_quotes, delimiter=";")
    #for row in csv_reader:
    #    print(row['QUOTE'], "  quote from ", row['AUTHOR'])
    quotes = []
    author = []
    for row in csv_reader:
        quotes.append(row['QUOTE'])
        author.append(row['AUTHOR'])

print(time.localtime())

drink_notify = ToastNotifier()
#exercise_notify = ToastNotifier()

#i = input("Message: ")
custom_notify = ToastNotifier()


working_dir = pathlib.Path(__file__).parent.absolute()

is_night = 0

while 1:
    num = randint(1, len(quotes))
    print(quotes[num] + " | quote from: " + author[num])
    current_time = time.localtime()
    if current_time.tm_hour > 12:
        am_or_pm = "PM"
    else:
        am_or_pm = "AM"
    if current_time.tm_hour >= 21:
        is_night = 1 # change when your bed time is through this logic
    while is_night == 1:
        custom_notify.show_toast(f"It's getting pretty late...","Get some rest. Reward yourself from a day of hard work, and respect your body's health. \n\n Here is an inspirational quote to finish off the day...",icon_path=f'{working_dir}\PogChamp.ico',duration=10)
        custom_notify.show_toast(f"{author[num]}",f"{quotes[num]}",duration=10)
        img = Image.open(f'{working_dir}\images\sleep.jpg')
        img.show()
        exit()
    if current_time.tm_min <= 40:
        #print(f'{working_dir}\pogchamp.png')
        custom_notify.show_toast(f"{author[num]}",f"{quotes[num]}",duration=2)
        img = Image.open(f'{working_dir}\images\pepe_cool.png')
        img.show()
    if current_time.tm_min > 30 and current_time.tm_min <= 34:
        drink_notify.show_toast("Reminder to Hydrate!", "You should drink at least 3 water bottles per day. Stay fresh!",icon_path=f'{working_dir}\PogChamp.ico',duration=10)


        
        
        #custom_notify.show_toast(f"Year is {time.localtime().tm_year}", f"Time is {time.localtime().tm_hour % 12}:{time.localtime().tm_min}:{time.localtime().tm_sec} {am_or_pm}", icon_path=None, duration=5)

#exercise_notify.show_toast("Pushups! NOW!", "Exercise improves your cognitive performance.",icon_path=None,duration=10)
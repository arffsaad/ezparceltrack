from os import system
from requests_html import HTMLSession
from time import sleep

couriers = ["null","jt","poslaju", "ninjavan"]
print("\nEZ ParcelTracker")
courier = int(input("Select your courier\n[1] J&T\n[2] Poslaju\n[3] Ninja Van\n"))
tracking = input("\nEnter your tracking number: ")
tail = couriers[courier] + "/" + tracking

system('cls')
print("Tracking...")
session = HTMLSession()
resp = session.get("https://www.tracking.my/" + tail)
resp.html.render(timeout=30)

stat = resp.html.find('#tracking', first=True)
stat = stat.text.split("\n")
stat = stat[0].replace(" ","")

if (stat == "pending"):
    sleep(0.3)
    print(".", end="")
    sleep(0.3)
    print(".", end="")
    sleep(0.3)
    print(".", end="")
else:
    statsel = "#tracking > div.text-center.tracking-status-" + stat
    status = resp.html.find(statsel, first=True)
    date = resp.html.find('#tracking > div.tracking-list > div:nth-child(1) > div.tracking-date', first=True)
    date = date.text[0:-8]
    time = resp.html.find('#tracking > div.tracking-list > div:nth-child(1) > div.tracking-date > span', first=True)
    details = resp.html.find('#tracking > div.tracking-list > div:nth-child(1) > div.tracking-content',first=True)
    location = resp.html.find('#tracking > div.tracking-list > div:nth-child(1) > div.tracking-content > span', first=True)
    details = details.text[0:-(len(location.text))]

system('cls')

if (stat == "pending"):
    print("Not Found. It's either:\n1. Your parcel has just been shipped, and has not reflected in the system\n2. You mistyped your tracking number.")
else:
    print("CURRENT PARCEL STATUS: ", status.text.upper(), "\n")
    sleep(0.3)
    print(date, end= "\t")
    sleep(0.3)
    print(time.text.upper(),end = "\n\n")
    sleep(0.3)
    print(details)
    sleep(0.3)
    print(location.text, "\n\n")

input("Press Enter to exit...")


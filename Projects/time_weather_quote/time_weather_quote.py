from tkinter import *
from tkinter import ttk
from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
from quoters import Quote


def get_time():
    current_time = datetime.now().strftime("%I:%M %p")
    output.set(current_time)


def get_weather():
    # sends a http request
    # creates a new response object
    response = requests.get(url="https://www.google.com/search?q=weather")

    # check for HTTP 200 OK success, indicating the request succeded
    print("Recieved:", response.status_code)
    if response.status_code == 200:
        # print("success")
        soup = bs(response.content, "html.parser")

        forecast = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
        # print(forecast)
        output.set(forecast)


def get_quote():
    output.set(Quote.print())


main = Tk()
main.title("Test Gui App")
main.geometry("355x200")

main.columnconfigure(3, weight=0)
main.rowconfigure(2, weight=3)


main_frame = ttk.Frame(padding="3 3 12 12")
main_frame.grid(row=0, column=0)


output = StringVar()

ttk.Button(
    main,
    text="time",
    width=5,
    command=get_time,
).grid(row=1, column=1)

ttk.Button(main, text="weather", width=8, command=get_weather).grid(row=1, column=2)
ttk.Button(main, text="quote", width=6, command=get_quote).grid(row=1, column=3)

ttk.Label(main, textvariable=output).grid(row=2, column=2)

main.mainloop()

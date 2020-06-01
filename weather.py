from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Tkinter App")
root.iconbitmap("icons/gor.ico")
# root.minsize(300, 250)
root.geometry("600x100")


def getZip():
    try:
        api_request = requests.get(
            f"http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zip.get()}&date=2020-06-01&distance=5&API_KEY=FCD00D59-7954-4D65-813D-837392E665FC"
        )
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        quality = str(api[0]["AQI"])
        category = api[0]["Category"]["Name"]

        if category == "Good":
            bg_color = "#0C0"
        elif category == "Moderate":
            bg_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            bg_color = "#ff900"
        elif category == "Unhealthy":
            bg_color = "#FF0000"
        elif category == "Very Unhealthy":
            bg_color = "#990066"
        elif category == "Hazardous":
            bg_color = "#660000"
    except Exception as e:
        api = f"Error encountered: {e}"
        print(api)
    else:
        postResult(city, quality, category, bg_color)


def callback(event):
    getZip()


def postResult(city: str, quality: str, category: str, bg_color):
    global myLabel
    myLabel.grid_forget()
    myLabel.configure(text=city + " Air quality: " + str(quality) + " (" + category + ")")
    myLabel.configure(font=("Helvetica", 20))
    myLabel.configure(background=bg_color)
    root.configure(background=bg_color)
    myLabel.grid(row=1, column=0, columnspan=2)


myLabel = Label(root, text="")
myLabel.grid(row=1, column=0, columnspan=2)

zip = Entry(root)
zip.bind("<Return>", callback)
zip.grid(row=0, column=0, sticky="wesn")

submitButton = Button(root, text="Submit", command=getZip)
submitButton.grid(row=0, column=1, sticky="wesn")

# Event loop
root.mainloop()

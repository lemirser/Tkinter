from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Tkinter App")
root.iconbitmap("icons/gor.ico")
# root.minsize(300, 250)
root.geometry("450x40")


try:
    api_request = requests.get(
        "http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=89129&date=2020-06-01&distance=5&API_KEY=FCD00D59-7954-4D65-813D-837392E665FC"
    )
    api = json.loads(api_request.content)
    city = api[0]["ReportingArea"]
    quality = api[0]["AQI"]
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

    myLabel = Label(
        root,
        text=city + " Air quality: " + str(quality) + " (" + category + ")",
        font=("Helvetica", 20),
        background=bg_color,
    )
    root.configure(background=bg_color)
    myLabel.pack()
except Exception as e:
    api = f"Error encountered: {e}"
    print(api)


# Event loop
root.mainloop()

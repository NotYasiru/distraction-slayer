from dotenv import load_dotenv
from openai import OpenAI
import os
import asyncio
import datetime
import pygetwindow as gw
import serial 

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
arduino = serial.Serial(port='your port', baudrate=9600, timeout=.1) #replace your arduino board's port

def alarm(signal):
    print("alarm")
    arduino.write(bytes(signal, 'utf-8'))


def save_window_data(date, time, window):    
    directory_path = "window_data"
    file_path = os.path.join(directory_path, f"{date}.txt")
    
    try:
        with open(file_path, "a") as f:
            f.write(f"{time} {window}\n")
            print("Data written successfully.")
    except Exception as e:
        print("An error occurred:", e)

async def monitor_active_window():
    previous_window_title = ""
    
    while True:        
        current_window_title = get_active_window_title()
        
        if current_window_title and current_window_title != previous_window_title:
            alarm("1")

            current_window_title_low = current_window_title.lower()

            browsers = ["opera", "edge", "chrome"]   #add your browsers
            banned = ["facebook", "instagram"]       #add the sites

            date_and_time = str(datetime.datetime.now())[:-7]
            save_window_data(date_and_time[:-9], date_and_time[10:], current_window_title_low)

            #print(current_window_title_low)

            if any(word in current_window_title_low for word in browsers):
                if "youtube" in current_window_title_low:
                    vid_title = str((current_window_title_low.split(" - "))[:-2])
                    if vid_title != "[]":
                        client = OpenAI()
                        completion = client.chat.completions.create(
                          model="gpt-3.5-turbo",
                          messages=[
                            {"role": "system", "content": "Identify the category to which the given title belongs. Reply only one of these(music/ education/ technology/ science/ life/ entertainment)"},
                            {"role": "user", "content": vid_title}
                          ]
                        )

                        ai_result = str(completion.choices[0].message.content.lower())

                        #print(ai_result)


                        if ai_result in ["music", "entertainment"]:
                            alarm("2")
                
                elif any(word in current_window_title_low for word in banned):
                    #print("banned site")
                    alarm("2")

            previous_window_title = current_window_title
        
        await asyncio.sleep(5)

def get_active_window_title():
    active_window = gw.getActiveWindow()
    return active_window.title if active_window else None


def monitor_contains_window_title(monitor, window_title):
    for window in gw.getAllWindows():
        if window.title == window_title:
            window_center_x = window.left + (window.width / 2)
            window_center_y = window.top + (window.height / 2)
            if monitor.x <= window_center_x <= monitor.x + monitor.width and monitor.y <= window_center_y <= monitor.y + monitor.height:
                return True
    return False

if __name__ == "__main__":
    asyncio.run(monitor_active_window())

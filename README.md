Distraction Slayer
==================

Distraction Slayer is a Python script designed to help you maintain focus by detecting distracting websites or applications while you work. When a distraction is detected, it automatically closes the distracting software or the browser tab. Additionally, you have the option to integrate an Arduino board equipped with a taser or loud buzzer to provide a physical reminder to stay focused.

Installation
------------

Before running the Python script, ensure you have the required libraries installed. You can install them using pip:

`pip install python-dotenv`

`pip install openai`

`pip install pygetwindow`


To use the Arduino functionality, install pyserial:

`pip install pyserial`

Arduino Setup
-------------

To use Distraction Slayer with an Arduino board, follow these steps:

1.  Upload the provided [Arduino code](https://github.com/NotYasiru/distraction-slayer/blob/main/distraction_slayer_arduino/distraction_slayer_arduino.ino) to your Arduino board. This code includes functionality for controlling an indicator, such as a buzzer or taser.
    
2.  Connect the indicator (buzzer/taser) to the appropriate pin on your Arduino board, as specified in the uploaded Arduino code.
    
3.  Ensure your Arduino board is connected to your computer via USB.
    

Usage
-----

Before running the Python script, make sure to configure the following:

1.  **ChatGPT API Key**: Enter your ChatGPT API key in the **.env** file.
    
2.  **Arduino Board's Port**: If you want use Arduino functionality, add your Arduino board's port to the **main.py** file. Otherwise, leave it black like this. `arduino = serial.Serial(port='', baudrate=9600, timeout=.1)`
    
3.  **Close Arduino IDE**: Make sure to close the Arduino IDE before executing the Python script to prevent interference with the Arduino board's port.
    

Once you have completed the setup, you can run the main Python script. Simply execute the following command:

`python main.py`

The script will monitor your screen activity and identify distracting websites or applications based on your configuration. If an Arduino is connected, the indicator on your Arduino board will activate when distractions are detected. This will automatically close the distracting application or browser tab.

Additionally, Distraction Slayer utilizes the OpenAI API to identify the type of videos the user watches on YouTube.

Configuration
-------------

You can customize the behavior of Distraction Slayer by modifying the configuration options in the **main.py** file.


Acknowledgments
---------------

*   This project was inspired by the need to maintain focus in an increasingly distracting digital environment.

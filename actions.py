import os
import webbrowser
import datetime
import psutil
from speech.speak import speak

# Volume control imports
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def set_volume(change):
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevelScalar()

        if change == "up":
            volume.SetMasterVolumeLevelScalar(min(current + 0.1, 1.0), None)
        elif change == "down":
            volume.SetMasterVolumeLevelScalar(max(current - 0.1, 0.0), None)
        elif change == "mute":
            volume.SetMute(1, None)
    except Exception as e:
        speak("Sorry, I could not control the volume.")
        print("Volume error:", e)


def perform_action(command):

    # Handle tuple for commands with extra data
    if isinstance(command, tuple):
        cmd_name, response = command
    else:
        cmd_name = command
        response = None

    if cmd_name == "HELLO":
        speak("Hello Vandana! How can I help you?")

    elif cmd_name == "OPEN_CHROME":
        speak("Opening Chrome for you.")
        webbrowser.open("https://www.google.com")

    elif cmd_name == "PLAY_MUSIC":
        speak("Playing music for you.")
        webbrowser.open("https://open.spotify.com")

    elif cmd_name == "OPEN_NOTEPAD":
        speak("Opening Notepad.")
        os.system("notepad")

    elif cmd_name == "WHATSAPP":
        speak("Opening WhatsApp Web.")
        webbrowser.open("https://web.whatsapp.com")

    elif cmd_name == "TIME":
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")

    elif cmd_name == "BATTERY":
        battery = psutil.sensors_battery()
        percent = battery.percent
        speak(f"Your battery level is {percent} percent")

    elif cmd_name == "DATE_DAY":
        today = datetime.datetime.now()
        date = today.strftime("%d %B %Y")
        day = today.strftime("%A")
        speak(f"Today is {day}, {date}")

    elif cmd_name == "VOLUME_UP":
        set_volume("up")
        speak("Increasing volume")

    elif cmd_name == "VOLUME_DOWN":
        set_volume("down")
        speak("Decreasing volume")

    elif cmd_name == "MUTE":
        set_volume("mute")
        speak("Volume muted")

    elif cmd_name == "PLAY_SPECIFIC_MUSIC":
        import urllib.parse
        song_name, platform = response
        query = urllib.parse.quote(song_name)

        if platform == "ytmusic":
            url = f"https://music.youtube.com/search?q={query}"
        else:
            url = f"https://www.youtube.com/results?search_query={query}"

        speak(f"Playing {song_name} on YouTube Music")
        webbrowser.open(url)

    elif cmd_name == "SEND_WHATSAPP_MESSAGE":
        name, msg = response
        speak(f"Opening WhatsApp chat to {name}")
        webbrowser.open("https://web.whatsapp.com")
        # Optional: pyautogui automation later

    elif cmd_name == "EXIT":
        speak("Goodbye Vandana! Have a nice day.")
        return False

    else:
        speak("Sorry, I did not understand that.")

    return True
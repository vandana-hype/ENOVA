def classify_command(text):
    text = text.lower()

    if "hello" in text:
        return "HELLO"

    elif "chrome" in text:
        return "OPEN_CHROME"

    elif "music" in text and "play" not in text:
        return "PLAY_MUSIC"

    elif "notepad" in text:
        return "OPEN_NOTEPAD"

    elif "whatsapp" in text:
        return "WHATSAPP"

    elif "time" in text:
        return "TIME"

    elif "battery" in text:
        return "BATTERY"

    elif "date" in text or "day" in text:
        return "DATE_DAY"

    elif "volume up" in text or "increase volume" in text:
        return "VOLUME_UP"

    elif "volume down" in text or "decrease volume" in text:
        return "VOLUME_DOWN"

    elif "mute" in text:
        return "MUTE"

    elif "play" in text:
        # Specific music handling
        song_name = text.replace("play", "").strip()
        platform = "youtube"  # default

        if "youtube music" in song_name:
            platform = "ytmusic"
            song_name = song_name.replace("youtube music", "").strip()

        return "PLAY_SPECIFIC_MUSIC", (song_name, platform)

    elif "message" in text or "msg" in text:
        # Flexible WhatsApp message
        if "message" in text:
            text = text.replace("message", "").strip()
        else:
            text = text.replace("msg", "").strip()

        parts = text.split(" ", 1)  # first word = name, rest = message
        if len(parts) == 2:
            name = parts[0]
            msg = parts[1]
            return "SEND_WHATSAPP_MESSAGE", (name, msg)
        else:
            return "UNKNOWN", None

    elif "exit" in text or "stop" in text:
        return "EXIT"

    else:
        return "UNKNOWN"
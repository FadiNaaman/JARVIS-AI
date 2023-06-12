import commands

def understand(query):
    # Introductions

    # Groceries

    # Academic

    # Email

    # Definition

    # Media

    # SETTINGS #
    # Raise Volume
    if("volume" in query):
        if ("raise" in query):
            commands.changeVolume(0.1)
        if ("lower" in query):
            commands.changeVolume(-0.1)
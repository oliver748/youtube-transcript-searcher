from os import system
from datetime import timedelta


def title(title): # creates a title for the console
    return system("title " + title)


def clear(): # clears the console for a more clean look
    return system("cls")


def formatter(string, detour): 
    """
    yes, this is near impossible to understand but it basically takes the 
    transcript that's been given to this function and formats it, then
    sends it back - really hard to make it readable
    """
    string_split = string.split(", ")
    subtitle_string = string[9:len(string_split[0])-1]
    time = string_split[1][9:len(string_split[1])]
    timecode = timedelta(seconds=round(float(time))-detour)
    
    return subtitle_string, timecode


def setup(): 
    """
    was made because future implementations in setup are needed so why not
    make this in the start instead of changing it in the future; gives a
    much better structure aswell
    """
    channel_ids = input("File name where all channel ids are (.txt): ")
    content_search = input("Content to search for (delimiter=comma): ").lower()
    return channel_ids, content_search.split(',')
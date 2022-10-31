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

def output_result(string, file_name):
    with open(file_name, "a") as output:
        output.write(f"{string}\n")

def setup(): 
    """
    was made because future implementations in setup are needed so why not
    make this in the start instead of changing it in the future; gives a
    much better structure aswell
    """
    print("Note: Leave output file name blank if you don't wanna output results\n")
    channel_ids = input("File name where all channels are (.txt): ")
    content_search = input("Content to search for (delimiter=comma): ").lower()
    output_file = input("File name to output results (.txt): ")
    return channel_ids, content_search.split(','), output_file
import os
import requests
from ServerCollector import ServerCollector
from ScraperCode import scrape
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

"""
The beginning GUI to be run for scraping
"""

channelIDs = ServerCollector()
MAX_IN_UNCOMPRESSED = 100_000 #The maximum amount of messages in an uncompressed file before being forced to run Huffman Compression
#Gets token and guild information

token = channelIDs[-1]
print(f"Token: {token}")
channelIDs.pop(-1)
guild = channelIDs[-1]
print(f"Guild: {guild}")
channelIDs.pop(-1)

serverName = requests.get(f"https://discord.com/api/v9/guilds/{guild}"
                          , headers={"authorization":token}).json()['name']

filePath = ""

def getFile():
    global filePath
    root = tk.Tk()
    root.withdraw() 
    
    selected_path = filedialog.askdirectory(title="Select Folder to store messages")
    
    if selected_path:
        filePath = selected_path
        try:
            os.mkdir(f"/{filePath}/{serverName}/")
        except FileExistsError:
            print("File exists")
    root.destroy()
getFile()

#Loops for every desired channel
for channel in channelIDs:


    lastID = 0  # message ID
    currentMessages = 0 #Current messages in a file
    stopID = -1
    #Get channel name again
    r = requests.get(f"https://discord.com/api/v9/channels/{channel}",
                     headers = {'authorization':token})
    channelName = r.json()['name']

    print(channelName)

    #Get approximate num messages
    r = requests.get(f"https://discord.com/api/v9/guilds/{guild}/messages/search?channel_id={channel}"
                     + "&sort_by=timestamp&sort_order=desc&offset=0",
                     headers = {'authorization':token})
    totalMessages = r.json()['total_results']
    print(f"Total messages: {totalMessages}")

    #Attempts to open file
    try:
        file = open(f"{filePath}/{serverName}/{channelName}.txt","w")
    except FileNotFoundError:
        file = open(f"{filePath}/{serverName}/{channelName}.txt","x")
        file.close()
        file = open(f"{filePath}/{serverName}/{channelName}.txt","w")


    scrape(token, channel, int(stopID), file, totalMessages, channelName, MAX_IN_UNCOMPRESSED)



    file.close()
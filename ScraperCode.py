import requests
import tkinter as tk
from tkinter import ttk
import time

def scrape(token, channelID, stopID, file, totalMessages, channelName, MAX_IN_UNCOMPRESSED) -> tuple[int, int]:

    allMessages = 0
    currentMessages = 0
    lastID = 0
    scraperSession = requests.Session()
    def update():
        """
        Updates the progress bar to reflect the amount of messages scraped

        And runs scraper code
        """

        nonlocal lastID
        nonlocal percentage_label
        nonlocal currentMessages
        nonlocal totalMessages
        nonlocal allMessages
        nonlocal scraperSession

        headers = {'authorization':token}
        scraperSession.headers.update(headers)
        while True:
            start = time.time()

            if lastID == 0:
                r = scraperSession.get(f"https://discord.com/api/v9/channels/{channelID}/messages?limit=100")
            else:
                r = scraperSession.get(f"https://discord.com/api/v9/channels/{channelID}/messages?limit=100&before={lastID}")
            if r.status_code != 200:
                pass
                time.sleep(1)
                #temporal connection issue
            else:
                print(f"Scrape time: {(time.time()-start)}")
                start = time.time()
                messages = r.json()
                if len(messages) == 0:
                    root.destroy()
                    file.close()
                    return currentMessages, -1
                for message in messages:
                    file.write(str(message) + '\n')
                lastID = int(messages[-1]['id'])

                currentMessages += len(messages)
                allMessages += len(messages)
                progressBar['value'] += len(messages)
                print(progressBar['value'])
                progressBar.update_idletasks()
                percentage_label.config(text=f"{progressBar['value'] * 100 / totalMessages}%")
                #Updates until the channel is fully scraped at the desired point
                if lastID <= stopID:
                    root.destroy()
                    file.close()
                    return currentMessages, -1
                print(f"Process time: {(time.time()-start)}")


        


    #Progress bar for channel
    root = tk.Tk()
    root.title(channelName)
    progressBar = ttk.Progressbar(root, mode='determinate', length=200)
    progressBar.pack(pady=20)
    percentage_label = tk.Label(root, text="0%")
    percentage_label.pack()
    progressBar['maximum'] = totalMessages
    progressBar['value'] = 0
    root.after(1, update)
    root.mainloop()




    
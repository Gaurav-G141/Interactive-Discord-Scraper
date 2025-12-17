from ChannelSelector import makeBoxes,tk
import requests
from tkinter import messagebox

def ServerCollector() -> list[str]:
    """
    The primary function responsible for requesting all the channels the user wants to scrape

    Params:
        - Token: This is the user's token, will be used to allow the discord API to be used
        - Server ID: This is the ID of the server to be scraped.

    Returns:
        - Returns a list of strings
        - The majority of the list will be the IDs of every channel the user wishes to scrape
        - The second to last String is the ID of the guild. This is required for collecting messages later in the code
        - The last String is the user's token, again required for collecting messages later in the code
    """
    channels = [] #The names of each channel in this server the user can access
    ids = {} #Maps the names in channels to their IDs
    token = ""
    guild = ""
    def retrieve_input(textbox) -> str:
        """
        Gets the input from a textbox
        """
        return textbox.get("1.0",'end-1c')

    def clear(root) -> None:
        """
        Clears the root at the end of ServerCollector
        """
        for widget in root.winfo_children():
            widget.destroy()

    def getToken() -> None:
        """
        Extracts the user's tokens from the token box
        """
        nonlocal token
        s = retrieve_input(tokenWidget)
        s = s.replace('\n','')
        token = s
        return s


    def displayChannels() -> list[str]:
        """
        Generates boxes based on every channel available to the user

        Params:
            - Uses the token and guild ID collected before calling this method
        Returns:
            - Will first display a checkbox for every channel the user has read access to
            - Will return a list of names of every channel the user wishes to scrape
        """
        nonlocal ids
        nonlocal guild
        guild = retrieve_input(serverWidget)
        r = requests.get(f"https://discord.com/api/v9/guilds/{retrieve_input(serverWidget)}",
                         headers= {'authorization':getToken()})
        #If the user token or guild ID is invalid, try again
        if r.status_code != 200:
            messagebox.showerror("Invalid requests", "Something went wrong when you inputted your token "
                                                    + "and server. Make sure that the server ID and token is correct")
            exit()

        else:
            #Save server information
            server_id = r.json()['id']
            server_name = r.json()['name']
            r = requests.get(f"https://discord.com/api/v9/guilds/{server_id}/channels",
                             headers={'authorization': getToken()})
            ids = {}
            for s in r.json():
                print(s["name"])
                #If the channel can be read, add it to the list of IDs
                print(s)
                print()
                print()
                if s['type'] in {0,5,15}:
                    r = requests.get(f"https://discord.com/api/v9/channels/{s['id']}/messages",
                                 headers={'authorization': getToken()})
                    if r.status_code == 200:
                        ids[s["name"]] = s["id"]
            print(ids)
            clear(root)
            return makeBoxes(server_name, list(ids.keys()), root)

    def end():
        """
        Sets the channels variable, ending this section of the program
        """
        nonlocal channels
        channels = displayChannels()

    #Main display
    root = tk.Tk()
    root.option_add("*Font", "Arial 12")
    root.geometry("800x800")

    serverLabel = tk.Label(root, text="Server ID (NOT NAME)")
    serverLabel.pack(pady=10)
    serverWidget = tk.Text(root, height=10, width=50, wrap=tk.WORD)
    serverWidget.pack(pady=10)

    tokenLabel = tk.Label(root, text="Your token")
    tokenLabel.pack(pady=10)
    tokenWidget = tk.Text(root, height=10, width=50, wrap=tk.WORD)
    tokenWidget.pack(pady=10)

    submission_button = tk.Button(root, text="Get Channels", command=end)
    submission_button.pack(pady=10)



    root.mainloop()
    f = [ids[c] for c in channels]
    f.append(guild)
    f.append(token)
    return f
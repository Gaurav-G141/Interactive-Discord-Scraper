**OVERVIEW**

This program is a fully interactive Discord scraper, complete with a GUI for ease of use to collect the message contents of any discord server you wish to collect

Uses tkinter for the GUI and requests for collecting messages, using the offical discord API


**Files**

- ServerCollector.py: Requests the user's token and server ID
- ScraperCode.py: Code for scraping the messages from a particular channel
- ChannelSelector.py: Gives users the options to select the desired channels they want to have scraped
- main.py: The first executed piece of code, calls the other three

**DEPENDENCIES**

- Tkinter: Used for GUI, including textboxs and file selector
- OS: Used for writing files outside of the directory of the code
- Requests: Used to send URL requests, for this program Discord API, in order to collect messages

**HOW TO USE**

First, download all code files and run main.py

Step 1) In the boxes that show, enter in the ID of your server and your discord token
  - Use [this video](https://www.youtube.com/watch?v=xh28F6f-Cds) to see how to access your token
  - To get your server ID, use [this video](https://www.youtube.com/watch?v=HjkRZy5d_qM)
  - **IMPORTANT SAFETY NOTE** Your API token is the primary way discord lets you use your account. Someone with your token will have full access to your account, even if you have secondary measures such as 2FA. NEVER GIVE OUT YOUR DISCORD TOKEN UNLESS YOU'RE FULLY CONFIDENT IN THE CODE USING YOUR TOKEN

Step 2) The program will manually check each channel in the server for read access. This may take a few minutes
  - Once it has done so, select the channels you would like to have scraped
  - If you want to scrape most or all of the channels in the server, use the flip all button to flip every checkbox

Step 3) Once you've confirmed your channels, select the location where you'd like to have the scraped messages saved to
  - Ensure that the directory is somewhere that your user has write/create file access to

Step 4) Simply wait for every channel to be scraped. At the end, you will have a folder with the server name, and a file for each channel with those channel's messages
  - Space: Around 1.7 KB per message
  - Time: To write/process messages is very short, around 0.01 seconds/100 messages. By far more time will be spent in the actual requests (for home wifi I get a rate of of 0.3-0.4 seconds/100 messages. While ethernet/faster WIFI can reduce these times, due to rate limits on API usage, I would not recommend going below 0.2 seconds/100 messages)

If you'd like to read more on how these messages are formatted, the [Discord Developer Portal](https://discord.com/developers/docs/intro) has multiple resources over message/channel objects and scraping

**IMPORTANT NOTICE**

Discord does not offically allow the usage of API requests on your own account (or any non-bot account) for scraping purposes. This is purely for educational purposes, and API requests should never be used for malicious intent.

Like a password, it is your responsibility to keep your token safely guarded. Never input your token into software with unknown origins, and do not share tokens with anyone over non-secure communication links.

Finally, regardless of intent, for ethical reasons you should never scrape a server without owner/admin consent. The adminstrative team of whichever server you wish to scrape should have full knowledge of what you're scraping and how you plan to use the data in question. Never upload the result of scraped data online without server owner consent. If you're scraping a server where you'd have access to channels that could be considered private (such as staff channels or pateron), do not scrape those channels. Do not scrape any channels considered private or for specific people.    

  


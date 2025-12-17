import tkinter as tk


def end(buttons, isChecked) -> list[str]:
    """
    Marks the end of this section of the program, verifies the buttons to be pressed

    Params:
        - Buttons: Every button that could've been checked
        - isChecked: A list showing whether each button was pressed

    Return: A list of channel names that the user wished to have accessed
    """
    ans = []
    for i in range(len(buttons)):
        if (isChecked[i].get()) == 1:
            print(buttons[i].cget("text"))
            ans.append(buttons[i].cget("text"))
    print("Button pressed")
    return ans

def makeBoxes(server, channels, root) -> list[str]:
    """
    The main method for this section of the code, runs during ServerCollector

    Params:
        - server: ID of the discord server
        - channels: List of Every channel the user can read (by name)
        - root: Tkinter root window

    Return:
        - The list of channels (by name) the user wished to have scraped
    """
    ans = [] #The list of channel names
    index = 0 #Position of the buttons
    ADJUST = 17 #The maximum length of any channel name. Ensures that channel names do not overlap while
    # keeping neat aesthetics

    root.title(f"Channels in {server} accessible to you")

    #Makes list of buttons to be pressed/unpressed
    isChecked = [tk.IntVar() for i in range(len(channels))]
    buttons = [tk.Checkbutton(
        text = channels[i],
        variable = isChecked[i],
        onvalue = 1,
        offvalue = 0,
        command = "")
        for i in range(len(channels))
    ]

    def endHelper():
        """Nested function for calling end method"""
        nonlocal ans
        ans = end(buttons=buttons, isChecked=isChecked)
        root.destroy()



    #Shows 17 buttons at once. GoLeft and GoRight changes which one
    def showSome():
        nonlocal index
        y = 0
        for i in range(ADJUST * index, min(ADJUST * index + ADJUST,len(buttons))):
            (buttons[i]).place(x = 0,y = y)
            y += 20

    #Unshows those 17 buttons
    def unshow():
        nonlocal index
        for i in range(ADJUST * index, min(ADJUST * index + ADJUST,len(buttons))):
            (buttons[i]).place_forget()

    #Moves the selection panel left or right
    def goLeft():
        nonlocal index
        nonlocal root
        unshow()
        if (index != 0):
            index -= 1
        showSome()
        displayButtons()
    def goRight():
        nonlocal index
        nonlocal root
        unshow()
        if (index * ADJUST + ADJUST < len(buttons)):
            index += 1
        showSome()
        displayButtons()



    def flipAll():
        """Flip the sign of every button"""
        nonlocal isChecked
        for i in range(len(isChecked)):
            if isChecked[i].get() == 1:
                isChecked[i].set(0)
            else:
                isChecked[i].set(1)


    def displayButtons():
        #End button
        endButton = tk.Button(root, text="Select channels", command=endHelper)
        endButton.place(x = 0, y = 550)
        #Flip button
        flipButton = tk.Button(root, text="Flip All", command=flipAll)
        flipButton.place(x = 0, y = 600)
        #Left and Right button
        leftButton = tk.Button(root, text="Scroll left", command=goLeft)
        leftButton.place(x = 100,y = 600)
        rightButton = tk.Button(root, text="Scroll right", command=goRight)
        rightButton.place(x = 200,y = 600)


    #Display
    
    showSome()
    displayButtons()
    root.mainloop()
    return ans
import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os
import re

def play():
    ''' For playing music '''
    pygame.mixer.music.load(playList.get(tkinter.ACTIVE))  # Set selected music to active
    var.set(playList.get(tkinter.ACTIVE))  # Set a variable to the song
    pygame.mixer.music.play()  # Play the song

def stop():
    ''' To stop music '''
    pygame.mixer.music.stop()

def pause():
    ''' To pause music '''
    pygame.mixer.music.pause()

def resume():
    ''' To resume music '''
    pygame.mixer.music.unpause()

def masterButton():
    ''' The button to play/stop/pause/resume music '''
    global buttonText

    if pygame.mixer.music.get_busy():  # Checks if music is playing
        pause()
        buttonText.set("Play")
    else:
        if var.get() == playList.get(tkinter.ACTIVE):  # Checks if selected music was the one playing or not
            resume()
            buttonText.set("Pause") 
        else:
            stop()  # Stop the current playing music
            play()  # Start playing the selected music
            buttonText.set("Pause")

def lowerVolume():
    ''' Decreases volume '''
    newVolume = pygame.mixer.music.get_volume() - 0.1
    pygame.mixer.music.set_volume(newVolume)
    volume.set(str(int(newVolume*100)) + " %")

def raiseVolume():
    ''' Increases volume '''
    newVolume = pygame.mixer.music.get_volume() + 0.1
    pygame.mixer.music.set_volume(newVolume)
    volume.set(str(int(newVolume*100)) + " %")

def setDirectory():
    ''' Sets the directory according to user '''
    global songList, playList
    directory = askdirectory() # Asks directory from user
    os.chdir(directory)  # Sets the directory to the directory user chooses
    songList = os.listdir()  # Creating song list
    playList.delete(0, tkinter.END)  # Empties the playlist
    # Adding songs from songList to playList
    counter = True  # Checks if any songs are there or not
    pos = 0
    for item in songList:
        if re.search(".mp3$", item):
            playList.insert(pos, item)
            pos = pos + 1
            counter = False

    if counter:  # Checks if any songs are present or not
        playList.insert(pos, "No MP3 songs found")

def packEverything():
    ''' One function for packing everything '''
    songTitle.pack()
    playList.pack(fill = "both", expand = "yes")
    playButton.pack(side = tkinter.TOP)
    changeDirectory.pack(side = tkinter.LEFT)
    increaseVolume.pack(side = tkinter.RIGHT)
    decreaseVolume.pack(side = tkinter.RIGHT)
    volumeLabel.pack(side = tkinter.BOTTOM)



musicPlayer = tkinter.Tk()  # Creating a tkinter window
musicPlayer.title('MUSIC PLAYER')  # Setting title
musicPlayer.geometry('800x600')  # Setting the size of the window
musicPlayer.configure(background='Yellow')  # Setting colour of window

songList = os.listdir()  # Creating song list
playList = tkinter.Listbox(musicPlayer, font = "times 17", bg = "Yellow", selectmode = tkinter.SINGLE)  # Creating playlist

# Adding songs from songList to playList
pos = 0
counter = True  # Checks if any songs are there or not
for item in songList:
    if re.search(".mp3$", item):  # RegEX for finding MP3 songs
        playList.insert(pos, item)
        pos = pos + 1
        counter = False

if counter:  # Checks if any songs are present or not
    playList.insert(pos, "No MP3 songs found")

# Initializing pygame modules
pygame.init()
pygame.mixer.init()

buttonText = tkinter.StringVar()
buttonText.set("Play")

# Creating buttons
playButton = tkinter.Button(musicPlayer, height = 2, width = 10, textvariable = buttonText, command = masterButton, bg = "#242B2E", fg = "#23C4ED")
decreaseVolume = tkinter.Button(musicPlayer, height = 2, width = 15, text = "Decrease Volume", command = lowerVolume, bg = "#242B2E", fg ="#23C4ED")
increaseVolume = tkinter.Button(musicPlayer, height = 2, width = 15, text = "Increase Volume", command = raiseVolume, bg = "#242B2E", fg = "#23C4ED")
changeDirectory = tkinter.Button(musicPlayer, height = 2, width = 15, text = "Change Directory", command = setDirectory, bg = "#242B2E", fg = "#23C4ED")

var = tkinter.StringVar()
songTitle = tkinter.Label(musicPlayer, font = "times 16", textvariable = var, fg = "green", bg = "Yellow")

volume = tkinter.StringVar()
volume.set(str(int(pygame.mixer.music.get_volume()*100)) + " %")
volumeLabel = tkinter.Label(musicPlayer, font = "times 14", textvariable = volume, bg = "Yellow")

packEverything()

musicPlayer.mainloop()  # Closing the loop
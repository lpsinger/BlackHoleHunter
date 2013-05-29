#!/usr/bin/env python

###############################################################################
# 
#  A Gravitational wave data analysis game.
#  Created by Cardiff University Relativity Group.
#  All rights reserved
#
###############################################################################

# Load necessary modules.
import cgi
import random
import sys
import ConfigParser
from GWDA_game_html import *
numBoxes = 4
numSignals = 84
numNoise = 84
maxPlays = 6
initLives = 2
path = "/mp3signalBankglitchesnew/"
glitchpath = "/mp3signalBankglitchesnew/"
localpath = "../.."


def GWDA_game_main():
  # Main program.

  # Read difficulty level from input.

  form = cgi.FieldStorage()

  try:
    numPlays = int(form.getvalue("numplays"))
    numLives = int(form.getvalue("numlives"))
    userScore = int(form.getvalue("userscore"))  
  except:
    numPlays = 0
    numLives = initLives
    userScore = 0
  try:
    difficultyLevel = int(form.getvalue("difficulty"))
  except:
    htmlOutput = html_header_standard()
    htmlOutput += error_form_reading()
    return htmlOutput

  if numLives < 1:
    htmlOutput = html_header_standard()
    htmlOutput += game_over(False,userScore)
    return htmlOutput
  if numPlays > (maxPlays - 1):
    htmlOutput = html_header_standard()
    htmlOutput += game_over(True,userScore)
    return htmlOutput
 
  if difficultyLevel > 5:
    tempLevel = 5
  elif difficultyLevel < 6 and difficultyLevel > 3:
    tempLevel = 4
  else:
    tempLevel = difficultyLevel

  # Randomly choose the signals and noise files.
  # Choose location of signal

  signalLocation = random.randrange(0,numBoxes,1)
  signalFlag = False
  waveSound = []
  wavePicture = []
  temppath = ""

  for i in range(0,numBoxes):
    if i == signalLocation:
      j = random.randrange(1,11,1)
      temppath = path
      signalsound = "/data" + str(tempLevel) + ".mp3"
      signalpic = "/data" + str(tempLevel) + ".jpg"
      signoisepic = "/signal" + str(tempLevel) + ".jpg"
      if tempLevel > 2:
        if (difficultyLevel == 3 and j < 3) or (difficultyLevel == 4 and j < 4) or (difficultyLevel == 5 and j < 8) or (difficultyLevel == 6 and j < 3) or (difficultyLevel == 7 and j < 6) or (difficultyLevel == 8 and j < 10):
          temppath = glitchpath
          signalsound = "/data" + str(tempLevel) + "glitch.mp3"
          signalpic = "/data" + str(tempLevel) + "glitch.jpg"
          signoisepic = "/signal" + str(tempLevel) + "glitch.jpg"
      randSignalIndex = random.randrange(1,numSignals+1,1)
      waveSound.append( temppath + "sigbank" + str(randSignalIndex) + \
                signalsound)
      wavePicture.append(temppath + "sigbank" + str(randSignalIndex) + \
                signalpic)
      signalSound = ( temppath + "sigbank" + str(randSignalIndex) + \
                "/hplus" + ".mp3")
      signalPicture = (temppath + "sigbank" + str(randSignalIndex) + \
                "/signal" + ".jpg")
      sigNoisePicture = (temppath + "sigbank" + str(randSignalIndex) + \
                signoisepic)
      iniFile = (localpath + temppath + "sigbank" + str(randSignalIndex) + \
                "/info" + ".ini")
      signalFlag = True
    else:
      randNoiseIndex = random.randrange(1,numNoise+1,1)
      temppath = path
      noisepic = "/noise.jpg"
      noisesound = "/noise.mp3"
      j = random.randrange(1,11,1)
      if tempLevel > 2:
        if (difficultyLevel == 3 and j < 3) or (difficultyLevel == 4 and j < 4) or (difficultyLevel == 5 and j < 8) or (difficultyLevel == 6 and j < 3) or (difficultyLevel == 7 and j < 6) or (difficultyLevel == 8 and j < 10):
          temppath = glitchpath
          noisepic = "/noise" + str(tempLevel) + "glitch.jpg"
          noisesound = "/noise" + str(tempLevel) + "glitch.mp3"
      waveSound.append( temppath + "sigbank" + str(randNoiseIndex) + \
                noisesound )
      wavePicture.append( temppath + "sigbank" + str(randNoiseIndex) + \
                noisepic )

  # Read the ini file
  
  configcp = ConfigParser.ConfigParser()
  configcp.read(iniFile)
  signalType = configcp.get("main","system")
  signalMass1 = configcp.get("main","mass1")
  signalMass2 = configcp.get("main","mass2")
  signalInclination = configcp.get("main","inclination")
 
  if signalFlag == False:
    htmlOutput = html_header_standard()
    htmlOutput += no_signal_set()
    return htmlOutput
  
  # Write html output
  
  if tempLevel > 2:
    glitchFlag = True
  else:
    glitchFlag = False

  htmlOutput = html_header_flash(waveSound,signalSound)
  htmlOutput += game_main_html(numBoxes,waveSound,wavePicture,signalSound, \
                      signalPicture,sigNoisePicture,signalType, \
                      signalMass1,signalMass2,signalInclination, \
                      signalLocation, userScore,difficultyLevel,glitchFlag, \
                      numPlays,numLives)
             
  return htmlOutput


def GWDA_game_results ():
  quoteFile = "../../quotes.ini"
  form = cgi.FieldStorage()
  wavePicture = []
  waveSound = []

  # Reading values from html form

  try:
    boxChoice = int(form.getvalue("answer"))
    boxEncryptedValue = int(form.getvalue("asfdghti"))
    sigNoisePicture = str(form.getvalue("signalpic"))
    userScore = int(form.getvalue("userscore"))
    difficultyLevel = int(form.getvalue("difficulty"))
    numPlays = int(form.getvalue("numplays"))
    numLives = int(form.getvalue("numlives"))
    wavePicture.append(str(form.getvalue("wavepic1")))
    wavePicture.append(str(form.getvalue("wavepic2")))
    wavePicture.append(str(form.getvalue("wavepic3")))
    wavePicture.append(str(form.getvalue("wavepic4")))
    waveSound.append(str(form.getvalue("wavesound1")))
    waveSound.append(str(form.getvalue("wavesound2")))
    waveSound.append(str(form.getvalue("wavesound3")))
    waveSound.append(str(form.getvalue("wavesound4")))    
  except:
    htmlOutput = html_header_standard()
    htmlOutput += error_form_reading()
    return htmlOutput 

  wavePicture[boxEncryptedValue] = sigNoisePicture  

  # Determine the correct value of the box:

  boxRealValue = boxEncryptedValue + 1

  # Choose a random quote to display

  configcp = ConfigParser.ConfigParser()
  configcp.read(quoteFile)
  numQuotes = int(configcp.get("main","numquotes"))
  randQuoteNum = random.randrange(1,numQuotes+1,1)
  quoteText = configcp.get("quote" + str(randQuoteNum),"quote")
  quoteLink = configcp.get("quote" + str(randQuoteNum),"weblink")
  quoteId = configcp.get("quote" + str(randQuoteNum),"quoteId")
  quoteDivId = configcp.get("quote" + str(randQuoteNum), "quoteDivId")
  quoteSrc = configcp.get("quote" + str(randQuoteNum), "quoteSrc")
  quoteHd = configcp.get("quote" + str(randQuoteNum), "quoteHd")
  htmlOutput = html_header_flash(waveSound,waveSound[0])
  numPlays += 1
  
  if boxChoice == boxRealValue:
    userScore += difficultyLevel
    difficultyLevel += 1
    htmlOutput += answer_given(True,wavePicture,userScore,quoteText,\
                                 quoteLink,quoteId,quoteDivId,quoteSrc,quoteHd,difficultyLevel,numPlays,numLives)
  else:
    userScore -= 1
    numLives -=1
    htmlOutput += answer_given(False,wavePicture,userScore,quoteText,\
                                 quoteLink,quoteId,quoteDivId,quoteSrc,quoteHd,difficultyLevel,numPlays,numLives)
  return htmlOutput

def GWDA_game_restart():
  form = cgi.FieldStorage()
  try:
    userScore = int(form.getvalue("userscore"))
    quoteText = str(form.getvalue("quotetext"))
    quoteLink = str(form.getvalue("quotelink"))
    quoteId = str(form.getvalue("quoteId"));
    quoteDivId = str(form.getvalue("quoteDivId"));
    quoteSrc = str(form.getvalue("quoteSrc"));
    quoteHd = str(form.getvalue("quoteHd"));
  except:
    htmlOutput = html_header_standard()
    htmlOutput += error_form_reading()
    return htmlOutput
  htmlOutput = html_header_standard()
  htmlOutput += game_restart(userScore,quoteText,quoteLink,quoteId,quoteDivId,quoteSrc,quoteHd)
  return htmlOutput

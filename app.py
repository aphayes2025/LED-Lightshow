'''
Author: Dylan Laberge and Aidan Hayes
CS 121 Final Project
Description: App.py is the Flask app that runs our project. It controls a WS2812B LED strip and allows it to do a bunch of different patters
'''

from turtle import color
from flask import Flask, render_template
import time  
import board
import neopixel
import sys
import random

# Use static_url_path to allow Flask to find the files in the static folder
app = Flask(__name__, static_url_path='/static')

# Dictionary of Colors and their respective rgb numbers to use in patterns
colors = {1: [255,0,0],     # Red
          2: [0,0,255],     # Blue
          3: [0,255,0],     # Green
          4: [255,155,0],   # Yellow
          5: [255,25,0],    # Orange
          6: [255,0,100],   # Pink
          7: [255,0,255],   # Purple
          8: [0,100,100]}   # Cyan

# Create baseline neopixel if one isnt created in a pattern with GPIO pin, num of LEDS and brightness
pixels = neopixel.NeoPixel(board.D18, 100, brightness=1)

# Creates a global boolean variable isTrue to be used in while loops
isTrue = False

# Turns all the LEDs Red
@app.route("/red_led_on", methods=["POST"])
def red_led_on_r():
    pixels.fill((colors[1][0], colors[1][1], colors[1][2])) # The function for filling all the LEDs on the strip with, in this case, red LEDs
    print("Red LED on")
    return "ok"

# Turns all the LEDs Blue
@app.route("/blue_led_on", methods=["POST"])
def blue_led_on_r():
    pixels.fill((colors[2][0], colors[2][1], colors[2][2]))
    print("Blue LED on")
    return "ok"

# Turns all the LEDs Green
@app.route("/green_led_on", methods=["POST"])
def green_led_on_r():
    pixels.fill((colors[3][0], colors[3][1], colors[3][2]))
    print("Green LED on")
    return "ok"

# Turns the global variable isTrue to False so while loops can be exited
@app.route("/effects_led_off", methods=["POST"])
def effects_led_off_r():
    global isTrue
    isTrue = False
    print("LED off")
    return "ok"

# If a pattern doesn't use a loop it turns off all the LEDs
@app.route("/led_off", methods=["POST"])
def led_off_r():
    pixels.fill((0,0,0))
    print("LED off")
    return "ok"

# Turns all the LEDs Yellow
@app.route("/yellow_led_on", methods=["POST"])
def yellow_led_on_r():
    pixels.fill((colors[4][0], colors[4][1], colors[4][2]))
    print("Yellow LED on")
    return "ok"

# Turns all the LEDs Orange
@app.route("/orange_led_on", methods=["POST"])
def orange_led_on_r():
    pixels.fill((colors[5][0], colors[5][1], colors[5][2]))
    print("Orange Led on")
    return "ok"

# Turns all the LEDs Pink
@app.route("/pink_led_on", methods=["POST"])
def pink_led_on_r():
    pixels.fill((colors[6][0], colors[6][1], colors[6][2]))
    print("Pink Led on")
    return "ok"

# Turns all the LEDs Purple
@app.route("/purple_led_on", methods=["POST"])
def purple_led_on_r():
    pixels.fill((colors[7][0], colors[7][1], colors[7][2]))
    print("Purple Led on")
    return "ok"

# Rainbow fills the whole strip with colors and looping through the colors
@app.route("/rainbow_led_on", methods=["POST"])
def rainbow_led_on_r():
    global isTrue
    isTrue = True
    while isTrue == True:
        # rainbow setting, having sleeps in between to make it look like transition
        # red
        pixels.fill((255, 0, 0))
        time.sleep(1.5)
        # orange
        pixels.fill((255, 25, 0))
        time.sleep(1.5)
        # yellow
        pixels.fill((255, 155, 0))
        time.sleep(1.5)
        # green
        pixels.fill((0, 255, 0))
        time.sleep(1.5)
        # blue
        pixels.fill((0, 0, 255))
        time.sleep(1.5)
        # purple
        pixels.fill((255, 0, 255))
        time.sleep(1.5)
        # pink
        pixels.fill((255, 0, 100))
        time.sleep(1.5)
    # Once the button is pressed again and isTrue is set to False, turns all LEDs off
    pixels.fill((0,0,0))
    print("Rainbow Led on")
    return "ok"

# Strobe lights switching from white to off rapidly on a loop
# CAUTION make sure no one around could be affected by this
@app.route("/strobe_led_on", methods=["POST"])
def strobe_led_on_r():
    global isTrue
    isTrue = True
    while isTrue == True:
        pixels.fill((255, 255, 255))
        time.sleep(0.05)
        pixels.fill((0,0,0))
        time.sleep(0.05)
    pixels.fill((0,0,0))
    print("Strobe Led on")
    return "ok"

# A Christmas themed pattern using red and green to create multiple effects per loop
@app.route("/christmas_chase_led_on", methods=["POST"])
def christmas_chase_led_on_r():
    pixels = neopixel.NeoPixel(board.D18, 100, brightness=1)
    global isTrue
    isTrue = True
    while isTrue:
        x = 50
        y = 49
        c = 0
        d = 50
        # While c is less than 49: c = 49, x = 99, y = 0, d = 50
        while c < 49:
            pixels[x] = (255, 0, 0)  # The function to change a single LED to a color
            pixels[y] = (0, 255, 0)
            x += 1
            y -= 1
            c += 1
            time.sleep(0.02)
        # While d is greater than 1: c = 49, x = 50, y = 49, d = 1
        while d > 1:
            pixels[x] = (0,255, 0)
            pixels[y] = (255, 0, 0)
            x -= 1
            y += 1
            d -= 1
            time.sleep(0.02)
        # While d is less than 24: c = 49, x = 98, y = 1, d = 24
        while d < 24:
            pixels[x] = (255,0,0)
            pixels[y] = (0,255,0)
            x += 2
            y -= 2
            d += 1
            time.sleep(0.04)
        # Loops through the entire strip making all of them green
        s = 1
        while s < 100:
            pixels[s] = (0,255,0)
            s +=1
            time.sleep(0.01)
        # Loops through the strip changing every other led red
        l = 1
        while l < 100:
            pixels[l] = (255,0,0)
            l += 2
            time.sleep(0.02)
    pixels.fill((0,0,0))
    print("Christmas Chase Led On")
    return "ok"

# Scroll starts at the end of the strip and changes the current LED to the color of the one before it making the colors go down the strip
@app.route("/scroll_led_on", methods=["POST"])
def scroll_led_on_r():
    pixels = neopixel.NeoPixel(board.D18, 100, brightness=1)
    global isTrue
    isTrue = True
    lastColor = 0
    while isTrue:
        numPixels = 99
        # Randomly generates a color from the range of the colors dictionary
        randColor = random.randint(1,8)
        # If it generates the color of the previous iteration it chooses a new color so it doesn't to the same color twice in a row
        while randColor == lastColor:
            randColor = random.randint(1,8)
       
        x = 1
        while x < 100:
            x += 1
            pixels[numPixels] = pixels[numPixels - 1] # Changes the current led to the one of the previous
            numPixels -= 1
       
        # Sets the first led of the strip to the color of the randomly generated color
        pixels[0] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])
       
        # Save the color to last color to compare on the next iteration
        lastColor = randColor
   
    pixels.fill((0,0,0))
    print("Scroll Led On")
    return "ok"

# Bar scroll is the same as Scroll but works in sections of 5 making the colors go by faster
@app.route("/bar_scroll_led_on", methods=["POST"])
def bar_scroll_led_on_r():
    pixels = neopixel.NeoPixel(board.D18, 100, brightness=1)
    global isTrue
    isTrue = True
    lastColor = 0
    while isTrue:
        numPixels = 99
        randColor = random.randint(1,8)
        while randColor == lastColor:
            randColor = random.randint(1,8)
       
        x = 1
        # Decrease the range of x as it moves in chunks of 5
        while x <= 95:
            x += 1
            pixels[numPixels] = pixels[numPixels - 5]
            numPixels -= 1
       
        # Set the first 5 leds to the color generated
        pixels[0] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])
        pixels[1] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])
        pixels[2] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])
        pixels[3] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])
        pixels[4] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])
       
        lastColor = randColor
   
    pixels.fill((0,0,0))
    print("Bar Scroll Led On")
    return "ok"

# Wave generates 2 random colors and runs down the strip with the first color and once it reaches the end comes back from the end with the second color
@app.route("/wave_led_on", methods=["POST"])
def wave_led_on_r():
    pixels = neopixel.NeoPixel(board.D18, 100, brightness=1)
    global isTrue
    isTrue = True
    lastColor = 0
    while isTrue:
        numPixels = 1
        randColor = random.randint(1,8)
        while randColor == lastColor:
            randColor = random.randint(1,8)
        randColor2 = random.randint(1,8)
        while randColor2 == randColor or randColor2 == lastColor:
            randColor2 = random.randint(1,8)

        pixels[0] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])

        x = 1
        while x < 100:
            x += 1
            pixels[numPixels] = pixels[numPixels - 1]
            numPixels += 1
            time.sleep(.02)
       
        pixels[numPixels - 1] = (colors[randColor2][0], colors[randColor2][1], colors[randColor2][2])
       
        x = 1
        while x < 100:
            x += 1
            pixels[numPixels-2] = pixels[numPixels - 1]
            numPixels -= 1
            time.sleep(.02)
       
        lastColor = randColor2
        #time.sleep(.01)
   
    pixels.fill((0,0,0))
    print("Scroll Led On")
    return "ok"

# Runs down the strip and randomly changes the color for every led
@app.route("/constant_random_led_on", methods=["POST"])
def constant_random_led_on():
    # max number of Leds + global vars
    x = 100
    global isTrue
    isTrue = True

    # global loop + inside for loop
    while isTrue == True:
        for i in range(x):
            # getting random value
            values = random.choice(list(colors.values()))
            pixels[i] = (values)
            time.sleep(0.05)
    pixels.fill((0,0,0))
    print("Constant Random Led On")
    return "ok"

# Rainbow flashes the colors of the rainbow along a small section of the LED strip
@app.route("/rainbow_pattern_led_on", methods=["POST"])
# for small amount of leds
def rainbow_pattern_led_on():
    # creating pixels video
    pixels = neopixel.NeoPixel(board.D18, 140, brightness=1)

    global isTrue
    isTrue = True

    while isTrue == True:
        # first 10 will look like normal rainbow
        # red
        pixels[1] = ((255, 0, 0))
        time.sleep(0.05)
        pixels[1] = ((0, 0, 0))
        # orange
        pixels[2] = ((255, 25, 0))
        time.sleep(0.05)
        pixels[2] = ((0, 0, 0))
        # yellow
        pixels[3] = ((255, 255, 0))
        time.sleep(0.05)
        pixels[3] = ((0, 0, 0))
        # green
        pixels[4] = ((0, 255, 0))
        time.sleep(0.05)
        pixels[4] = ((0, 0, 0))
        # blue
        pixels[5] = ((0, 0, 255))
        time.sleep(0.05)
        pixels[5] = ((0, 0, 0))
        # purple
        pixels[6] = ((255, 0, 255))
        time.sleep(0.05)
        pixels[6] = ((0, 0, 0))
        # pink
        pixels[7] = ((255, 0, 100))
        time.sleep(0.05)
        pixels[7] = ((0, 0, 0))
        # red
        pixels[8] = ((255, 0, 0))
        time.sleep(0.05)
        pixels[8] = ((0, 0, 0))
        # orange
        pixels[9] = ((255, 25, 0))
        time.sleep(0.05)
        pixels[9] = ((0, 0, 0))

        # go back but continue rainbow
        # yellow
        pixels[8] = ((255, 255, 0))
        time.sleep(0.05)
        pixels[8] = ((0, 0, 0))
        # green
        pixels[7] = ((0, 255, 0))
        time.sleep(0.05)
        pixels[7] = ((0, 0, 0))
        # blue
        pixels[6] = ((0, 0, 255))
        time.sleep(0.05)
        pixels[6] = ((0, 0, 0))
        # purple
        pixels[5] = ((255, 0, 255))
        time.sleep(0.05)
        pixels[5] = ((0, 0, 0))

        # keep going other way
        # pink
        pixels[6] = ((255, 0, 100))
        time.sleep(0.05)
        pixels[6] = ((0, 0, 0))
        # red
        pixels[7] = ((255, 0, 0))
        time.sleep(0.05)
        pixels[7] = ((0, 0, 0))
        # orange
        pixels[8] = ((255, 25, 0))
        time.sleep(0.05)
        pixels[8] = ((0, 0, 0))
        # yellow
        pixels[9] = ((255, 255, 0))
        time.sleep(0.05)
        pixels[9] = ((0, 0, 0))
        # green
        pixels[10] = ((0, 255, 0))
        time.sleep(0.05)
        pixels[10] = ((0, 0, 0))
        # blue
        pixels[11] = ((0, 0, 255))
        time.sleep(0.05)
        pixels[11] = ((0, 0, 0))
        # purple
        pixels[12] = ((255, 0, 255))
        time.sleep(0.05)
        pixels[12] = ((0, 0, 0))
        # pink
        pixels[13] = ((255, 0, 100))
        time.sleep(0.05)
        pixels[13] = ((0, 0, 0))
        # red
        pixels[14] = ((255, 0, 0))
        time.sleep(0.05)
        pixels[14] = ((0, 0, 0))
        # orange
        pixels[15] = ((255, 25, 0))
        time.sleep(0.05)
        pixels[15] = ((0, 0, 0))

    pixels.fill((0,0,0))
    print("Rainbow Pattern Led On")
    return "ok"

@app.route("/random_led_on", methods=["POST"])
def led_pattern():
    num_leds = 20
    # creating pixels video
    pixels = neopixel.NeoPixel(board.D18, num_leds, brightness=1)

    # counter + global vars
    x = 0
    global isTrue
    isTrue = True

    while isTrue == True:
        while x < 7:
            values = random.choice(list(colors.values()))
            pixels[x] = (values)
            time.sleep(0.05)
            pixels[x] = (0, 0, 0)
            x += 1
        while x > 5:
            values = random.choice(list(colors.values()))
            pixels[x] = (values)
            time.sleep(0.05)
            pixels[x] = (0, 0, 0)
            x -= 1
        while x < num_leds:
            values = random.choice(list(colors.values()))
            pixels[x] = (values)
            time.sleep(0.05)
            pixels[x] = (0, 0, 0)
            x += 1
        while 0 < x:
            values = random.choice(list(colors.values()))
            pixels[x - 1] = (values)
            time.sleep(0.05)
            pixels[x - 1] = (0,0,0)
            x -= 1
        pixels.fill((0,0,0))
        time.sleep(0.05)
    print("Random Led On")
    return "ok"

# Sparkle chooses 5 random leds and checks to make sure there isnt repeats. It flashes these chosen leds with random colors and turns them back off
@app.route("/sparkle_led_on", methods=["POST"])
def sparkle_led_on_r():
    numPixels = 100
    pixels = neopixel.NeoPixel(board.D18, numPixels, brightness=1)
    global isTrue
    isTrue = True
    while isTrue:

        randPixel1 = random.randint(0, numPixels - 1)
        randPixel2 = random.randint(0, numPixels - 1)
        while randPixel1 == randPixel2:
            randPixel2 = random.randint(0, numPixels - 1)
        randPixel3 = random.randint(0, numPixels - 1)
        while randPixel3 == randPixel1 or randPixel3 == randPixel2:
            randPixel3 = random.randint(0, numPixels - 1)
        randPixel4 = random.randint(0, numPixels - 1)
        while randPixel4 == randPixel1 or randPixel4 == randPixel2 or randPixel4 == randPixel3:
            randPixel4 = random.randint(0, numPixels - 1)
        randPixel5 = random.randint(0, numPixels - 1)
        while randPixel5 == randPixel1 or randPixel5 == randPixel2 or randPixel5 == randPixel3 or randPixel5 == randPixel4:
            randPixel4 = random.randint(0, numPixels - 1)


        randColor = random.randint(1,8)
        pixels[randPixel1] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])
       
        time.sleep(.2)
       
        pixels[randPixel1] = (0, 0, 0)
        randColor = random.randint(1,8)
        pixels[randPixel2] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])

        time.sleep(.2)

        pixels[randPixel2] = (0, 0, 0)
        randColor = random.randint(1,8)
        pixels[randPixel3] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])

        time.sleep(.2)

        pixels[randPixel3] = (0, 0, 0)
        randColor = random.randint(1,8)
        pixels[randPixel4] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])
   
        time.sleep(.2)

        pixels[randPixel4] = (0, 0, 0)
        randColor = random.randint(1,8)
        pixels[randPixel5] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])
   
        time.sleep(.2)
        pixels[randPixel5] = (0, 0, 0)
   
    pixels.fill((0,0,0))
    print("Sparkle Led On")
    return "ok"

# Wave 2 creates a section of 6 leds and picks a random color and runs down the led strip with them turning off the leds behind it
@app.route("/wave2_led_on", methods=["POST"])
def wave2_led_on_r():
    pixels = neopixel.NeoPixel(board.D18, 100, brightness=1)
    global isTrue
    isTrue = True
    lastColor = 0
    while isTrue:
        numPixels = 99

        randColor = random.randint(1,8)
        while randColor == lastColor:
            randColor = random.randint(1,8)

        pixels[0] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])
       
        x = 1
        while x < numPixels:
            pixels[x] = (colors[randColor][0], colors[randColor][1], colors[randColor][2])
            if(x > 5):
                pixels[x - 6] = (0, 0, 0)
            x += 1
            time.sleep(.02)

        pixels[x - 6] = (0, 0, 0)
        time.sleep(.02)
        pixels[x - 5] = (0, 0, 0)
        time.sleep(.02)
        pixels[x - 4] = (0, 0, 0)
        time.sleep(.02)
        pixels[x - 3] = (0, 0, 0)
        time.sleep(.02)
        pixels[x - 2] = (0, 0, 0)
        time.sleep(.02)
        pixels[x - 1] = (0, 0, 0)
        time.sleep(.02)
        pixels[x] = (0, 0, 0)
        lastColor = randColor

    pixels.fill((0,0,0))
    print("Wave2 Led On")
    return "ok"

# Fill Three is a pattern using red green and blue lights that chase eachother across the strip
@app.route("/fill_three_led_on", methods=["POST"])
def three_led_fill():
    num_leds = 100
    # creating pixels video
    pixels = neopixel.NeoPixel(board.D18, num_leds, brightness=1)

    # counter + global vars
    global isTrue
    isTrue = True
    x = 1
    y = 50
    z = 100
    while isTrue == True:
        # after x = 10, y = 0, z = 10
        while x < 50:
            pixels[x - 1] = (colors[1][0], colors[1][1], colors[1][2])
            pixels[y - 1] = (colors[2][0], colors[2][1], colors[2][2])
            pixels[z - 1] = (colors[3][0], colors[3][1], colors[3][2])
            x += 1
            y -= 1
            z -= 1
            time.sleep(0.05)
        # after x = 20, y = 10, z = 0
        while x < 100:
            pixels[x - 1] = (colors[1][0], colors[1][1], colors[1][2])
            pixels[y - 1] = (colors[2][0], colors[2][1], colors[2][2])
            pixels[z - 1] = (colors[3][0], colors[3][1], colors[3][2])
            x += 1
            y += 1
            z -= 1
            time.sleep(0.05)
        # after x = 10, y = 20, z = 10
        while y < 100:
            pixels[x - 1] = (colors[1][0], colors[1][1], colors[1][2])
            pixels[y - 1] = (colors[2][0], colors[2][1], colors[2][2])
            pixels[z - 1] = (colors[3][0], colors[3][1], colors[3][2])
            x -= 1
            y += 1
            z += 1
            time.sleep(0.05)
        # after x = 0, y = 10, z = 20
        while z < 100:
            pixels[x - 1] = (colors[1][0], colors[1][1], colors[1][2])
            pixels[y - 1] = (colors[2][0], colors[2][1], colors[2][2])
            pixels[z - 1] = (colors[3][0], colors[3][1], colors[3][2])
            x -= 1
            y -= 1
            z += 1
            time.sleep(0.05)
    pixels.fill((0,0,0))
    print("Fill Three Led On")
    return "ok"

# Chase Three is the same as Fill Three however it turns off the leds after leaving it
@app.route("/chase_three_led_on", methods=["POST"])
def three_led_chase():
    num_leds = 20
    # creating pixels video
    pixels = neopixel.NeoPixel(board.D18, num_leds, brightness=1)

    # counter + global vars
    global isTrue
    isTrue = True
    x = 1
    y = 10
    z = 20
    while isTrue == True:
        # after x = 10, y = 0, z = 10
        while x < 10:
            pixels[x - 1] = (colors[1][0], colors[1][1], colors[1][2])
            pixels[y - 1] = (colors[2][0], colors[2][1], colors[2][2])
            pixels[z - 1] = (colors[3][0], colors[3][1], colors[3][2])
            time.sleep(0.1)
            pixels[x - 1] = (0,0,0)
            pixels[y - 1] = (0,0,0)
            pixels[z - 1] = (0,0,0)
            x += 1
            y -= 1
            z -= 1

        # after x = 20, y = 10, z = 0
        while x < 20:
            pixels[x - 1] = (colors[1][0], colors[1][1], colors[1][2])
            pixels[y - 1] = (colors[2][0], colors[2][1], colors[2][2])
            pixels[z - 1] = (colors[3][0], colors[3][1], colors[3][2])
            time.sleep(0.1)
            pixels[x - 1] = (0, 0, 0)
            pixels[y - 1] = (0, 0, 0)
            pixels[z - 1] = (0, 0, 0)
            x += 1
            y += 1
            z -= 1
            time.sleep(0.05)
        # after x = 10, y = 20, z = 10
        while y < 20:
            pixels[x - 1] = (colors[1][0], colors[1][1], colors[1][2])
            pixels[y - 1] = (colors[2][0], colors[2][1], colors[2][2])
            pixels[z - 1] = (colors[3][0], colors[3][1], colors[3][2])
            time.sleep(0.1)
            pixels[x - 1] = (0, 0, 0)
            pixels[y - 1] = (0, 0, 0)
            pixels[z - 1] = (0, 0, 0)
            x -= 1
            y += 1
            z += 1
            time.sleep(0.05)
        # after x = 0, y = 10, z = 20
        while z < 20:
            pixels[x - 1] = (colors[1][0], colors[1][1], colors[1][2])
            pixels[y - 1] = (colors[2][0], colors[2][1], colors[2][2])
            pixels[z - 1] = (colors[3][0], colors[3][1], colors[3][2])
            time.sleep(0.1)
            pixels[x - 1] = (0, 0, 0)
            pixels[y - 1] = (0, 0, 0)
            pixels[z - 1] = (0, 0, 0)
            x -= 1
            y -= 1
            z += 1
            time.sleep(0.05)
    pixels.fill((0,0,0))
    print("Chase Three Led On")
    return "ok"

# Gradient is similar to rainbow however it changes colors much slower and smoother going through the whole rgb range
@app.route("/gradient_led_on", methods=["POST"])
def gradient_led_on_r():
    num_leds = 100
    # creating pixels video
    pixels = neopixel.NeoPixel(board.D18, num_leds, brightness=1)

    # counter + global vars
    global isTrue
    isTrue = True
    red = 250
    green = 0
    blue = 0
    while isTrue == True:
        # start with red full, decrease red increase green
        while red > 0:
            pixels.fill((red, green, blue))
            red -= 10
            green += 10
            time.sleep(.1)
        # Once green fills up, decrease green increase blue
        while green > 0:
            pixels.fill((red, green, blue))
            green -= 10
            blue += 10
            time.sleep(.1)
        # Once blue fills up, decrease blue increase red
        while blue > 0:
            pixels.fill((red, green, blue))
            blue -= 10
            red += 10
            time.sleep(.1)

    pixels.fill((0,0,0))
    print("Chase Three Led On")
    return "ok"



@app.route("/", methods=["GET"])
def home():
    return render_template("button.html", title="LED LightShow", name="Aidan Hayes")

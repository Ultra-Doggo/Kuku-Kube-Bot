import PIL.ImageGrab, pyautogui, pyscreeze, time, sys
from collections import Counter

# these 2d list "pixel coordinates" hold the
# center of each squares, depending how many are on screen
# they're hardcoded to work on a 15.4-inch, 2880x1800 pixel display
two = []
for x in [580, 1080]:
    for y in [930, 1430]:
        two.append((x, y))

three = []
for x in [500, 820, 1140]:
    for y in [840, 1160, 1480]:
        three.append((x, y))

four = []
for x in [460, 700, 940, 1180]:
    for y in [810, 1050, 1290, 1530]:
        four.append((x, y))

five = []
for x in [440, 640, 840, 1040, 1240]:
    for y in [770, 970, 1170, 1370, 1570]:
        five.append((x, y))

six = []
for x in [420, 584, 748, 912, 1076, 1240]:
    for y in [764, 928, 1092, 1256, 1420, 1584]:
        six.append((x, y))

seven = []
for x in [410, 550, 690, 830, 970, 1110, 1250]:
    for y in [750, 890, 1030, 1170, 1310, 1450, 1590]:
        seven.append((x, y))

eight = []
for x in [400, 525, 650, 775, 900, 1025, 1150]:
    for y in [740, 865, 990, 1115, 1240, 1365, 1490, 1615]:
        eight.append((x, y))

nine = []
for x in [395, 505, 615, 725, 835, 945, 1055, 1165, 1275]:
    for y in [735, 845, 955, 1065, 1175, 1285, 1395, 1505, 1615]:
        nine.append((x, y))


# function to take a temporary screenshot @ each new set of squares,
# and add each pixel color to a color_list list
def process(dimension):
    im = pyscreeze.screenshot()
    color_list = []

    if (dimension == 2):
        for i in two:
            color_list.append(im.getpixel(i))
        tell_diff(color_list, two)
            
    elif (dimension == 3):
        for i in three:
            #print(im.getpixel(i))
            color_list.append(im.getpixel(i))
        tell_diff(color_list, three)

    elif (dimension == 4):
        for i in four:
            #print(im.getpixel(i))
            color_list.append(im.getpixel(i))
        tell_diff(color_list, four)

    elif (dimension == 5):
        for i in five:
            #print(im.getpixel(i))
            color_list.append(im.getpixel(i))
        tell_diff(color_list, five)

    elif (dimension == 6):
        for i in six:
            #print(im.getpixel(i))
            color_list.append(im.getpixel(i))
        tell_diff(color_list, six)

    elif (dimension == 7):
        for i in seven:
            #print(im.getpixel(i))
            color_list.append(im.getpixel(i))
        tell_diff(color_list, seven)

    elif (dimension == 8):
        for i in eight:
            #print(im.getpixel(i))
            color_list.append(im.getpixel(i))
        tell_diff(color_list, eight)

    elif (dimension == 9):
        for i in nine:
            #print(im.getpixel(i))
            color_list.append(im.getpixel(i))
        tell_diff(color_list, nine)


# this calls find_color_pos
def tell_diff(color_list, pixel_list):
    print("Analysing pixel info ... ")
    print(color_list)

    print("Searching for diff. pixel ... ")
    cnt = Counter()

    for clr in color_list:
            cnt[clr] += 1

    print(cnt)

    for item in cnt:
        if (cnt[item] == 1):
                print("different pixel =", item)
                color_to_click = item
                find_color_pos(color_to_click, color_list, pixel_list)


def find_color_pos(color_to_click, color_list, pixel_list):
        for clr in color_list:
                if (color_to_click == clr):
                        index = color_list.index(clr)
                        print("diff pixel index:", index)

        # now we should call the function that will lead us
        # to clicking the color from this list index position
        click_at_index(index, pixel_list)


def click_at_index(index, pixel_list):
        print("Now to click correct index ...")

        pixel_location = pixel_list[index]
        print("pixel location =", pixel_location)

        click_location = [x / 2 for x in pixel_location]
        print("click location =", click_location)

        pyautogui.click(click_location)


def switchApp():
    pyautogui.keyDown('command')
    time.sleep(0.05)
    pyautogui.press('tab')
    pyautogui.keyUp('command')
    # warning : make sure that broswer is 2nd most recently used,
    # and occupies the left half of your display


# switches to the browser and clicks the start button
def start():
    switchApp()
    # the x's and y's represent where on screen to
    # click & drag the mouse, in order to press the start button
    pyautogui.mouseDown(button='left', x=720/2, y=1180/2)
    pyautogui.mouseUp(button='left', x=710/2, y=1170/2)
    
    # refresh the webpage before running script again - the replay button is
    # in a different location than the regular start button


def main():
    start()
    time.sleep(0.5)

    # argument tells us how many squares currently on screen
    # this is ALWAYS the pattern for the game. 2x2, 3x3, 4x4, etc
    process(2)
    process(3)
    process(4)

    process(5)
    process(5)

    process(6)
    process(6)

    process(7)
    process(7)
    process(7)

    '''
    process(8)
    process(8)
    process(8)
    process(8)
    process(8)
    process(8)
    process(8)
    '''


    for i in range(0, 6):
        process(8)

    for i in range(0, 98):
        process(9)


# run the script
main()
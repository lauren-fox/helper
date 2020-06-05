import colorsys

# adjust the canvas size here
size(1175,1500)

def hue(r, g, b, v):
    h, s, v = colorsys.rgb_to_hsv(r,g,b)
    h = h * v
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return r, g, b
    
    
# path to the image
path = "/Users/laurenfox/Desktop/F3420018.JPG"

# get the size of the image
w, h = imageSize(path)

# change this value to increase or decrease 
# the number of pixels
s = 15

# loop over the width of the image
for x in range(0, w, s):
    
    # loop of the height of the image
    for y in range(0, h, s):
        
        # get the color
        # adjust the size values of the oval and rect to 
        # increase the size of the pixels 
        color = imagePixelColor(path, (x, y))
        if color:
            r, g, b, a = color
            fill(r, g, b, a)
            oval(x,y,8.5,8.5)
            r, g, b = hue(r, g, b, 12500)
            fill(r,g,b,a)
            rect(x,y,-7.5,-7.5)

# name the image file            
saveImage("~/Desktop/untitled.png")

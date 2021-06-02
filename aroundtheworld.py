from PIL import  Image
me = Image.open('love.png')
bgs = Image.open('go.jpg')
bgs.paste(me,(0,0),me)
bgs.show()

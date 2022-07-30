import json
import PIL.Image as image

img = image.open('./test.png')
with open('./test.json', "r") as f:
    dirs = json.load(f)["frames"]
    for i in dirs:
        name = i['filename']
        frame = i['frame']
        box = (frame['x'], frame['y'], frame['x']+frame['w'], frame['y']+frame['h'])
        print(name, ': ', box)
        newImage = img.crop(box)
        newImage.save('./output/'+name+'.png')



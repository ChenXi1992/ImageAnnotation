import os
from PIL import Image
cutSize = 37.5  # When the pic size is 75 x 75


class ImageIteration:
    count = 1
    fileDir = "static/Rendered_img"
    saveDir = "static/Solor_panel"
    classifiedDir = "static/Classified_img"

    os.makedirs(saveDir, exist_ok=True)
    os.makedirs(classifiedDir,exist_ok = True)


    totalImgs = sorted(os.listdir(fileDir))

def cut_by_point(data,dir):

    pic_path = data["pic"]
    x_val = data["x"]
    y_val = data["y"]

    x_val = int(x_val)
    y_val = int(y_val)
    
    #    Save the pic 
    
    pil_im = Image.open(pic_path)

    print("The pic that cutting is {}".format(pic_path))
    width,height = pil_im.size

    left = x_val - cutSize
    upper = y_val - cutSize
    right = x_val + cutSize
    lower = y_val + cutSize

    pic_name = pic_path.split("/")[-1]

    
    # left = max(0,x_val-cutSize)
    # upper = max(0,y_val -cutSize)
    # right = min(x_val + cutSize,width)
    # lower = min(y_val + cutSize,height)

    savePath = dir + '/' +  pic_name[:-4] + '_' + 'x_'+ str(x_val) + '_y_' +  str(y_val) +  '.png'

    print("Saving pic")
    
    pil_im.crop((left,upper,right,lower)).save(savePath)
    

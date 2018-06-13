
# coding: utf-8

# In[1]:
from flask import Flask,render_template
from flask import request
from flask import jsonify, url_for
import os
from cutImage  import cut_by_point,ImageIteration
import shutil


app = Flask(__name__)

img = ImageIteration()


@app.route('/')



def display_web():
    return render_template('pic.html')

@app.route('/cutPic/', methods = ['POST','GET'])

def get_data():
    name = request.args.get('pic_no')
    if name[0] == "/":
        name = name[1:]
    x_val = request.args.get('x')
    y_val = request.args.get('y')

    print("the pic name is {}".format(name))

    cut_by_point({"pic":name,"x":x_val,"y":y_val},img.saveDir)

    return jsonify({'results':'Sucessfully'})


@app.route('/img/', methods = ['POST','GET'])

def get_img():

    path = img.fileDir + '/' +  img.totalImgs[img.count]

    if img.count > 1:
        shutil.move(img.fileDir+'/'+ img.totalImgs[img.count-1], img.classifiedDir + '/' + img.totalImgs[img.count-1])

    img.count += 1

    print(img.count)


    return jsonify({'url':path})

if __name__ == '__main__':

	app.debug = True
	app.run(host = 'localhost',port = 4000)

from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
import urllib.request
from PIL import Image


app = Flask(__name__,  template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    image_url = request.form['image_url']
    img = Image.open(urllib.request.urlopen(image_url))
    img = img.resize((256,256))
    img = np.reshape(img,[1,256,256,3])
    img = img.astype('float32')
    img /= 255.0
    model = load_model('artifacts.h5')


    class_names = ['This artifact comes from Ancient Greece!', 'This is a prehistoric artifact!', 'This is a Renaissance era piece!']
    prediction = class_names[model.predict_classes(img)[0]]

    return render_template('result.html', prediction=prediction)



if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 4000
    app.run(HOST, PORT)

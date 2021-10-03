from flask import render_template, request
import os
import numpy as np
from utils import classify
from PIL import Image
from io import BytesIO
import base64
import cv2
import warnings
warnings.filterwarnings("ignore")


def index():
    if request.method == 'POST':

        # FileStorage object wrapper
        image = request.files['image']
        if image:
            try:
                pil_img = Image.open(image)
                # print(pil_img)
                cv_img = np.array(pil_img)

                print(cv_img.dtype, "///////////")
                result = classify(cv_img)

                print("done")
                if result == 0:
                    decision = "cancer detected"
                else:
                    decision = "cancer not detected <3"
                data = BytesIO()
                pil_img.save(data, "JPEG")
                encoded_img_data = base64.b64encode(data.getvalue())
                img_data = encoded_img_data.decode('utf-8')
                return render_template("index.html", result=decision, image=img_data)
            except Exception as e:
                print(e, "\nunsuccessful", cv_img.shape)

    return render_template("index.html")

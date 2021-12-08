from flask import render_template, request
import os
import numpy as np
from utils import classify
from PIL import Image
from io import BytesIO
import base64
import cv2
from datetime import date
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
                db_add(result)
                print("done")
                if result == 0:
                    decision = "cancer detected"
                else:
                    decision = "cancer not detected <3"
                data = BytesIO()
                pil_img.save(data, "JPEG")
                encoded_img_data = base64.b64encode(data.getvalue())
                img_data = encoded_img_data.decode('utf-8')
                return render_template("index.html", result=decision, image=img_data, count=result_db_count())
            except Exception as e:
                print(e, "\nunsuccessful", cv_img.shape)

    return render_template("index.html", count=result_db_count())


def db_add(result):
    from app import Data, db
    today = date.today()
    today = today.strftime("%b-%d-%Y")
    data = Data(date=today, result=result)
    db.session.add(data)
    db.session.commit()


def db_read():
    from app import Data, db
    all = Data.query.all()
    print(all)


def result_db_count():
    from app import Data, db
    try:
        all = Data.query.all()
        return len(all)
    except:
        return "many"

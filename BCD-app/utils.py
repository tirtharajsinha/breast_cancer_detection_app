from keras.models import model_from_json
import cv2
import numpy as np
from PIL import Image
import imutils


def classify(cv_img):
    # img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    print(cv_img.dtype, "/////////////////////////")
    test_img = prepare_image_target(cv_img)
    model = loaddata()
    test_pred = model.predict_on_batch(test_img)
    return np.argmax(test_pred)


def prepare_image_target(img):
    try:
        img = crop_contour_img(img)
        img = cv2.resize(img, (128, 128))
    except:
        img = Image.fromarray(img)
        img = np.array(img.convert("RGB"))
        img = cv2.resize(img, (128, 128))

    img = np.array(img)
    img = img.reshape(1, 128, 128, 3)
    return img


def loaddata():
    json_file = open('static/model/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("static/model/model.h5")
    return loaded_model


def crop_contour_img(image):

    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayscale = cv2.GaussianBlur(grayscale, (5, 5), 0)
    threshhold_image = cv2.threshold(grayscale, 50, 255, cv2.THRESH_BINARY)[1]
    threshhold_image = cv2.erode(threshhold_image, None, iterations=3)
    threshhold_image = cv2.dilate(threshhold_image, None, iterations=3)

    countour = cv2.findContours(
        threshhold_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    countour = imutils.grab_contours(countour)
    c = max(countour, key=cv2.contourArea)

    extreme_pnts_left = tuple(c[c[:, :, 0].argmin()][0])
    extreme_pnts_right = tuple(c[c[:, :, 0].argmax()][0])
    extreme_pnts_top = tuple(c[c[:, :, 1].argmin()][0])
    extreme_pnts_bot = tuple(c[c[:, :, 1].argmax()][0])

    new_image = image[extreme_pnts_top[1]:extreme_pnts_bot[1],
                      extreme_pnts_left[0]:extreme_pnts_right[0]]
    new_image = cv2.threshold(
        new_image, 65, 255, cv2.THRESH_BINARY, cv2.CHAIN_APPROX_SIMPLE)[1]
    new_image = cv2.bitwise_not(new_image)

    return new_image

import urllib.request
import cv2
import json
import pyzbar.pyzbar as pyzbar
import numpy as np
import time
import calendar
import requests
def decode(im):
    decodedObjects = pyzbar.decode(im)
    if decodedObjects:
        params = {
            "qrstring": str((decodedObjects[0].data).decode('utf-8'))
        }
        validapiresponse = requests.get(url="https://q8ros48qra.execute-api.ap-south-1.amazonaws.com/default/0802validate/qrstringvalidate", params=params)
        json_data = json.loads(validapiresponse.text)
        if json_data['body'] == 'VALID':
            timestamp = calendar.timegm(time.gmtime())
            params = {
                "timestamp": timestamp,
                "qrstring": (decodedObjects[0].data).decode('utf-8')
            }
            response = requests.get(url="https://ictwi7jcc2.execute-api.ap-south-1.amazonaws.com/sec/0802/insert",params=params)
        # time.sleep(1)
        print((decodedObjects[0].data).decode('utf-8') + " was "+json_data['body'])
        return (decodedObjects[0].data).decode('utf-8')

url = 'http://192.168.5.80:8080/shot.jpg'

while True:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    cv2.imshow('test', img)
    myqrstring = decode(img)
    # timestamp = str(calendar.timegm(time.gmtime()))

    if ord('q') == cv2.waitKey(10):
        exit(0)
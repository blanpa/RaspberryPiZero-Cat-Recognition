# import tensorflow.keras
from tflite_runtime.interpreter import Interpreter

from PIL import Image, ImageOps
import numpy as np
from io import BytesIO
from time import sleep
from picamera import PiCamera
from time import sleep
import logging
from datetime import datetime
import os
import telegram


botToken = ""
bot = telegram.Bot(token=botToken)
chat_id = ""

logging.basicConfig(filename='logs.log', filemode='w', level=logging.DEBUG) 

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load cam
camera = PiCamera() 
camera.rotation = 90

logging.debug("START")

f = 0

while True:
    sleep(1)
    my_stream = BytesIO()
    camera.start_preview()
    sleep(1)
    camera.capture(my_stream, 'jpeg') 
    camera.stop_preview()
    image = Image.open(my_stream)
    imageresize = image.resize((224, 224), Image.LANCZOS)
    imageasarray = np.asarray(imageresize)

    # data = image.reshape(1, 224,224,3)

    interpreter = Interpreter(model_path="model/model.tflite")
    interpreter.allocate_tensors()

    # input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    input_tensor= np.array(np.expand_dims(imageasarray, 0), dtype=np.float32)
    input_index = interpreter.get_input_details()[0]["index"]
    interpreter.set_tensor(input_index, input_tensor)
    #Run the inference
    interpreter.invoke()
    output_details = interpreter.get_output_details()[0]
    
    prediction = interpreter.get_tensor(output_details['index']).tolist()[0]
    index = prediction.index(max(prediction))
    now = datetime.now().time() # time 

    logs = f"time: {now} class: {index} prediction: {prediction[index]}" 

    print(logs)
    logging.debug(logs)

    # if index == 0:
    #     path = os.path.join("data", "predicted",f"b{np.random.randint(100000)}.jpg")
    #     image.save(path, quality=80, optimize=True, progressive=True)
    #     pass

    if index == 0:
        pass

    if index == 1:
        path = os.path.join("data", "predicted") + f"c{f}.jpg"
        f+=1
        image.save(path, quality=80, optimize=True, progressive=True)
        bot.send_photo(chat_id=chat_id, caption= f"time: {now} class: {index} prediction: {prediction[index]}", photo=open(path, 'rb'))
        
    
    if index == 2:
        path = os.path.join("data", "predicted") + f"c{f}.jpg"
        f+=1
        image.save(path, quality=80, optimize=True, progressive=True)
        bot.send_photo(chat_id=chat_id, caption= f"time: {now} class: {index} prediction: {prediction[index]}", photo=open(path, 'rb'))


    if index == 3:
        pass


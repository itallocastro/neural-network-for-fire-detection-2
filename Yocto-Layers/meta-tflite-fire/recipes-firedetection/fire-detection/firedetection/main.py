import tflite_runtime.interpreter as tflite
import cv2
import numpy as np
import pathlib
import glob
import sys

def get_camera_index():
    camIndex = [int(vi.split("/")[-1][5:]) for vi in glob.glob("/dev/video*")]
    for ci in camIndex:
        try:
            cap = cv2.VideoCapture(ci)
            ret, frame = cap.read()
            cap.release()
            if ret == True:
                return ci
        except:
            pass
    return None 

def set_input_tensor(interpreter, image):
    tensor_index = interpreter.get_input_details()[0]['index']
    input_tensor = interpreter.tensor(tensor_index)()[0]
    input_tensor[:, :] = image

def bgr2rgb(img):
  return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def classify_image(interpreter, image):
    set_input_tensor(interpreter, image)
    interpreter.invoke()
    output_details = interpreter.get_output_details()[0]
    output = np.squeeze(interpreter.get_tensor(output_details['index']))
    img_pred = 0 if output <= 0.5 else 1
    return img_pred


def main(argv=None):
    if argv is None:
        argv = sys.argv

    print("Getting interpreter")
    interpreter = tflite.Interpreter("./model.tflite")
    interpreter.allocate_tensors()

    print("Getting camera")
    cindex = get_camera_index()
    if cindex is None:
        print("Camera not found")
        return 0
    print(f"Camera at {cindex}")
    cap = cv2.VideoCapture(cindex)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == False:
            break
        img = cv2.resize(frame, (256, 256), interpolation=cv2.INTER_AREA)
        img = bgr2rgb(img)
        res = classify_image(interpreter, img)
        print(f"Fire {'not ' if res < 0.5 else ''}detected.")

    cap.release()
    cv2.destroyAllWindows()

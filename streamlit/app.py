import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image



def detect_objects(our_image):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.subheader("Detected object with box and confidence :")
    net = cv2.dnn.readNet("./scripts/yolov4-custom_2000.weights", "./scripts/yolov4-custom.cfg")

    classes = []
    with open("./scripts/coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]

    

    # LOAD THE IMAGE
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img,1)
    height,width,channels = img.shape


    # DETECTING OBJECTS (CONVERTING INTO BLOB)
    blob = cv2.dnn.blobFromImage(img, 0.00392, (608,608), (0,0,0), True, crop = False)   #(image, scalefactor, size, mean(mean subtraction from each layer), swapRB(Blue to red), crop)

    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes =[]

    # SHOWING INFORMATION CONTAINED IN 'outs' VARIABLE ON THE SCREEN
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)  
            confidence = scores[class_id] 
            if confidence > 0.5:   
                # OBJECT DETECTED
                #Get the coordinates of object: center,width,height  
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)  #width is the original width of image
                h = int(detection[3] * height) #height is the original height of the image

                # RECTANGLE COORDINATES
                x = int(center_x - w /2)   #Top-Left x
                y = int(center_y - h/2)   #Top-left y
                
                #To organize the objects in array so that we can extract them later
                boxes.append([x,y,w,h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    score_threshold = st.sidebar.slider("Confidence Threshold", 0.00,1.00,0.5,0.01)
    nms_threshold = st.sidebar.slider("NMS Threshold", 0.00, 1.00, 0.4, 0.01)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences,score_threshold,nms_threshold)      

    colors = np.random.uniform(0,255,size=(len(confidences), 3))  
    font = cv2.FONT_HERSHEY_SIMPLEX
    items = []
    for i in range(len(boxes)):
        if i in indexes:
            x,y,w,h = boxes[i]
            #To get the name of object 
            label = str.upper((classes[class_ids[i]]))   
            color = colors[i]
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)     
            items.append(label)
            text = "{}: {:.4f}".format(classes[class_ids[i]], confidences[i])
            cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,1.5, color, 2)
            print(f'this is i = {i}')

    st.image(img,width = 600)

def object_main():
    """Fruit Object Detection APP"""

    st.title("Fruit Object Detection")
    # st.write("Object detection is a central algorithm in computer vision. The algorithm implemented below is YOLO (You Only Look Once), a state-of-the-art algorithm trained to identify thousands of objects types. It extracts objects from images and identifies them using OpenCV and Yolo. This task involves Deep Neural Networks(DNN), yolo trained model, yolo configuration and a dataset to detect objects.")

    choice = st.radio("", ("Show Demo", "Browse an Image"))
    st.write()

    if choice == "Browse an Image":
        st.set_option('deprecation.showfileUploaderEncoding', False)
        image_file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])

        if image_file is not None:
            our_image = Image.open(image_file)  
            detect_objects(our_image)

    elif choice == "Show Demo":
        our_image = Image.open("./../explore/testImages/banana_holding.jpg")
        detect_objects(our_image)

if __name__ == '__main__':
    object_main()
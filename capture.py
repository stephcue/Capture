#Senior Design AMPD capture definition
#uses OpenCV 2.4.2, Python 2.7, Raspberry Pi3, and Pi Camera module v2

import imutils
import cv2
from imutils.video import VideoStream

def capture():
    size = 4
    vs = VideoStream(usePiCamera= 1).start()
    time.sleep(2.0)

    #loading the xml file
    classifier = cv2.CascadeClassifier('pill_classifier.xml')
    sampleNum = 0

    while True:
        frame = vs.read()

        # Resizing to speed up detection
        mini = cv2.resize(frame, (frame.shape[1] / size, frame.shape[0] / size))

        # detecting using classifier
        pills = classifier.detectMultiScale(mini)

        # Drawing rectangles around each pill
        for p in pills:
            (x, y, w, h) = [v * size for v in p] #Scale the shapesize backup
            cv2.rectangle(frame, (x, y), (x + w, y + h),(0,255,0),thickness=4)
            
            #Saving the images and incrementing counter
            sampleNum = sampleNum + 1
            sub_pill = frame[y:y+h, x:x+w]
            
            PillFileName = "data/pill_detected" + str(sampleNum) + ".jpg"
            cv2.imwrite(PillFileName, sub_pill)

        #Display captured image
        cv2.imshow('img', frame)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
        # break if the sample number is more than 30
        elif sampleNum > 29:
            break
    vs.quit()
    cv2.destroyAllWindows()

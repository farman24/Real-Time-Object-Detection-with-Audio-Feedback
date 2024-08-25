import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

video = cv2.VideoCapture(1)
labels = []


def playSound(text):
    output = gTTS(text=text,lang= "en",slow=False)
    output.save(".\sounds\output.mp3")
    playsound(".\sounds\output.mp3")

while True:
    ret, frame = video.read()  # capturing each frame from video
    bbox, label, conf = cv.detect_common_objects(frame)  # draws box around the objects with an label
    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Objectdetection", output_image)  # should the image to user
    for i in label:
        if i not in labels:
            labels.append(i)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
go = True
newSentence = []
for i in labels:

    if go:
        newSentence.append("There is a " + i)
        go = False
    else:
        newSentence.append("an " + i)
playSound((" ").join(newSentence))

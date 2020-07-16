import pytesseract
from pytesseract import Output
from PIL import Image
import cv2

cap = cv2.VideoCapture(0)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe' # path

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    # txt = pytesseract.image_to_string(img) # if you want to print text which is detected thru camera.
    # print(txt)

    data = pytesseract.image_to_data(frame, output_type=Output.DICT)

    boxes = len(data['text'])
    for i in range(boxes):
        if int(data['conf'][i]) > 70:
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(frame, data['text'][i], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)


    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
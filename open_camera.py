import cv2

cascada = cv2.CascadeClassifier("C:/Users/ebarr/Desktop/haarcascade_frontalface_alt.xml")
   
captura = cv2.VideoCapture(0)

while(True):
    ret, frame = captura.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
    
    cv2.imshow('Frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
cv2.destroyAllWindows()
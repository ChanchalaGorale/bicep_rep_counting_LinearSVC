import cv2 

class Camera:

    def __init__(self):

        self.camera = cv2.VideoCapture(0)
        
        if not self.camera.isOpened():
            print("Cannot open camera")
            exit()
        
        self.width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
    def __del__(self):
        if  self.camera.isOpened():
            self.camera.release()

    def get_frame(self):
        if not self.camera.isOpened():
            ret, frame =  self.camera.read()

            if ret:
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RBG)
            else:
                return None, None
        else:
                return None, None
            

    


         
           




import cv2
import numpy as np



class Raise_region:
    """Here we raise region on threshold picture.
    Thank to that we can contourn false detections from
    anatomy part of the face.

    For that we must determin region from DLIB points for have
    coordinates. Sometimes we must increment region from the
    head region.

    Indeed we recuperate feature of the wrinkle from the treshold
    picture.
    
    """

    def __init__(self, landmarks, picture, head_box,
                 points_list, adding_height, add_width, frame):

        """Importing landmarks from DLIB, the picture (threshold),
        who can be adaptativ (11, 2), (3, 5),
        the head box include in a box,
        our list points choosen from DLIB,
        our increment height and width regions"""

        self.landmarks = landmarks
        self.picture = picture
        self.head_box = head_box
        self.points_list = points_list
        self.adding_height = adding_height
        self.add_width = add_width
        self.frame = frame



    def raising_part(self):
        """Put white on region convex interest on a gray picture"""

        #Add height px of our y points.
        width, height = self.head_box[2:]
        add_height_to_points = int(height * self.adding_height)
        add_width_to_points  = int(width  * self.add_width)
        
        #Recuperate landmarks 1:-1
        region = [(self.landmarks.part(n).x, self.landmarks.part(n).y - add_height_to_points)
                  for n in self.points_list[1: -1]]

        #First and last landmark (for hide on eyes)
        region1 = [(self.landmarks.part(self.points_list[0]).x + add_width_to_points,
                    self.landmarks.part(self.points_list[0]).y)]
        region2 = [(self.landmarks.part(self.points_list[-1]).x + add_width_to_points,
                    self.landmarks.part(self.points_list[-1]).y)]

        #Make one list
        region1 += region
        region1 += region2

        #Transfor points into array
        region = np.array(region1)
        #Fill the region in white color on a gray picture
        cv2.fillPoly(self.picture, [region], (255, 255, 255))

        #cv2.imshow("dxd<vwv", self.picture)
        #cv2.fillPoly(self.frame, [region], (255, 255, 255))










#Our landmarks points from DLIB.
ON_LEFT_EYE  = [17, 18, 19, 20, 21]
ON_RIGHT_EYE = [22, 23, 24, 25, 26]
MOUSE        = [21, 6, 10, 22]
LEFT_EYE     = [36, 37, 38, 39, 40, 41]
RIGHT_EYE    = [42, 43, 44, 45, 46, 47]
add = 0.055
zero = 0
def raising(landmarks, th, th1, head_box, frame):

    global ON_LEFT_EYE
    global ON_RIGHT_EYE
    global MOUSE
    global LEFT_EYE
    global RIGHT_EYE

    global add
    global zero

  
    #start_time_timmer = time.time()


    raising_on_eyes1 = Raise_region(landmarks, th, head_box, ON_LEFT_EYE, add, zero, frame)
    raising_on_eyes1.raising_part()
    
    raising_on_eyes2 = Raise_region(landmarks, th, head_box, ON_RIGHT_EYE, add, zero, frame)
    raising_on_eyes2.raising_part()


    raising_mouse1 = Raise_region(landmarks, th, head_box, MOUSE, zero, zero, frame)
    raising_mouse1.raising_part()

    raising_eye3  = Raise_region(landmarks, th, head_box, LEFT_EYE, zero, zero, frame)
    raising_eye3.raising_part()
    
    raising_eye4  = Raise_region(landmarks, th, head_box, RIGHT_EYE, zero, -0.5, frame)
    raising_eye4.raising_part()


    raising_mouse2 = Raise_region(landmarks, th1, head_box, MOUSE, zero, zero, frame)
    raising_mouse2.raising_part()

    raising_eye1  = Raise_region(landmarks, th1, head_box, LEFT_EYE, zero, zero, frame)
    raising_eye1.raising_part()
    
    raising_eye2  = Raise_region(landmarks, th1, head_box, RIGHT_EYE, add, zero, frame)
    raising_eye2.raising_part()

    #print("raising: ", time.time() - start_time_timmer)













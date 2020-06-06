import cv2
import numpy as np

class MakeArea:

    #global en cls
    
    def __init__(self, points, adding, landmarks, frame_head, mode_region, threshold):

        self.points      = points
        self.adding      = adding
        self.landmarks   = landmarks
        self.frame_head  = frame_head
        self.mode_region = mode_region
        self.threshold   = threshold


    @staticmethod
    def make_line(thresh):
        """We make line for detect more than one area
        with border, on eyelashes is paste to the border"""

        cv2.line(thresh, (0, 0), (0, thresh.shape[0]), (255, 255, 255), 2)
        cv2.line(thresh, (0, 0), (thresh.shape[1], 0), (255, 255, 255), 2)
        cv2.line(thresh, (thresh.shape[1], 0), (thresh.shape[1], thresh.shape[0]), (255, 255, 255), 2)
        cv2.line(thresh, (0,  thresh.shape[0]), (thresh.shape[1], thresh.shape[0]), (255, 255, 255), 2)

        return thresh


    def recuperate_coordinates(self):
        """Here we recuperate coordinate of landmarks under convex area.
        middle mode's mean of 2 landmarks"""

        if self.mode_region == "middle":
            point  = self.points[-1]
            points = self.points[:-1]

        area_landmarks = [(self.landmarks.part(pts[0]).x + add[0],
                           self.landmarks.part(pts[1]).y + add[1])
                          for pts, add in zip(self.points, self.adding)]

        if self.mode_region == "middle":
            midle_point = self.landmarks.part(point[0]).x + self.landmarks.part(point[1]).x
            midle_point = int(midle_point / 2)
            area_landmarks += [(midle_point, self.landmarks.part(point[0]).y)]

        self.convexPoints = cv2.convexHull(np.array(area_landmarks))  

        crops = MakeArea.masks_from_convex(self)
        crop_threhsold, crop_frame, box_crop = crops

        return crop_threhsold, crop_frame, box_crop


    def masks_from_convex(self):
        """Make a mask of the region convex interest from the frame.
        Make a box of the mask"""

        height_frame, width_frame = self.frame_head.shape[:2]
        black_frame = np.zeros((height_frame, width_frame), np.uint8)
        mask = np.full((height_frame, width_frame), 255, np.uint8)
        cv2.fillPoly(mask, [self.convexPoints], (0, 0, 255))

        #cv2.drawContours(self.frame_head, [self.convexPoints], -1, (0, 0, 255), 1)
        mask_threhsold = cv2.bitwise_not(black_frame, self.threshold.copy(), mask=mask)

        self.box_crop = cv2.boundingRect(self.convexPoints)
        x ,y, w, h = self.box_crop

        self.crop_threshold = mask_threhsold[y:y+h, x:x+w]
        self.crop_threshold = MakeArea.make_line(self.crop_threshold)

        self.crop_frame     = self.frame_head[y:y+h, x:x+w]

        #cv2.imshow("cdqsdcqs", self.threshold)
        #cv2.rectangle(self.frame_head, (x, y), (x+w, y+h), (0, 0, 255), 1)

        return (self.crop_threshold, self.crop_frame, self.box_crop)


    @staticmethod
    def skin_detector(frame):

        min_YCrCb = np.array([0,140,85],np.uint8)
        max_YCrCb = np.array([240,180,130],np.uint8)
        imageYCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
        skinRegionYCrCb = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))
        skinMask = cv2.dilate(skinRegionYCrCb, kernel, iterations = 2)
        skinMask = cv2.morphologyEx(skinMask, cv2.MORPH_CLOSE, kernel)

        skinYCrCb = cv2.bitwise_and(frame, frame, mask = skinMask)

        return skinYCrCb

"""dedz"""

import cv2


from figure.wrinkle.make_area_class import MakeArea

class Detection:
    """
        zadza
    """
    def __init__(self, landmarks, frame, mode_feature, threshold,
                 crop_threshold, box_crop, data_feature, crop_frame,
                 wrinkle_number, crop_skin):
        """
            Here we recuperate our data features.
            the contours dimensions, the max and min length and width of
            contours.
            Make class object of threshold, crop threshold (mask from region define
            by makeArea class).

            Recuperate the frame and the crop for drawContours and the skin
            crop for define forehead without hair.

            Recuperate the region convex in a box, and the wrinkle number in case
            we have defined it. Finnaly the mode of the feature (direction of
            the wrinkle ex: beetween != forehead.)
        """

        max_contour, min_contour, min_length, max_length, min_width, max_width = data_feature

        self.crop_threhsold = crop_threshold
        self.box_crop = box_crop
        self.min_contour = min_contour
        self.max_contour = max_contour
        self.min_length = min_length
        self.max_length = max_length
        self.min_width = min_width
        self.max_width = max_width
        self.mode_feature = mode_feature
        self.crop_frame = crop_frame
        self.wrinkle_number = wrinkle_number
        self.frame = frame
        self.crop_skin = crop_skin


    @staticmethod
    def extremums(contour):
        """Recuperate left, right top and bottom extemums corner's"""

        xextremum = tuple(contour[contour[:, :, 0].argmin()][0])  #left
        yextremum = tuple(contour[contour[:, :, 1].argmin()][0])  #right
        wextremum = tuple(contour[contour[:, :, 0].argmax()][0])
        hextremum = tuple(contour[contour[:, :, 1].argmax()][0])  #bottom

        return xextremum, yextremum, wextremum, hextremum

    def localisation_wrinkle(self):
        """
        dzadazdaz
        """
        _, _, width, height = self.box_crop

        wrinkles_list = []

        max_contour = int((width * height) * self.max_contour)
        min_contour = int((width * height) * self.min_contour)

        max_length_requiert = int(height * self.max_length)
        min_length_requiert = int(height * self.min_length)

        contours, _ = cv2.findContours(self.crop_threhsold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:

            if min_contour < cv2.contourArea(cnt) < max_contour:

                xextremum, yextremum, wextremum, hextremum = Detection.extremums(cnt)
                extemums = xextremum, yextremum, wextremum, hextremum
                largeur = wextremum[0] - xextremum[0]
                longueur = hextremum[1] - yextremum[1]

                if self.mode_feature == "length":
                    features = (longueur, largeur, min_length_requiert,
                                max_length_requiert, hextremum, yextremum)

                    Detection.condition_length(features, wrinkles_list)


                elif self.mode_feature == "width":
                    features = (largeur, longueur, self.min_width,
                                self.max_width, xextremum, wextremum)

                    Detection.condition_width(features, self.crop_frame)


                elif self.mode_feature == "lengthWidth":
                    features = (max_length_requiert, longueur, min_length_requiert,
                                self.max_width, largeur, self.min_width,
                                hextremum, yextremum)

                    Detection.condition_length_and_width(features, self.crop_frame)


                elif self.mode_feature == "left":
                    cv2.line(self.crop_frame, (wextremum[0], yextremum[1]),
                             (xextremum[0], hextremum[1]), (0, 255, 0), 1)


                elif self.mode_feature == "right":
                    cv2.line(self.crop_frame, (xextremum[0], yextremum[1]),
                             (wextremum[0], hextremum[1]), (0, 255, 255), 1)


                elif self.mode_feature == "length_or_width":
                    features = (longueur, min_length_requiert, largeur)
                    Detection.condition_length_width(features, extemums, wrinkles_list)


                elif self.mode_feature == "black":
                    features = (largeur, longueur, xextremum, wextremum, self.min_width, self.max_width)
                    Detection.condition_black(features, wrinkles_list, cnt, self.crop_skin, width)


        if len(wrinkles_list) >= self.wrinkle_number:
            [cv2.line(self.crop_frame, i[0], i[1], (0, 0, 255), 1) for i in wrinkles_list]



    @classmethod
    def condition_length(cls, features, wrinkles):
        """Recuperate wrinkle if length > width"""

        longueur, largeur, min_length, max_length, hextremum, yextremum = features

        if longueur > largeur and\
           min_length < longueur < max_length:
            wrinkles.append((hextremum, yextremum))


    @classmethod
    def condition_width(cls, features, crop_frame):
        """Recuperate wrinkle if width > length"""

        largeur, longueur, min_width, max_width, xextremum, wextremum = features

        if largeur > longueur and\
            min_width < largeur < max_width:
            cv2.line(crop_frame, xextremum, wextremum, (0, 0, 255), 1)

    @classmethod
    def condition_length_and_width(cls, features, crop_frame):

        """Recuperate wrinkle if width's and length are in interval."""

        max_length, longueur, min_length,\
            max_width, largeur, min_width, hextremum,\
            yextremum = features

        if max_length > longueur >= min_length and\
            max_width > largeur >= min_width:
            cv2.line(crop_frame, hextremum, yextremum, (255, 0, 0), 1)

    @classmethod
    def condition_length_width(cls, features, extemums, wrinkles):

        """Recuperate wrinkle if width > length
        and length > width and < to minLength."""
        longueur, min_length, largeur = features
        xextremum, yextemum, wextremum, hextremum = extemums

        if largeur > longueur:
            wrinkles.append((wextremum, xextremum))

        elif largeur < longueur < min_length:
            wrinkles.append((hextremum, yextemum))

    @classmethod
    def condition_black(cls, features, wrinkle_list, cnt, mask_skin, width):
        """
            dzdazdaz
        """


        largeur, longueur, xextremum, wextremum, min_width, max_width = features

        if Detection.no_skin_color(cnt, mask_skin) is False:

            min_width = int(max_width * width) > largeur > int(min_width * width)
            delta_y = wextremum[1] - xextremum[1]
            delta_x = wextremum[0] - xextremum[0]

            pente_angulaire = 0.25 > (delta_y / delta_x) > -0.25#0.4

            if largeur > longueur and min_width and pente_angulaire:
                wrinkle_list.append((wextremum, xextremum))



    @staticmethod
    def recuperate_coordinate(crop_color_skin, extremums):
        """Recuperate from extremums contours the color
        from the picture"""

        xextremum, yextremum, weextremum, heextremum = extremums

        contours = (crop_color_skin[xextremum[1], xextremum[0]],    #right
                    crop_color_skin[yextremum[1], yextremum[0]],    #left
                    crop_color_skin[yextremum[1], xextremum[0]],    #left_bot
                    crop_color_skin[heextremum[1], xextremum[0]],   #left_top
                    crop_color_skin[yextremum[1], weextremum[0]],   #right_bot
                    crop_color_skin[heextremum[1], weextremum[0]],  #right_top
                    crop_color_skin[yextremum[1], xextremum[0]],    #top_right
                    crop_color_skin[yextremum[1], weextremum[0]],   #top_left
                    crop_color_skin[heextremum[1], weextremum[0]],  #bot_right
                    crop_color_skin[heextremum[1], weextremum[0]])  #bot_left

        return contours




    @staticmethod
    def no_skin_color(contour, crop_color_skin):
        """
        We take all extemums contours and verify if 2 of their points
        touch a black pixel (0, 0, 0). It indicate if the contour
        is a skin contour or not. If not it's a hair.
        """

        #Recuperate extremums contours colors from the skin picture.
        right, left, left_bot, left_top, right_bot, right_top,\
                top_right, top_left, bot_right, bot_left\
                = Detection.recuperate_coordinate(crop_color_skin, (Detection.extremums(contour)))

        #If extremums left and right touch black pixel (255, 255, 255)
        #isn't skin pixels.
        #Verify if sides touch black pixels. (no skin pixels)
        verification = lambda i: bool(i[0] == 0 and i[1] == 0 and i[2] == 0)

        #right left extremums.
        #Break and return True if the 2 px touchs black pixel.
        for i in [[verification(i) for i in [right, left]],
                  [verification(i) for i in [left_bot, left_top]],
                  [verification(i) for i in [right_bot, right_top]],
                  [verification(i) for i in [top_right, top_left]],
                  [verification(i) for i in [bot_right, bot_left]]]:

            if i.count(True) == 2:
                return True


        return False











def beetween_wrinkle(landmarks, frame, threshold, height_head, width_head):
    """
    dzadaz
    """

    add_height = int(height_head * 0.09)  #5 de 74
    add_width = int(width_head  * 0.015) #1 de 90
    add = ((-add_width, -add_height), (add_width, -add_height), (0, -add_height))
    points = ((21, 21), (22, 22), (27, 27))

    beetween_eyes = MakeArea(points, add, landmarks, frame, "", threshold)
    crop_threshold, crop_frame, box_crop = beetween_eyes.recuperate_coordinates()

    #maxContour, minContour, minLength, maxLength, min_width, max_width
    data_feature = (0.5, 0.075, 0, 100000, 0, 0)
    beetween_eyes_detect = Detection(landmarks, frame, "length", threshold,
                                     crop_threshold, box_crop, data_feature, crop_frame, 2, "")

    beetween_eyes_detect.localisation_wrinkle()




def side_mouth_right_wrinkle(landmarks, frame, threshold, width_head):

    """
    dazdza
    """

    adding = ((0, 0), (0, 0), (0, 0), (0, 0))
    points = ((35, 30), (54, 54), (46, 35), (54, 54))

    side_mouth_right = MakeArea(points, adding, landmarks, frame, "", threshold)
    crop_threshold, crop_frame, box_crop = side_mouth_right.recuperate_coordinates()


    #maxContour, minContour, minLength, maxLength, min_width, max_width
    data_feature = (0.8, 0.008, 0.26, 10000, int(width_head * 0.06), 10000)

    side_mouth_right_detect = Detection(landmarks, frame, "lengthWidth", threshold,
                                        crop_threshold, box_crop, data_feature, crop_frame, 0, "")

    side_mouth_right_detect.localisation_wrinkle()


def side_mouth_left_wrinkle(landmarks, frame, threshold, width_head):
    """
    dzad
    """

    adding = ((0, 0), (0, 0), (0, 0), (0, 0))
    points = ((31, 30), (48, 48), (41, 31), (48, 48))


    side_mouth_left = MakeArea(points, adding, landmarks, frame, "", threshold)
    crop_threshold, crop_frame, box_crop = side_mouth_left.recuperate_coordinates()

    #maxContour, minContour, minLength, maxLength, min_width, max_width
    data_feature = (0.8, 0.008, 0.26, 10000, int(width_head * 0.06), 10000)

    side_mouth_left_detect = Detection(landmarks, frame, "lengthWidth", threshold,
                                       crop_threshold, box_crop, data_feature, crop_frame, 0, "")

    side_mouth_left_detect.localisation_wrinkle()



def crow_feet_right_wrinkle(landmarks, frame, threshold1):

    """
    dzadaz
    """

    adding = ((0, 0), (0, 0), (0, 0))
    points = ((36, 37), (17, 37), (36, 31), (0, 17))


    crow_right = MakeArea(points, adding, landmarks, frame, "middle", threshold1)
    crop_threshold, crop_frame, box_crop = crow_right.recuperate_coordinates()

    #maxContour, minContour, minLength, maxLength, min_width, max_width
    data_feature = (0.8, 0.003, 0.26, 0, 0.28, 0)

    crow_right_detect = Detection(landmarks, frame, "length_or_width", threshold1,
                                  crop_threshold, box_crop, data_feature, crop_frame, 4, "")

    crow_right_detect.localisation_wrinkle()



def crow_feet_left_wrinkle(landmarks, frame, threshold1):

    """
    dazdaz
    """

    adding = ((0, 0), (0, 0), (0, 0))
    points = ((45, 44), (26, 44), (45, 35), (16, 26))


    crow_left = MakeArea(points, adding, landmarks, frame, "", threshold1)
    crop_threshold, crop_frame, box_crop = crow_left.recuperate_coordinates()

    #maxContour, minContour, minLength, maxLength, min_width, max_width
    data_feature = (0.8, 0.003, 0.26, 0, 0.28, 0)

    crow_left_detect = Detection(landmarks, frame, "length_or_width", threshold1,
                                 crop_threshold, box_crop, data_feature, crop_frame, 4, "")

    crow_left_detect.localisation_wrinkle()



def under_eyes_right_wrinkle(landmarks, frame, threshold, width_head):

    """
    dzadza
    """

    add_height = int(width_head * 0.1) #8 de 85
    adding = ((0, add_height), (0, add_height), (0, 2 * add_height), (0, 2 * add_height))
    points = ((42, 42), (45, 45), (42, 42), (45, 45))


    under_eye_right = MakeArea(points, adding, landmarks, frame, "", threshold)
    crop_threshold, crop_frame, box_crop = under_eye_right.recuperate_coordinates()

    #maxContour, minContour, minLength, maxLength, min_width, max_width
    data_feature = (0.8, 0.05, 0, 0, 0, 0)

    under_eye_right_detect = Detection(landmarks, frame, "right", threshold,
                                       crop_threshold, box_crop, data_feature, crop_frame, 0, "")

    under_eye_right_detect.localisation_wrinkle()





def under_eyes_left_wrinkle(landmarks, frame, threshold, width_head):
    """
    dzadza
    """

    add_height = int(width_head * 0.1) #8 de 85
    adding = ((0, add_height), (0, add_height), (0, 2 * add_height), (0, 2 * add_height))
    points = ((36, 36), (39, 39), (36, 36), (39, 39))


    under_eye_left = MakeArea(points, adding, landmarks, frame, "", threshold)
    crop_threshold, crop_frame, box_crop = under_eye_left.recuperate_coordinates()

    #maxContour, minContour, minLength, maxLength, min_width, max_width
    data_feature = (0.8, 0.05, 0, 0, 0, 0)

    under_eye_left_detect = Detection(landmarks, frame, "left", threshold,
                                      crop_threshold, box_crop, data_feature, crop_frame, 2, "")

    under_eye_left_detect.localisation_wrinkle()



def forehead(landmarks, head_box, frame, threshold):

    """
    We try to localise forehead wrinkles. For that we use a DLIB model
    using 81 landmarks who's include the forehead.
    We increment the forehead for havn't got the on eyes (adding).
    Then we define our points. We make the area who's define a mask
    (threshold and frame) of the region interest.
    Next we make a crop skin with the static function skin color for
    detect the skin and none detect the hair.
    Next we define the feature of the wrinkle and try to recuperate
    contour with the conditions.
    """

    _, _, width_head, height_head = head_box

    add1 = - int(0.1 * height_head)
    add2 = int(0.1 * width_head)

    adding = [(add2, 0), (add2, 0), (add2, 0), (0, 0),
              (0, 0), (0, 0), (0, 0), (0, 0),
              (-add2, 0), (-add2, 0), (-add2, 0),

              (0, add1), (0, add1),(0, add1), (0, add1), (0, add1),
              (0, add1),(0, add1), (0, add1), (0, add1), (0, add1)]

    points = [(75, 75), (76, 76), (68, 68), (69, 69),
              (70, 70), (71, 71), (80, 80), (72, 72),
              (73, 73), (79, 79), (74, 74),

              (26, 26), (25, 25), (24, 24), (23, 23), (22, 22),
              (21, 21), (20, 20), (19, 19), (18, 18), (17, 17)]


    front = MakeArea(points, adding, landmarks, frame, "", threshold)
    crop_threshold, crop_frame, box_crop = front.recuperate_coordinates()

    crop_skin = MakeArea.skin_detector(crop_frame)

    #maxContour, minContour, minLength, maxLength, min_width, max_width
    data_feature = (0.9, 0.0039, 0, 100000, 0.15, 0.71)

    front = Detection(landmarks, frame, "black", threshold,
                      crop_threshold, box_crop, data_feature, crop_frame, 2, crop_skin)

    front.localisation_wrinkle()



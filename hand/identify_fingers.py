import cv2
from scipy.spatial import distance as dist



def draw_line_pts(copy, text, pts1, pts2):
    """Draw line and put text"""

    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(copy, text, pts2, font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.line(copy, pts1, pts2, (0, 255, 0), 1)


def releve_data_thumb_fingers(points, thumb):
    """We need thumb/fingers space for releve ratio"""

    for i in points:
        if i != (): print(dist.euclidean(i, thumb[0][-1]))


def removing(nb, liste):
    """Remove fingers annatotation from list"""
    for i in range(nb): liste.remove(liste[0])



def ratio_choice(direction):
    """Choose the ratio length"""

    if direction in ("droite", "gauche"):   area = "width"
    elif direction in ("bas", "haut"):      area = "height"
    return area



def thumb_to_next_finger(points, thumb, fing, copy):
    """Sometimes no detection of index, so we need to identify by distance
    the next finger"""

    #Draw thumb points
    draw_line_pts(copy, "P", thumb[0][-1], thumb[0][-1])

    #Identify distance beetween first and thumb point
    thumb_index = dist.euclidean(points[0], thumb[0][-1])
    print(thumb_index, (w,h))


    #Index
    if area == "width" and thumb_index < w * 0.574 or\
       area == "height" and thumb_index < w * 0.574:
        draw_line_pts(copy, fing[0],thumb[0][-1], points[0])
        removing(1, fing)

    #Major
    elif area == "width" and w * 0.775 > thumb_index > w * 0.574 or\
         area == "height" and w * 0.775 > thumb_index > w * 0.574:
        draw_line_pts(copy, fing[1], thumb[0][-1], points[0])
        removing(2, fing)

    #Auricular
    elif 130 > thumb_index > 105:
        draw_line_pts(copy, fing[2], thumb[0][-1], points[0])
        removing(3, fing)

    #Annular
    elif thumb_index > 130:
        draw_line_pts(copy, fing[3], thumb[0][-1], points[0])
        removing(4, fing)


    cv2.imshow("thumb_next_finger", copy)
    cv2.waitKey(0)
      

def printing(rectangle, thumb, fingers, direction, axis):

    print("")
    print("IDENTIFY FINGERS")

    #Ratio aspect
    print("Box de la main est de: ", rectangle)
    #Need the thumb for detect the next first finger
    print(thumb)
    #Our finger's
    print(fingers)
    #Direction for the location for the next first finger
    print(direction, axis)




def identify_fingers(thumb, fingers, crop, rectangle, direction, axis):


    printing(rectangle, thumb, fingers, direction, axis)

    copy = crop.copy()
    fing = ["I", "M", "An", "a"]
    x, y, w, h = rectangle


    #Add None then replace by ()
    fingers += [None for i in range(4 - len(fingers))]
    points = [(lambda x: () if x == None else x[0][-1])(i) for i in fingers]

    #Choice area in function of hand position
    area = ratio_choice(direction)

    #Identify finger after the thumb
    thumb_to_next_finger(points, thumb, fing, copy)

    #For us
    releve_data_thumb_fingers(points, thumb)


    for i in range(len(points)):
        print("\n", fing)

        if i < len(points) - 1 and points[i] != () and points[i + 1] != ():

            distance = dist.euclidean(points[i], points[i + 1])
            print(a, (w, h))

            #One point after
            if distance < w * 0.295 and area == "width" or\
               distance < w * 0.295 and area == "height":
                print("Moins 35")
                draw_line_pts(copy, fing[0], points[i], points[i + 1])
                removing(1, fing)

            elif len(fing) == 1:
                print("reste plus qu'un doigt")
                draw_line_pts(copy, fing[0], points[i], points[i + 1])
                removing(1, fing)

            elif (w * 0.295) * 2 > distance > w * 0.295:
                print("1 doigt apres")
                draw_line_pts(copy, fing[1], points[i], points[i + 1])
                removing(2, fing)

            elif (w * 0.295) * 3 > distance > (w * 0.295) * 2:
                print("2 doigts apres")
                draw_line_pts(copy, fing[2], points[i], points[i + 1])
                removing(3, fing)

            elif (w * 0.295) * 4 > distance > (w * 0.295) * 3:
                print("3 doigts apres")
                draw_line_pts(copy, fing[3], points[i], points[i + 1])
                removing(4, fing)

            elif distance > (w * 0.295) * 4:
                print("ici ecart supp a * 4")



            cv2.imshow("thumb_next_finger", copy)
            cv2.waitKey(0)
            print("")


    if len(fing) > 0: print("manque des doigts :", fing)




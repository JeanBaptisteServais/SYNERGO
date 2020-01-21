"""Here we recuperate skeletton points. We need to identify the position of the
thumb. By this we can search, organise and identify the finger's and their positions.
For that we compare fingertip coordiantes."""

import cv2
from scipy.spatial import distance as dist


def thumb_localisation(end_fingers, thumb):
    """Compare Thumb, fingers x and y position and determinate thumb position
    in function of them."""

    thumbx, thumby = thumb[0], thumb[1]                                 #Thumb (x, y)
    dico_direction = {"left" :0, "right" :0, "top" :0, "bot" :0}

    for fing in end_fingers:
        fingx, fingy = fing[0], fing[1]                                 #Finger (x, y)

                                                                        #Compare Thumb - fingers
        if thumbx < fingx:      dico_direction["left"]  += 1            #x axis
        elif thumbx > fingx:    dico_direction["right"] += 1
        if thumby < fingy:      dico_direction["top"]   += 1            #y axis
        elif thumby > fingy:    dico_direction["bot"]   += 1


    if dico_direction["left"] > dico_direction["right"]:    hand = "pouce gauche"
    elif dico_direction["right"] > dico_direction["left"]:  hand = "pouce droite"

    return hand


def printing(thumb, index, major, annular, auricular):
    """Printing for printing informations"""
    print("HAND LOCATION")    
    print(thumb, index, major, annular, auricular, "\n")


def thumb_location(thumb, index, major, annular, auricular, crop):

    copy = crop.copy()

    printing(thumb, index, major, annular, auricular)                               #1 - Print data finger's

    fingers = [index, major, annular, auricular]                                    #2 - Recuperate fingers.



    removing = lambda liste, element: liste.remove(element)                         #3 - Delete False detection.
    [removing(i, j) for i in fingers for j in i if j == ((0, 0), (0, 0))]



    end_fingers = [finger[-1][1] for finger in fingers if finger != []]             #4 - recuperate fingertips
    [cv2.circle(copy, fingers, 2, (255, 0, 0), 2)for fingers in end_fingers]



    thumb_find = len([j for i in thumb for j in i if j == (0, 0)])                  #5 - Verify thumb isn't empty
    thumb_validation_points = len(thumb) * 2



    if thumb_validation_points == thumb_find:                                       #6 - Empty thumb
        return False

    else:
        thumb = [j for i in thumb for j in i if j != (0, 0)][-1]                    #7 - Recuperate last point thumb

        hand = thumb_localisation(end_fingers, thumb)                               #8 - Thumb localisation compared fingers

        cv2.circle(copy, thumb, 2, (0, 0, 255), 2)
        cv2.imshow("Hand", copy)
        cv2.waitKey(0)

        print(hand, "\n")

        return hand

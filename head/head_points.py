from dlib import get_frontal_face_detector, shape_predictor
import cv2
import numpy as np


def load_model_dlib(path_points_head):
    detector = get_frontal_face_detector()
    predictor = shape_predictor(path_points_head)

    return predictor, detector


def recuperate_landmarks(gray_frame, predictor, detector):
    """Recuperate landmarks from dlib"""

    faces = detector(gray_frame)
    out = None, None

    if len(faces) > 0:
        landmarks = predictor(gray_frame, faces[0])
        out = faces, landmarks

    return out


def get_face_in_box(landmarks):
    """Recuperate all coordiantes of landmarks (faces points).
    Recuperate convex points (exterior of face) and triangle
    points (area of the interior of the face)."""

    points = [(landmarks.part(n).x, landmarks.part(n).y)
              for n in range(0, 68)]

    convexhull = cv2.convexHull(np.array(points))
    head_box = cv2.boundingRect(convexhull)

    return head_box


def head_points(gray_frame, predictor, detector):

    out = None, None
    faces, landmarks = recuperate_landmarks(gray_frame, predictor, detector)
    if landmarks is not None:
        head_box = get_face_in_box(landmarks)
        out = landmarks, head_box

    return out

from video_capture import video_lecture

#Video
videoA = r"C:\Users\jeanbaptiste\Desktop\jgfdposgj\video\a.mp4"
videoB = r"C:\Users\jeanbaptiste\Desktop\jgfdposgj\video\b.mp4"
videoC = r"C:\Users\jeanbaptiste\Desktop\jgfdposgj\video\c.mp4"
videoD = r"C:\Users\jeanbaptiste\Desktop\jgfdposgj\video\d.mp4"
videoE = r"C:\Users\jeanbaptiste\Desktop\jgfdposgj\video\e.mp4"
videoF = r"C:\Users\jeanbaptiste\Desktop\jgfdposgj\video\f.mp4"
videoG = r"C:\Users\jeanbaptiste\Desktop\jgfdposgj\video\g.mp4"


#Models
facePoints = r"C:\Users\jeanbaptiste\Desktop\jgfdposgj\face\models\shape_predictor_68_face_landmarks.dat"




if __name__ == "__main__":

    video_lecture(videoA, facePoints)

import cv2
import numpy as np
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer
import screeninfo
video_path='street_urchin.mp4'

screen_id = 0
screen = screeninfo.get_monitors()[screen_id]
WIDTH, HEIGHT = screen.width, screen.height
dim = (WIDTH, HEIGHT)
print('width', WIDTH)
print('height', HEIGHT)

window_name = "window"
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
# #cv2.namedWindow("output", cv2.WINDOW_NORMAL) 
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

def PlayVideo(video_path):
    video = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        success, frame = video.read()
        frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        audio_frame,val = player.get_frame()
        if not success:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow(window_name, frame)
        if val != 'eof' and audio_frame is not None:
            # audio
            frame, t = audio_frame
    video.release()
    cv2.destroyAllWindows()


PlayVideo(video_path)




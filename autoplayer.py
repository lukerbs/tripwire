from gpiozero import MotionSensor
import vlc
import time


media_player = vlc.MediaPlayer()
media_player.toggle_fullscreen()
t = 0.0
media = vlc.Media("movie.mp4")

pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    print('YOU MOVED!!!!!!!!!!!!!')
    media.add_option('start-time=' + str(t))
    media_player.set_media(media)
    media_player.play()
    #time.sleep(5)
    
    #time.sleep(media_player.get_length()/1000)
    

    pir.wait_for_no_motion()
    time.sleep(15)
    t+= 15.0
    media_player.stop()
    

    print('Motion stopped')
# importing vlc module
import vlc
import time
  
  
media_player = vlc.MediaPlayer()
media_player.toggle_fullscreen()
media = vlc.Media("movie.mp4")
  
media_player.set_media(media)

media_player.play()
time.sleep(2)
time.sleep(media_player.get_length()/1000)



# import os
# import winsound

from winsound import Beep

if __name__ == "__main__":

    # sound_file = os.getcwd() + os.sep + "notify_done_sound_1.wav"
    # sound_file = os.path.normpath(sound_file)
    # winsound.PlaySound(sound_file, winsound.SND_FILENAME)

    Beep(440, 500); Beep(440, 500); Beep(440, 500)
    Beep(349, 350); Beep(523, 150); Beep(440, 500); Beep(349, 350); Beep(523, 150); Beep(440, 1000) 
    # Beep(659, 500); Beep(659, 500); Beep(659, 500); Beep(698, 350); Beep(523, 150); Beep(415, 500); Beep(349, 350); Beep(523, 150); Beep(440, 1000)
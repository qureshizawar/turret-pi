import glob
import random
import simpleaudio

class GladosBitcher:
    sounds = []
    def __init__(self):
        # load the wav files
        files = [f for f in glob.glob('sounds/turret/*.wav')]

        print(files)

        for f in files:
            wav = simpleaudio.WaveObject.from_wave_file(f)
            self.sounds.append(wav)

    def bitch(self):
        r = random.randint(0, len(self.sounds))
        po = self.sounds[r].play()
        po.wait_done()


        
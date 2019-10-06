from os import environ, system
from os.path import join, split
from subprocess import Popen, DEVNULL
from threading import Thread

ffplay_path = join(split(__file__)[0], "bin", "ffplay.exe")

class Player():
    def __init__(self, url=None, proxy=None):
        self.url = url
        self.ps = None
        self.playing = False
        self.loop = False
        self.proxy = proxy

    def setURL(self, url):
        self.url = url

    def waitFunc(self):
        self.wait()
        self.playing = False
        if self.loop:
            self.play()

    def play(self, url=None):
        if url:
            self.setURL(url)
        if not self.url:
            return
        if self.playing:
            self.stop()
        self.command = ffplay_path + \
            " -i {} -nodisp -autoexit".format(self.url)
        envcopy = environ.copy()
        if self.proxy is not None:
            envcopy["http_proxy"] = self.proxy["http"]
            envcopy["https_proxy"] = self.proxy["https"]
        self.ps = Popen(self.command.split(), stdout=DEVNULL,
                        stderr=DEVNULL, env=envcopy)
        self.wait = self.ps.wait
        self.playing = True
        self.waitThread = Thread(target=self.waitFunc)
        self.waitThread.start()

    def stop(self):
        if not self.ps:
            return
        self.ps.terminate()
        self.ps = None

    def setURL_future(self, url):
        pass

    def stop_future(self):
        pass

    def play_future(self, url=None):
        pass

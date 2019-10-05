class Player():
    def __init__(self, url=None):
        self.url = url
        self.ps = None
        self.playing = False
        self.loop = False

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
        if global_proxy is not None:
            envcopy["http_proxy"] = global_proxy["http"]
            envcopy["https_proxy"] = global_proxy["https"]
        if play_legacy:
            system(self.command)
        else:
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

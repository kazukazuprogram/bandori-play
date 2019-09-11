from io import BufferedIOBase
from pygame import mixer
from requests import Session
from threading import Thread
from time import sleep

url = "https://vignette.wikia.nocookie.net/bandori/images/2/20/Ai_no_Scenario_%28Game_Version%29.ogg/revision/latest?cb=20190910042628"
s = Session()

def streamAudio(url):
    global audioFile
    global request_allowed
    print(url)
    request_allowed = -1
    g = s.get(url, stream=True)
    request_allowed = 0
    print("Streaming start.")
    if g.status_code == 200:
        print("REQ OK.")
        request_allowed = 1
        for chunk in g.iter_content(chunk_size=1024):
            audioFile.write(chunk)
    else:
        request_allowed = 2

request_allowed = -2
audioFile = BufferedIOBase()
Thread(target=streamAudio, args=(url, ))

while request_allowed==0:
    print(request_allowed)
    print(audioFile.read(16))
    sleep(0.1)
print("OK")
sleep(1)

mixer.init()
fp = open("file.ogg", "rb")
print(fp, audioFile)
mixer.music.load(audioFile)
mixer.music.play(-1)
sleep(60)

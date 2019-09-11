# pythonから叩くのでテスト用pythonコード
# 音を鳴らすためにpyaudioを叩いてます
import vorbistest
import pyaudio
import wave

file_path = b"/tmp/hoge.ogg"

res = vorbistest.decode(file_path) #ここでデコード

print(res)

channels = res['channels']
rate = res['rate']
width = res['width']
data = res['data']
p = pyaudio.PyAudio()
CHUNK = 1024
stream = p.open(format=p.get_format_from_width(width),
                channels=channels,
                rate=rate,
                output=True)

buffer = data.read(CHUNK) # python3 ではbytes型
while buffer != b'':
    stream.write(buffer) # audio側にwrite(ここで鳴らしている
    buffer = data.read(CHUNK) # バッファにread

# 後始末
stream.stop_stream()
stream.close()
p.terminate()

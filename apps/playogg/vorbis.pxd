cimport vorbistest as h
from libc.stdio cimport (
    FILE,
    fopen,
)

DEF BUFFER_SIZE = 32768

def decode(name):
    cdef int endian = 0 # 0 for little endian, 1 for big endian
    cdef int bitStream
    cdef char array[BUFFER_SIZE] # arrayという名のbuffer

    cdef FILE *f = fopen(name, "rb")
    cdef h.vorbis_info *pinfo

    cdef OggVorbis_File oggFile

    h.ov_open(f, &oggFile, NULL, 0)
    pinfo = h.ov_info(&oggFile, -1)

    print("version:%d"%pinfo.version)
    print("channels:%d"%pinfo.channels)
    print("rate:%d"%pinfo.rate)

    res = {
        'width':2, # pinfoにないのでwaveのwidthどれが良いのかわからず、
        'rate':pinfo.rate,
        'channels':pinfo.channels,
    }

    import io
    buf = io.BytesIO()

    cdef long load_length
    load_length = h.ov_read(&oggFile, array, BUFFER_SIZE, endian, 2, 1, &bitStream)
    while load_length>0:
        buf.write(array[:load_length])
        load_length = h.ov_read(&oggFile, array, BUFFER_SIZE, endian, 2, 1, &bitStream)
        pass
    h.ov_clear(&oggFile)

    buf.seek(0)
    res['data'] = buf
    return res

from libc.stdio cimport FILE

cdef extern from "vorbis/codec.h":
    # vorbis/codec.hを見ながら型を書く
    # vorbistest.pyxでvorbis_infoの中身を参照しているので書く必要がある
    ctypedef struct vorbis_info:
        int version
        int channels
        long rate

        long bitrate_upper
        long bitrate_nominal
        long bitrate_lower
        long bitrate_window

        void *codec_setup

cdef extern from "vorbis/vorbisfile.h":
    # vorbis/vorbisfile.hを見ながら型を書く
    ctypedef struct OggVorbis_File:
        pass
    int ov_open(FILE *f, OggVorbis_File *vf, char *initial, long ibytes)
    long ov_read(OggVorbis_File *fv, char *buffer, int length,
                      int bigendianp, int word, int sgned, int *bitstream)
    vorbis_info *ov_info(OggVorbis_File *vf, int link)
    int ov_clear(OggVorbis_File *vf)

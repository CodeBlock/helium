#!/usr/bin/env python
# (c) 2013 Ricky Elrod
# MIT Licensed.
# This file is part of the Helium project.

from sh import aplay, convert, robot36_encode, raspistill

cwd = '/tmp/'

def take_picture():
    '''Take a picture using the Raspberry Pi's Camera.
       The picture gets stored at /tmp/latest.jpg.
    '''
    raspistill("-w", "320", "-h", "240", "-o", "latest.jpg", _cwd=cwd)

def convert_picture_to_ppm():
    '''Convert latest.jpg to a PPM (latest.ppm).'''
    convert("latest.jpg", "latest.ppm", _cwd=cwd)

def overlay_text(text, top_or_bottom):
    '''Overlay text on latest.ppm.
       We do this twice so that it's readable in light and dark images.
    '''
    if top_or_bottom == 'top':
        (y1, y2) = (15, 16)
    else:
        (y1, y2) = (235, 236)
    convert(
        "latest.ppm",
        "-pointsize", "18",
        "-fill", "black",
        "-annotate", "+0+" + str(y1), # Shadow
        text,
        "-fill", "white",
        "-annotate", "+1+" + str(y2), # Foreground
        text,
        "latest.ppm",
        _cwd=cwd)

def make_sstv():
    '''Convert latest.ppm to an SSTV wav file.'''
    robot36_encode("latest.ppm", "latest.wav", _cwd=cwd)

def play_sstv():
    '''Play the SSTV file using aplay.'''
    aplay("latest.wav", _cwd=cwd)

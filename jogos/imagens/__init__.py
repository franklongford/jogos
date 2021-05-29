import os
import pygame as pg

cwdir = os.path.dirname(__file__)


def get_image(name):
    return pg.image.load(
        os.path.join(cwdir, name)
    )

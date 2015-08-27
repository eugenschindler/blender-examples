from bge import render
from bge import logic
import bgl
import blf

def initFontRendering():
    """init function - runs once"""
    # create a new font object, use external ttf file
    font_path = logic.expandPath('//Cubellan.ttf')
    # store the font indice - to use later
    logic.font_id = blf.load(font_path)

    # set the font drawing routine to run every frame
    scene = logic.getCurrentScene()
    scene.post_draw = [writeMessageOnScreen]

def writeMessageOnScreen():
    """write on screen"""
    width = render.getWindowWidth()
    height = render.getWindowHeight()

    bgl.glMatrixMode(bgl.GL_PROJECTION)
    bgl.glLoadIdentity()
    bgl.gluOrtho2D(0, width, 0, height)
    bgl.glMatrixMode(bgl.GL_MODELVIEW)
    bgl.glLoadIdentity()

    font_id = logic.font_id
    blf.position(font_id, (width * 0.02), (height * 0.05), 0)
    blf.size(font_id, 35, 50)
    bgl.glColor4f(1, 0, 0, 1)
    blf.draw(font_id, "Hello World!")

    bgl.glColor4f(0, 1, 0, 1)
    blf.position(font_id, (width * 0.02), (height * 0.15), 0)
    blf.size(font_id, 25, 50)
    blf.draw(font_id, "Hello World!")

    bgl.glColor4f(0, 0, 1, 1)
    blf.position(font_id, (width * 0.02), (height * 0.20), 0)
    blf.size(font_id, 25, 50)
    blf.draw(font_id, "Hello World!")
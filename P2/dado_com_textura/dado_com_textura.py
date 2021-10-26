from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png


ESCAPE = '\033'

window = 0

xrot = yrot = zrot = 0
dx = 0.1
dy = 0.1
dz = 0


def LoadTextures():
    global texture
    texture = glGenTextures(6)

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='dado.png')
    w, h, pixels, metadata = reader.read_flat()
    if (metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glBindTexture(GL_TEXTURE_2D, texture[1])
    reader = png.Reader(filename='dado.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    glBindTexture(GL_TEXTURE_2D, texture[2])
    reader = png.Reader(filename='dado.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    glBindTexture(GL_TEXTURE_2D, texture[3])
    reader = png.Reader(filename='dado.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    glBindTexture(GL_TEXTURE_2D, texture[4])
    reader = png.Reader(filename='dado.png')
    w, h, pixels, metadata = reader.read_flat()
    if (metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    glBindTexture(GL_TEXTURE_2D, texture[5])
    reader = png.Reader(filename='dado.png')
    w, h, pixels, metadata = reader.read_flat()
    if (metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


def InitGL(Width, Height):
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def DrawGLScene():
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0.5, 0.5, 0.5, 1.0)
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(zrot, 0.0, 0.0, 1.0)

    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUADS)

    # Frente do Dado
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 1.0 / 2.0); glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0 / 3.0, 1.0 / 2.0); glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0 / 3.0, 0.0); glVertex3f(-1.0, 1.0, 1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[1])
    glBegin(GL_QUADS)

    # Costas do Dado
    glTexCoord2f(2.0/3.0, 1.0/2.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(2.0/3.0, 1.0); glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0/2.0); glVertex3f(1.0, -1.0, -1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[2])
    glBegin(GL_QUADS)
    
    # Topo do Dado
    glTexCoord2f(0.0, 1.0/2.0); glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0/3.0, 1.0); glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0/3.0, 1.0/2.0); glVertex3f(1.0, 1.0, -1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[3])
    glBegin(GL_QUADS)

    # Fundo do dado
    glTexCoord2f(2.0/3.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(2.0/3.0, 1.0/2.0); glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0/2.0); glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, 1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[4])
    glBegin(GL_QUADS)

    # Lateral direita do Dado
    glTexCoord2f(1.0/3.0, 0.0); glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0/3.0, 1.0/2.0); glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(2.0/3.0, 1.0/2.0); glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(2.0/3.0, 0.0); glVertex3f(1.0, -1.0, 1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[5])
    glBegin(GL_QUADS)

    # Lateral esquerda do dado
    glTexCoord2f(1.0/3.0, 1.0/2.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0/3.0, 1.0); glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(2.0/3.0, 1.0); glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(2.0/3.0, 1.0/2.0); glVertex3f(-1.0, 1.0, -1.0)
    glEnd() 

    xrot = xrot + 0.01  # X rotation
    yrot = yrot + 0.02  # Y rotation
    zrot = zrot + 0.02  # Z rotation

    glutSwapBuffers()

def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == 'x' or tecla == 'X':
        dx = 0.5
        dy = 0
        dz = 0
    elif tecla == 'y' or tecla == 'Y':
        dx = 0
        dy = 0.5
        dz = 0
    elif tecla == 'z' or tecla == 'Z':
        dx = 0
        dy = 0
        dz = 0.5


def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        print("ESQUERDA")
        xrot -= dx  # X rotation
        yrot -= dy  # Y rotation
        zrot -= dz
    elif tecla == GLUT_KEY_RIGHT:
        print("DIREITA")
        xrot += dx  # X rotation
        yrot += dy  # Y rotation
        zrot += dz
    elif tecla == GLUT_KEY_UP:
        print("CIMA")
    elif tecla == GLUT_KEY_DOWN:
        print("BAIXO")


def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowSize(640, 480)

    # Inicia no canto superior esquerdo da tela
    glutInitWindowPosition(0, 0)

    window = glutCreateWindow("Textura")

    glutDisplayFunc(DrawGLScene)

    glutIdleFunc(DrawGLScene)

    glutReshapeFunc(ReSizeGLScene)

    glutKeyboardFunc(keyPressed)

    glutSpecialFunc(teclaEspecialPressionada)

    InitGL(640, 480)

    glutMainLoop()


if __name__ == "__main__":
    print("Pressione ESC para sair.")
    main()
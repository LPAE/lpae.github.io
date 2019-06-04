import numpy as np
from OpenGL.GL import *


class Solids:
    def __init__(self,
                 vertices=None,
                 edges=None,
                 surfaces=None,
                 color=None,
                 origin=(0, 0, 0),
                 axis=(0, 0, 0),
                 size=None):

        self.vertices = vertices
        self.edges = edges
        self.surface = surfaces
        self.color = np.asarray(color)
        self.size = size
        self._origin = np.asarray(origin)
        self._axis = np.asarray(axis)
        self._theta_degree = 0
        self._theta = 0

    def draw(self):
        glPushMatrix()
        self._translate()

        self._rotate()

        if self.vertices is not None and self.edges is not None:
            self._draw_edges()
            if self.surface is not None:
                self._draw_surfaces()
        glPopMatrix()

    def _draw_edges(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                if self.color is not None:
                    glColor3fv(self.color/2)
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def _draw_surfaces(self):
        glBegin(GL_QUADS)
        for surface in self.surface:
            for vertex in surface:
                if self.color is not None:
                    glColor3fv(self.color)
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def _translate(self):
        glTranslatef(self._origin[0], self._origin[1], self._origin[2])

    def _rotate(self):
        glRotatef(self._theta_degree, self._axis[0], self._axis[1], self._axis[2])

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = np.asarray(value)

    @property
    def origin(self):
        return self.origin

    @origin.setter
    def origin(self, value):
        self._origin = np.asarray(value)

    @property
    def axis(self):
        return self._axis

    @axis.setter
    def axis(self, value):
        self._axis = np.asarray(value)

    @property
    def theta(self):
        return self._theta

    @theta.setter
    def theta(self, value):
        self._theta = value
        self._theta_degree = 180 * (value / np.pi)
        if self._theta_degree > 360:
            self._theta_degree -= 360

    @property
    def theta_degree(self):
        return self._theta_degree

    @theta_degree.setter
    def theta_degree(self, value):
        self._theta_degree = value
        self._theta = np.pi*(value/180)
        if self._theta > 2*np.pi:
            self._theta -= 2*np.pi


class Cube(Solids):
    def __init__(self,
                 color=(1, 1, 1),
                 origin=(0, 0, -5),
                 axis=(0, 0, 0),
                 size=1):

        cube_vertices = np.array([[size/2, -size/2, -size/2],
                                  [size/2, size/2, -size/2],
                                  [-size/2, size/2, -size/2],
                                  [-size/2, -size/2, -size/2],
                                  [size/2, -size/2, size/2],
                                  [size/2, size/2, size/2],
                                  [-size/2, -size/2, size/2],
                                  [-size/2, size/2, size/2]])

        cube_edges = np.array([[0, 1],
                               [0, 3],
                               [0, 4],
                               [2, 1],
                               [2, 3],
                               [2, 7],
                               [6, 3],
                               [6, 4],
                               [6, 7],
                               [5, 1],
                               [5, 4],
                               [5, 7]])
        surfaces = ((0, 1, 2, 3),
                    (3, 2, 7, 6),
                    (6, 7, 5, 4),
                    (4, 5, 1, 0),
                    (1, 5, 7, 2),
                    (4, 0, 3, 6))

        super().__init__(vertices=cube_vertices,
                         edges=cube_edges,
                         surfaces=surfaces,
                         color=color,
                         origin=origin,
                         axis=axis,
                         size=size)

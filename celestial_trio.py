import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)

# Set up OpenGL
glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, width / float(height), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)

# Set up the initial camera position
gluLookAt(0, -10, 10, 0, 0, 0, 0, 0, 1)

# Constants for the objects
sun_radius = 1.5
earth_radius = 0.5
moon_radius = 0.2
earth_distance = 5.0
moon_distance = 1.5

# Variables for the animation
sun_angle = 0
earth_angle = 0
moon_angle = 0

# Function to draw a sphere
def draw_sphere(radius):
    quad = gluNewQuadric()
    gluSphere(quad, radius, 32, 32)

# Function to handle the display
def display():
    global sun_angle, earth_angle, moon_angle

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw the Sun
    glColor3f(1.0, 1.0, 0.0)
    glPushMatrix()
    glRotatef(sun_angle, 0, 0, 1)
    draw_sphere(sun_radius)
    glPopMatrix()

    # Draw the Earth
    glColor3f(0.0, 0.0, 1.0)
    glPushMatrix()
    glRotatef(earth_angle, 0, 0, 1)
    glTranslatef(earth_distance, 0, 0)
    draw_sphere(earth_radius)

    # Draw the Moon
    glColor3f(0.7, 0.7, 0.7)
    glRotatef(moon_angle, 0, 0, 1)
    glTranslatef(moon_distance, 0, 0)
    draw_sphere(moon_radius)
    glPopMatrix()

    # Update the angles (slower revolution speed)
    sun_angle += 0.05
    earth_angle += 0.03
    moon_angle += 0.1

    # Swap the buffers
    pygame.display.flip()

# Main loop
while True:
    # Process Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Render the scene
    display()


import pygame as pyg
import hs_drmgame as hsd

pyg.init()

is_running = True
clock = pyg.time.Clock()
fps = 60

screen = pyg.display.set_mode([800, 600])
pyg.display.set_caption("Dreams")

while is_running:
    for e in pyg.event.get():
        if e.type == pyg.QUIT:
            is_running = False
    # Drawing
    screen.fill((255, 255, 255))

    # Updating
    pyg.display.update()

pyg.quit()
exit()

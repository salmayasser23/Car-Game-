import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import math as m
import random

segment_h      = 12.0
lane_positions = [-3.0, -1.0, 1.0, 3.0]
num_cars       = 10
START_Y        = -2.65
WIN_SCORE = 300

def init_enemies():
    global enemy_cars
    enemy_cars = []
    
    rows = (num_cars + len(lane_positions) - 1) // len(lane_positions)
    slots = []
    for lane in lane_positions:
        for r in range(1, rows + 1):
            y = START_Y + r * segment_h
            slots.append((lane, y))
    random.shuffle(slots)
    for x, y in slots[:num_cars]:
        speed = random.uniform(0.03, 0.06)
        color = (random.random(), random.random(), random.random())
        enemy_cars.append({'x': x, 'y': y, 'speed': speed, 'color': color})



def Point(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def Rectangle(x1, y1, x2, y2, r, g, b):
    glBegin(GL_QUADS)
    glColor3f(r, g, b)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()

def Line(a, b, c, d, r, g, B):
    glColor3f(r, g, B)
    glLineWidth(4)
    glBegin(GL_LINES)
    glVertex2f(a, b)
    glVertex2f(c, d)
    glEnd()

def draw_circle(radius, cx, cy, r, g, b, num_segments=360):
    glColor3f(r, g, b)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        angle = 2.0 * m.pi * i / num_segments
        x = cx + radius * m.cos(angle)
        y = cy + radius * m.sin(angle)
        glVertex2f(x, y)
    glEnd()

def Triangle(a, b, c, d, e, f, r, g, B):
    glColor3f(r, g, B)
    glBegin(GL_TRIANGLES)
    glVertex2f(a, b)
    glVertex2f(c, d)
    glVertex2f(e, f)
    glEnd()

def draw_semi_circle(radius, cx, cy, r, g, b, num_segments=180):
    glColor3f(r, g, b)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(num_segments + 1):
        angle = m.pi * i / num_segments
        x = cx + radius * m.cos(angle)
        y = cy + radius * m.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_reversed_semi_circle(radius, cx, cy, r, g, b, num_segments=180):
    glColor3f(r, g, b)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(num_segments + 1):
        angle = m.pi + (m.pi * i / num_segments)
        x = cx + radius * m.cos(angle)
        y = cy + radius * m.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_dashed_line(x, y_start, y_end, dash_len=0.5, gap=0.3, r=1.0, g=1.0, b=1.0):
    current_y = y_start
    while current_y < y_end:
        dash_end = min(current_y + dash_len, y_end)
        Line(x, current_y, x, dash_end, r, g, b)
        current_y = dash_end + gap


def draw_sports_car(x, y, r, g, b):
    old_cx, old_cy = -3.1, -2.65
    dx, dy = x - old_cx, y - old_cy
    draw_semi_circle(0.55, -3.1+dx, -1.7+dy, r,g,b)
    Triangle(-3.6+dx, -1.7+dy, -2.6+dx, -1.7+dy, -3.1+dx, -2.7+dy, 0,0,0)
    Triangle(-3.6+dx, -3.1+dy, -2.6+dx, -3.1+dy, -3.0+dx, -2.2+dy, 0,0,0)
    Triangle(-3.6+dx, -1.7+dy, -3.6+dx, -3.1+dy, -3.0+dx, -2.4+dy, 0,0,0)
    Triangle(-2.6+dx, -1.7+dy, -2.6+dx, -3.1+dy, -3.0+dx, -2.4+dy, 0,0,0)
    Rectangle(-3.5+dx, -2.9+dy, -2.7+dx, -2.0+dy, r,g,b)
    Line(-3.5+dx, -2.0+dy, -3.6+dx, -1.7+dy, r,g,b)
    Line(-2.7+dx, -2.0+dy, -2.6+dx, -1.7+dy, r,g,b)
    Line(-3.5+dx, -2.9+dy, -3.6+dx, -3.1+dy, r,g,b)
    Line(-2.7+dx, -2.9+dy, -2.6+dx, -3.1+dy, r,g,b)
    Line(-3.6+dx, -1.7+dy, -2.6+dx, -1.7+dy, r,g,b)
    Rectangle(-3.6+dx, -3.1+dy, -2.6+dx, -3.5+dy, 0,0,0)
    Triangle(-3.5+dx, -2.9+dy, -2.7+dx, -2.9+dy, -3.1+dx, -3.5+dy, 0,0,0)
    Line(-3.6+dx, -1.7+dy, -3.6+dx, -3.1+dy, r,g,b)
    Line(-2.6+dx, -1.7+dy, -2.6+dx, -3.1+dy, r,g,b)
    draw_reversed_semi_circle(0.55, -3.1+dx, -3.4+dy, r,g,b)
    Line(-3.6+dx, -3.1+dy, -3.6+dx, -3.6+dy, r,g,b)
    Line(-2.6+dx, -3.1+dy, -2.6+dx, -3.6+dy, r,g,b)

def draw_scene(car_x, car_y):
    half_tiles = 25
    for i in range(-half_tiles, half_tiles + 1):
        base = i * segment_h
        Rectangle(-8.0, base-6.0, -4.0, base+6.0, 0.13, 0.55, 0.13)
        Rectangle( 4.0, base-6.0,  8.0, base+6.0, 0.13, 0.55, 0.13)
        Rectangle(-4.0, base-6.0,  4.0, base+6.0, 0.30, 0.30, 0.30)
        Line(-4.0, base-6.0, -4.0, base+6.0, 1.0,1.0,0.0)
        Line( 4.0, base-6.0,  4.0, base+6.0, 1.0,1.0,0.0)
        for x in (-2.0, 0.0, 2.0):
            draw_dashed_line(x, base-6.0, base+6.0)
    for e in enemy_cars:
        draw_sports_car(e['x'], e['y'], *e['color'])
    draw_sports_car(car_x, car_y,1,0,0)

def draw_flag_top_view(x, y, flip=False):
    Rectangle(x - 0.05, y, x + 0.05, y + 1.0, 0.4, 0.4, 0.4)
    draw_circle(0.1, x, y, 0.2, 0.2, 0.2)

    if not flip:
        
        Triangle(x + 0.05, y + 0.9, x + 0.6, y + 0.8, x + 0.05, y + 0.7, 1.0, 0, 0)
    else:
        
        Triangle(x - 0.05, y + 0.9, x - 0.6, y + 0.8, x - 0.05, y + 0.7, 1.0, 0, 0)

def draw_start_line(y, square_width=0.5, square_height=0.3):
    x_start = -4.0
    x_end = 4.0
    x = x_start
    toggle = True  

    while x < x_end:
        r, g, b = (1.0, 1.0, 1.0) if toggle else (0.0, 0.0, 0.0)
        Rectangle(x, y, x + square_width, y + square_height, r, g, b)
        toggle = not toggle
        x += square_width

def rotate_car_in_place(angle):
    glPushMatrix()
    glTranslatef(0, START_Y, 0)
    
    glRotatef(angle, 0.0, 0.0, 1.0)
    
    glTranslatef(0, -START_Y, 0)
    
    draw_sports_car(0, START_Y, 0.0, 0.8, 1.0)
    glPopMatrix()

def tire_barrier():
    for i in range(4):
        y = START_Y - 1 + i * 0.4

        draw_circle(0.15, -4.2, y, 0, 0, 0)  
        draw_circle(0.05, -4.2, y, 0.5, 0.5, 0.5) 

        draw_circle(0.15, 4.2, y, 0, 0, 0)
        draw_circle(0.05, 4.2, y, 0.5, 0.5, 0.5)

def check_collision(car_x, car_y, enemies):
    for e in enemies:
        if abs(e['x'] - car_x) < 1.0 and abs(e['y'] - car_y) < 2.5:
            return True
    return False

def show_message(message,font, display):
            go_surf = font.render(message, True, (0,0,0), (255,255,255))
            w, h   = go_surf.get_size()
            go_data = pg.image.tostring(go_surf, "RGBA", True)
            glWindowPos2d(display[0]//2 - w//2, display[1]//2 + 20)
            glDrawPixels(w, h, GL_RGBA, GL_UNSIGNED_BYTE, go_data)

            
            pa_surf = font.render("Play Again?  Y/N", True, (0,0,0), (255,255,255))
            w2, h2  = pa_surf.get_size()
            pa_data = pg.image.tostring(pa_surf, "RGBA", True)
            glWindowPos2d(display[0]//2 - w2//2, display[1]//2 - 20)
            glDrawPixels(w2, h2, GL_RGBA, GL_UNSIGNED_BYTE, pa_data)

            pg.display.flip()
            pg.time.wait(500)

            
            while True:
                ev = pg.event.wait()
                if ev.type == pg.QUIT:  return
                if ev.type == pg.KEYDOWN:
                    if ev.key == pg.K_y:  return main()
                    if ev.key == pg.K_n:  return



def update_enemy_positions(car_y):
    
    for e in enemy_cars:
        next_y = e['y'] + e['speed']
        
        ahead = None
        best_dist = float('inf')
        for o in enemy_cars:
            if o is not e and o['x']==e['x'] and o['y']>e['y']:
                dist = o['y'] - e['y']
                if dist < best_dist:
                    best_dist, ahead = dist, o
        
        if ahead and next_y > ahead['y'] - segment_h:
            e['y'] = ahead['y'] - segment_h
        else:
            e['y'] = next_y
        
        if e['y'] < car_y - 6.0:
            while True:
                tiles_ahead = random.randint(2, 5)
                new_y = car_y + tiles_ahead * segment_h
                new_x = random.choice(lane_positions)
                if not any(o is not e and o['x']==new_x and abs(o['y']-new_y)<segment_h
                           for o in enemy_cars):
                    break
            e['x'], e['y'] = new_x, new_y
            e['color'] = (random.random(), random.random(), random.random())
        
        ahead = None
        best_dist = float('inf')
        for o in enemy_cars:
            if o is not e and o['x']==e['x'] and o['y']>e['y']:
                dist = o['y'] - e['y']
                if dist < best_dist:
                    best_dist, ahead = dist, o
        if ahead:
            e['speed'] = random.uniform(0.03, max(0.03, ahead['speed'] - 0.001))
        else:
            e['speed'] = random.uniform(0.03, 0.06)

def main():
    pg.init()
    pg.mixer.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)


    pg.mixer.music.load("sound/car.mp3")
    pg.mixer.music.set_volume(0.2)
    pg.mixer.music.play(loops=-1)

    crash_sound = pg.mixer.Sound(r"sound/crash.mp3")
    crash_sound.set_volume(0.4)

    glClearColor(0.87, 0.73, 0.67, 1.0)

    font = pg.font.SysFont('Arial', 32, bold=True)
    score = 0
    speed_timer = 0
    target_volume = 0.2
    current_volume = 0.2

    angle = 0
    clock = pg.time.Clock()

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)

    init_enemies()


    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, -START_Y, -10.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_scene(-3.1, START_Y)
    draw_flag_top_view(-4.5, START_Y + 1.5)
    draw_flag_top_view( 4.5, START_Y + 1.5, True)
    draw_start_line(START_Y + 1.6)
    tire_barrier()
    draw_sports_car(3, START_Y, 1.0, 0.1, 0.5)


    start_msg = font.render("PRESS ENTER TO START", True, (0, 0, 0), (255, 255, 255))
    w, h = start_msg.get_size()
    data = pg.image.tostring(start_msg, "RGBA", True)
    glWindowPos2d(display[0]//2 - w//2, display[1] - 50)
    glDrawPixels(w, h, GL_RGBA, GL_UNSIGNED_BYTE, data)
    pg.display.flip()

    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                waiting = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, -START_Y, -10.0)

        draw_scene(-3.1, START_Y)
        draw_flag_top_view(-4.5, START_Y + 1.5)
        draw_flag_top_view( 4.5, START_Y + 1.5, True)
        draw_start_line(START_Y + 1.6)
        tire_barrier()
        draw_sports_car(3, START_Y, 1.0, 0.1, 0.5)

        rotate_car_in_place(angle)
        glWindowPos2d(display[0]//2 - w//2, display[1] - 50)
        glDrawPixels(w, h, GL_RGBA, GL_UNSIGNED_BYTE, data)
        pg.display.flip()

        angle = (angle + 2) % 360
        clock.tick(60)

    clock = pg.time.Clock()
    car_x, car_y = -3.1, -2.65
    forward_spd = 0.05
    steer_spd = 0.05
    lane_min = -3.5
    lane_max = 3.5

    while True:
        clock.tick(60)
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                return

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            car_x -= steer_spd
        if keys[pg.K_RIGHT]:
            car_x += steer_spd
        if keys[pg.K_UP]:
            car_y += forward_spd
            score += 0.1
            speed_timer += 1

        target_volume = 0.8 if keys[pg.K_UP] else 0.2
        if abs(current_volume - target_volume) > 0.01:
            current_volume += (target_volume - current_volume) * 0.1
            pg.mixer.music.set_volume(current_volume)

        car_x = max(lane_min, min(lane_max, car_x))

        if speed_timer >= 300:
            forward_spd += 0.005
            speed_timer = 0

        update_enemy_positions(car_y)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, -car_y, -10.0)

        glClear(GL_COLOR_BUFFER_BIT)
        draw_scene(car_x, car_y)

        display_score = f"{score:.1f}"
        surf = font.render(display_score, True, (0, 0, 0), (255, 255, 255))
        w2, h2 = surf.get_size()
        data2 = pg.image.tostring(surf, "RGBA", True)
        glWindowPos2d(10, 10)
        glDrawPixels(w2, h2, GL_RGBA, GL_UNSIGNED_BYTE, data2)

        if score >= WIN_SCORE:
            pg.mixer.music.fadeout(500)
            if show_message("YOU WIN!", font, display):
                return main()
            else:
                return

        if check_collision(car_x, car_y, enemy_cars):
            pg.mixer.music.fadeout(500)
            crash_sound.play()
            if show_message("GAME OVER", font, display):
                return main()
            else:
                return

        pg.display.flip()

    pg.quit()

main()

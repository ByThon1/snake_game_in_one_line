[
    exec("import pygame"),
    exec("import random"),
    pygame.init(),
    back := (192,192,192),
    gameDisplay := pygame.display.set_mode((800,600)),
    pygame.display.set_caption('A bit Racey'),
    gameDisplay.fill(back),
    clock := pygame.time.Clock(),
    running := True,
    kuyruk := [[200,100],[180,100],[160,100],[140,100],[120,100],[100,100]],
    rotation := "right",
    random_apple := lambda: [random.randint(0,39)*20,random.randint(0,29)*20],
    apple := random_apple(),
    score := 0,
    tick_speed := 10,
    [[
        gameDisplay.fill(back),
        _event := pygame.event.get(),
        running := any([event.type == pygame.QUIT for event in _event]),
        [print(f"Game Over\nScore - {score}\nLength - {len(kuyruk)}"),running := True] if not 0 <= kuyruk[0][0] < 800 or not 0 <= kuyruk[0][1] < 600 else None,
        [[
            [[[rotation := "up"] if event.key == pygame.K_w else [rotation := "down"] if event.key == pygame.K_s else [rotation := "left"] if event.key == pygame.K_a else [rotation := "right"] if event.key == pygame.K_d else None] if event.type == pygame.KEYDOWN else None]

        ] for event in _event],
        [[quit()] if running else None],
        [kuyruk.insert(0,[kuyruk[0][0]+20,kuyruk[0][1]]),kuyruk.pop()] if rotation == "right" else None,
        [kuyruk.insert(0,[kuyruk[0][0]-20,kuyruk[0][1]]),kuyruk.pop()] if rotation == "left" else None,
        [kuyruk.insert(0,[kuyruk[0][0],kuyruk[0][1]-20]),kuyruk.pop()] if rotation == "up" else None,
        [kuyruk.insert(0,[kuyruk[0][0],kuyruk[0][1]+20]),kuyruk.pop()] if rotation == "down" else None,
        [[pygame.draw.rect(gameDisplay,(0,255,0) if i == kuyruk[0] else (11,11,11),pygame.Rect(i[0],i[1],20,20)),] for i in kuyruk],

        [
            [apple := random_apple()],
            kuyruk.append([0,0]),
            score := score + 1,
        ] if kuyruk[0] == apple else None,
        pygame.draw.rect(gameDisplay,(255,0,0),pygame.Rect(apple[0],apple[1],20,20)),
        pygame.display.set_caption(f"Score - {score:_>3}  Length - {len(kuyruk)}"),

        pygame.display.update(),
        clock.tick(tick_speed),
    ] for _ in iter(int,1)]
]

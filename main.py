import random
import pygame

from pip._vendor.distlib.compat import raw_input

desc = input('Scegli un numero tra 1(IMPICCATO),2(TRIS) e 3(PING PONG) per iniziare a giocare !')
if desc == '1':  # GIOCO DELL'IMPICCATO
    def carica_parole():  # funzione che mi prende da un file tutte le parole che possono capitare. Il file deve contenere una parola per riga
        lista_di_parole = []
        with open('PAROLE.txt', 'r') as f:
            for line in f:
                parola = line.rstrip('\n')
                lista_di_parole.append(parola)
        return lista_di_parole


    def parola_random(lista_di_parole):  # funzione che prende a caso una delle parole presenti nel file
        return random.choice(lista_di_parole)


    def visualizza_parola(lista_lettere):
        print(' '.join(lettera for lettera in lista_lettere))


    def aggiorna_lettere_indovinate(parola, scelta, lettere_indovinate):
        for i, lettera in enumerate(parola):
            if lettera == scelta:
                lettere_indovinate[i] = lettera
        return lettere_indovinate


    def show_player_life():
        life = """
    ---
    """
        yield life

        life = """
    |----
    |
    |
    |
    |
    ---
    """
        yield life
        life = """
    |----0
    |    |
    |    |
    |    |
    |    |
    ---
    """
        yield life

        life = """
    |----O
    |    |
    |   /|\
    |    |
    |    |
    ---
    """

        yield life

        life = """
    |----O
    |    |
    |   /|\
    |    |
    |   /|\
    ---
    """

        yield life
        life = """

    |--\
    |   \O
    |    |
    |   /|\
    |    |
    --- /|\
    """
        yield life


    lista_di_parole = carica_parole()
    parola_da_indovinare = parola_random(lista_di_parole)
    lettere_indovinate = ['_' for lettera in parola_da_indovinare]
    vita_giocatore = show_player_life()

    visualizza_parola(lettere_indovinate)

    while True:
        scelta = input("Inserisci una lettera -> ")
        if scelta in parola_da_indovinare:
            lettere_indovinate = aggiorna_lettere_indovinate(parola_da_indovinare, scelta, lettere_indovinate)
            if parola_da_indovinare == ''.join(lettera for lettera in lettere_indovinate):
                print("Hai vinto, complimenti! La parola è: {0}".format(parola_da_indovinare))
                break
        else:
            try:
                print(next(vita_giocatore))
            except StopIteration:
                print("Hai perso, la parola era: {0}".format(parola_da_indovinare))
                break

        visualizza_parola(lettere_indovinate)
elif desc == '2':
    # Il programma inizia ponendo tutte le nove variabili uguali a 'x'.
    a1 = 'x'
    a2 = 'x'
    a3 = 'x'
    b1 = 'x'
    b2 = 'x'
    b3 = 'x'
    c1 = 'x'
    c2 = 'x'
    c3 = 'x'


    # Poi visualizza la scacchiera
    def scacchiera():
        print('\t 1 \t 2 \t 3 \n')
        print('a \t', a1, '\t', a2, '\t', a3, '\n')
        print('b \t', b1, '\t', b2, '\t', b3, '\n')
        print('c \t', c1, '\t', c2, '\t', c3, '\n')


    def vittoria(n):
        if ((a1 == n and a2 == n and a3 == n) or (b1 == n and b2 == n and b3 == n) or
                (c1 == n and c2 == n and c3 == n) or
                (a1 == n and b1 == n and c1 == n) or (a2 == n and b2 == n and c2 == n) or
                (a3 == n and b3 == n and c3 == n) or
                (a1 == n and b2 == n and c3 == n) or (a3 == n and b2 == n and c1 == n)):
            EsisteVincitore = 'si'
        else:
            EsisteVincitore = 'no'
            return EsisteVincitore


    scacchiera()
    nmosse = 0
    partitafinita = 'no'
    # Poi informa che muoverà prima “N”.
    print('Il primo giocatore sarà N \n')
    print('Muova N \n')
    mossafatta = 'no'
    x = raw_input('Dove vuoi scrivere N: a1, a2, a3, b1, b2, b3, c1, c2, c3? \n')
    if x == 'a1' and a1 == 'x':
        a1 = 'N'
        mossafatta = 'si'

    while nmosse < 9:
        print('Muova N \n')
        mossafatta = 'no'
        x = raw_input('Dove vuoi scrivere N: a1, a2, a3, b1, b2, b3, c1, c2, c3 \n')
        if x == 'a1' and a1 == 'x':
            a1 = 'N'
            mossafatta = 'si'
        elif x == 'a2' and a2 == 'x':
            a2 = 'N'
            mossafatta = 'si'
        elif x == 'a3' and a3 == 'x':
            a3 = 'N'
            mossafatta = 'si'
        elif x == 'b1' and b1 == 'x':
            b1 = 'N'
            mossafatta = 'si'
        elif x == 'b2' and b2 == 'x':
            b2 = 'N'
            mossafatta = 'si'
        elif x == 'b3' and b3 == 'x':
            b3 = 'N'
            mossafatta = 'si'
        elif x == 'c1' and c1 == 'x':
            c1 = 'N'
            mossafatta = 'si'
        elif x == 'c2' and c2 == 'x':
            c2 = 'N'
            mossafatta = 'si'
        elif x == 'c3' and c3 == 'x':
            c3 = 'N'
            mossafatta = 'si'

        if mossafatta == 'no':
            print('SQUALIFICATO!')
            partitafinita = 'si'
            nmosse = 10
            scacchiera()
            nmosse = nmosse + 1
            partitafinita = vittoria('N')
        if partitafinita == 'si':
            print('Ha vinto N \n')
            nmosse = 10
        elif nmosse == 9:
            print('PAREGGIO')
            nmosse = 10

        if partitafinita == 'no' and nmosse < 9:
            nmosse = nmosse + 1
            mossafatta = 'no'
            print('La mossa tocca a R \n')
            x = raw_input('Dove vuoi scrivere R: a1, a2, a3, b1, b2, b3, c1, c2, c3? \n')
        if x == 'a1' and a1 == 'x':
            a1 = 'R'
            mossafatta = 'si'
        elif x == 'a2' and a2 == 'x':
            a2 = 'R'
            mossafatta = 'si'
        elif x == 'a3' and a3 == 'x':
            a3 = 'R'
            mossafatta = 'si'
        elif x == 'b1' and b1 == 'x':
            b1 = 'R'
            mossafatta = 'si'
        elif x == 'b2' and b2 == 'x':
            b2 = 'R'
            mossafatta = 'si'
        elif x == 'b3' and b3 == 'x':
            b3 = 'R'
            mossafatta = 'si'
        elif x == 'c1' and c1 == 'x':
            c1 = 'R'
            mossafatta = 'si'
        elif x == 'c2' and c2 == 'x':
            c2 = 'R'
            mossafatta = 'si'
        elif x == 'c3' and c3 == 'x':
            c3 = 'R'
            mossafatta = 'si'
        if mossafatta == 'no':
            print('SQUALIFICATO!')
            partitafinita = 'si'
            nmosse = 10
            scacchiera()
            partitafinita = vittoria('R')
        if partitafinita == 'si':
            print('Ha vinto R \n')
            nmosse = 10

elif desc == '3':
    pygame.init()
    # Window setup
    win = pygame.display.set_mode((750, 500))
    pygame.display.set_caption('Pong')
    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    # Sprite Classes
    class Paddle1(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([10, 75])
            self.image.fill(white)
            self.rect = self.image.get_rect()
            self.points = 0
    class Paddle2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([10, 75])
            self.image.fill(white)
            self.rect = self.image.get_rect()
            self.points = 0
    class Ball(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([10, 10])
            self.image.fill(white)
            self.rect = self.image.get_rect()
            self.speed = 10
            self.dx = 1
            self.dy = 1
    # Sprite Creation
    paddle1 = Paddle1()
    paddle1.rect.x = 25
    paddle1.rect.y = 225
    paddle2 = Paddle2()
    paddle2.rect.x = 715
    paddle2.rect.y = 225
    paddle_speed = 10
    pong = Ball()
    pong.rect.x = 375
    pong.rect.y = 250
    all_sprites = pygame.sprite.Group()
    all_sprites.add(paddle1, paddle2, pong)
    def redraw():
        win.fill(black)
        # Title font
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render('PONG', False, white)
        textRect = text.get_rect()
        textRect.center = (750 // 2, 25)
        win.blit(text, textRect)
        # Player 1 Score
        p1_score = font.render(str(paddle1.points), False, white)
        p1Rect = p1_score.get_rect()
        p1Rect.center = (50, 50)
        win.blit(p1_score, p1Rect)
        # Player 2 Score
        p2_score = font.render(str(paddle2.points), False, white)
        p2Rect = p2_score.get_rect()
        p2Rect.center = (700, 50)
        win.blit(p2_score, p2Rect)
        # Updates all Sprites
        all_sprites.draw(win)
        # Draws updates
        pygame.display.update()
    run = True

    while run:
        pygame.time.delay(100)
        # Quit Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Paddle Movement
        key = pygame.key.get_pressed()
        if key[pygame.K_w]: #muovi paddle destra con w per sopa
            paddle1.rect.y += -paddle_speed
        if key[pygame.K_s]: #muovi paddle destra con s per sotto
            paddle1.rect.y += paddle_speed
        if key[pygame.K_UP]:#muovi paddle sinistra con freccia up per sopra
            paddle2.rect.y += -paddle_speed
        if key[pygame.K_DOWN]:#muovi paddle destra con freccia down per sotto
            paddle2.rect.y += paddle_speed
        # Moves pong ball
        pong.rect.x += pong.speed * pong.dx
        pong.rect.y += pong.speed * pong.dy
        if pong.rect.y > 490:
            pong.dy = -1
        if pong.rect.y < 1:
            pong.dy = 1
        if pong.rect.x > 740:
            pong.rect.x, pong.rect.y = 375, 250
            pong.dx = -1
            paddle1.points += 1
        if pong.rect.x < 1:
            pong.rect.x, pong.rect.y = 375, 250
            pong.dx = 1
            paddle2.points += 1
        if paddle1.rect.colliderect(pong.rect):
            pong.dx = 1
        if paddle2.rect.colliderect(pong.rect):
            pong.dx = -1
        redraw()
    pygame.quit()


if desc != '1' and desc != '2'and desc != '3':
    print('Gioco non presente.')

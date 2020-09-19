import random
import pygame
#boh
desc = input('Scegli un numero tra 1(IMPICCATO),2(TRIS) e 3(PING PONG) per iniziare a giocare !')
#CIAO RICCARDOOOOOOOOOOOO
if desc == '1':  # GIOCO DELL'IMPICCATO
    def carica_parole():
        lista_di_parole = []
        with open("PAROLE.txt", 'r') as f:
            for line in f:
                parola = line.rstrip('\n')
                lista_di_parole.append(parola)
        return lista_di_parole


    def parola_random(lista_di_parole):
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


elif desc == '2':       #TRIS
    theBoard = {'1': ' ', '2': ' ', '3': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '7': ' ', '8': ' ', '9': ' '}

    board_keys = []

    for key in theBoard:
        board_keys.append(key)

   #Stampiamo il tabellone aggiornato dopo ogni mossa. Creiamo una funzione in cui definiamo printBoard in modo che stampa il tabellone ogni volta che si chiama la funzione

    def printBoard(board):
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])


  #Ora scriveremo la funzione principale che ha tutte le funzionalità di gioco
    def game():
        turn = 'X'
        count = 0

        for i in range(10):
            printBoard(theBoard)
            print("E' il tuo turno," + turn + ".Muovi in una casalla  compresa da 1 a 9 partendo dall'alto?")

            move = input()

            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                print("Ops! Casella già piena.\nMuovi in un altro posto")
                continue

            # Ora controlleremo se il giocatore X o O ha vinto, per ogni mossa dopo 5 mosse
            if count >= 5:
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " VINTO. ****")
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " VINTO. ****")
                    break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " VINTO. ****")
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " VINTO. ****")
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " VINTO. ****")
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " VINTO. ****")
                    break
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " VINTO. ****")
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " VINTO. ****")
                    break

            #Se né X né O vincono e il tabellone è pieno, dichiareremo il risultato come "pareggio".
            if count == 9:
                print("\nGame Over.\n")
                print("PAREGGIO!!")

            # Cambiamo giocatore dopo ogni mossa
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

        #Ora chiederemo se il giocatore vuole riavviare il gioco o meno
        restart = input("Vuoi giocare ancora?y/n")
        if restart == "y" or restart == "Y":
            for key in board_keys:
                theBoard[key] = " "

            game()


    if __name__ == "__main__":
        game()

elif desc == '3':       # PING PONG
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
        if key[pygame.K_w]: #muovi paddle destra con w per sopra
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
        if paddle1.points==3 :
            pong.rect.x=0
            pong.rect.y=0
            print("The winner is Player1")
            pygame.quit()
        if paddle2.points == 3:
           pong.rect.x = 0
           pong.rect.y=0
           print("The winner is Player2")
           pygame.quit()

if desc != '1' and desc != '2'and desc != '3':
    print('Gioco non presente.')

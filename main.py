import pygame, os, random, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")


        #  Variables for Game
        gameWidth = 1280
        gameHeight = 720
        picSize = 128
        gameColumns = 5
        gameRows = 4
        padding = 10
        leftMargin = (gameWidth - ((picSize + padding) * gameColumns)) // 2
        rightMargin = leftMargin
        topMargin = (gameHeight - ((picSize + padding) * gameRows)) // 2
        bottomMargin = topMargin
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        selection1 = None
        selection2 = None


        # Loading the pygame screen.
        screen = pygame.display.set_mode((gameWidth, gameHeight))
        pygame.display.set_caption('Match Cards Game')
        gameIcon = pygame.image.load('images/Apple.png')
        pygame.display.set_icon(gameIcon)

        # Load the BackGround image into Python
        bgImage = pygame.image.load('Background.png')
        bgImage = pygame.transform.scale(bgImage, (gameWidth, gameHeight))
        bgImageRect = bgImage.get_rect()

        # Create list of Memory Pictures
        memoryPictures = []
        for item in os.listdir('images/'):
            memoryPictures.append(item.split('.')[0])
        memoryPicturesCopy = memoryPictures.copy()
        memoryPictures.extend(memoryPicturesCopy)
        memoryPicturesCopy.clear()
        random.shuffle(memoryPictures)

        # Load each of the images into the python memory
        memPics = []
        memPicsRect = []
        hiddenImages = []
        for item in memoryPictures:
            picture = pygame.image.load(f'images/{item}.png')
            picture = pygame.transform.scale(picture, (picSize, picSize))
            memPics.append(picture)
            pictureRect = picture.get_rect()
            memPicsRect.append(pictureRect)

        for i in range(len(memPicsRect)):
            memPicsRect[i][0] = leftMargin + ((picSize + padding) * (i % gameColumns))
            memPicsRect[i][1] = topMargin + ((picSize + padding) * (i % gameRows))
            hiddenImages.append(False)

        print(memoryPictures)
        print(memPics)
        print(memPicsRect)
        print(hiddenImages)

        gameLoop = True
        while gameLoop:
            # Load background image
            screen.blit(bgImage, bgImageRect)

            # Input events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for item in memPicsRect:
                        if item.collidepoint(event.pos):
                            if hiddenImages[memPicsRect.index(item)] != True:
                                if selection1 != None:
                                    selection2 = memPicsRect.index(item)
                                    hiddenImages[selection2] = True
                                else:
                                    selection1 = memPicsRect.index(item)
                                    hiddenImages[selection1] = True

            for i in range(len(memoryPictures)):
                if hiddenImages[i] == True:
                    screen.blit(memPics[i], memPicsRect[i])
                else:
                    pygame.draw.rect(screen, WHITE, (memPicsRect[i][0], memPicsRect[i][1], picSize, picSize))
            pygame.display.update()

            if selection1 != None and selection2 != None:
                if memoryPictures[selection1] == memoryPictures[selection2]:
                    selection1, selection2 = None, None
                else:
                    pygame.time.wait(1000)
                    hiddenImages[selection1] = False
                    hiddenImages[selection2] = False
                    selection1, selection2 = None, None

            win = 1
            for number in range(len(hiddenImages)):
                win *= hiddenImages[number]

            if win == 1:
                gameLoop = False







            pygame.display.update()

        pygame.quit()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()





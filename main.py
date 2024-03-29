import pygame
import time

pygame.init()

# Screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

# trash
#trashPosx, trashPosy = 1000, 1000

# Background image
bg = pygame.image.load("images/bgs/bg.png")
screen.blit(bg, (0, 0))

# Character avatar 1
boy1 = pygame.image.load("images/characters/boy1.png")
screen.blit(pygame.transform.scale(boy1, (350, 350)), (170, 150))

# Character avatar 2
boy2 = pygame.image.load("images/characters/boy2.png")
screen.blit(pygame.transform.scale(boy2, (350, 350)), (170, 150))

# Character avatar 3
boy3 = pygame.image.load("images/characters/boy3.png")
screen.blit(pygame.transform.scale(boy3, (350, 350)), (170, 150))

boy = boy1

# Coin rect
rectColor = (0, 0, 0)

# Amount of coins
coinCounter = 9999

# Amount of coins that you gonna get for 1 click
coinsForClick = 1

# click sound
clickSound = pygame.mixer.Sound("sounds/click.ogg")

# click to buy sound
buySound = pygame.mixer.Sound("sounds/button.wav")

# Character lvl
lvl = 1

# Character lvl2 counter
lvl2Counter = False

# Character lvl3 counter
lvl3Counter = False

# Character lvl4 counter
lvl4Counter = False

# Character lvl5 counter
lvl5Counter = False

# Auto Clicker info X multiplier number
autoClickMultiplierX = 1

# Auto Clicker info X multiplier number
multiplierMultiplierX = 1

# Auto Clicker info X multiplier price
autoClickMultiplierPrice = 10

# Multiplier info X multiplier price
MultiplierMultiplierPrice = 10

# Coins info
coins = pygame.font.SysFont('Comic Sans MS', 50)

# AutoClicker rect
autoClick = pygame.Surface((220, 100))
autoClick.set_alpha(200)
autoClick.fill((255, 255, 255))

# Multiplier rect
autoClick = pygame.Surface((220, 100))
autoClick.set_alpha(200)
autoClick.fill((255, 255, 255))

# Auto Clicker info
autoClickInfo = pygame.font.SysFont('Comic Sans MS', 26)
textAutoClicker = autoClickInfo.render("AutoClicker x", False, (0, 0, 0))

# Multiplier info
textMultiplier = autoClickInfo.render("Multiplier x", False, (0, 0, 0))

# BUY Button autoClicker
buyButton = pygame.Surface((180, 50))
buyButton.set_alpha(1000)
buyButton.fill((255, 129, 193))
screen.blit(buyButton, (490, 40))

# BUY Button Text autoClicker
textBUYFor = autoClickInfo.render('BUY for ', False, (255, 255, 255))

# Auto Clicker info X multiplier Price Rect
autoClickMultiplierBack = pygame.Surface((40, 40))
autoClickMultiplierBack.set_alpha(1000)
autoClickMultiplierBack.fill((0, 0, 0))

# lvl info text
textLvl = autoClickInfo.render('LVL:  ', False, (255, 255, 255))

# lvl info text rect
lvlNumberRect = pygame.Surface((40, 40))
lvlNumberRect.set_alpha(1000)
lvlNumberRect.fill((0, 0, 0))

pygame.display.set_caption("clicker")

mainLoop = True

clock = pygame.time.Clock()

'''
def autoClick():
    while True:
        global coinCounter
        coinCounter += 1
        time.sleep(2)
'''

# Автокликер не работает и из за него все вылетает

# Анимировать уведомление о повышении уровня

# Доработать функцию ниже, чтобы она работала в коде игры

'''
# Make long number short
def shorten_number(number_to_shorten):
    postfixes = ['m', 'b', ] # постфиксы для сокращенных чисел
    briefer_nums = [10**k for k in range(6, 6+3*len(postfixes), 3)] # список наших делителей
    for i in reversed(range(len(postfixes))):
        if number_to_shorten > briefer_nums[i]:
            num = number_to_shorten / briefer_nums[i]
            int_part = int(num)
            float_part = str(num - int_part).split('.')[1][:3]
            return str(int_part) + '.' + float_part + postfixes[i]
        else:
            return number_to_shorten
'''

# main loop
while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False

        # left mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos

            # Increase the number of coins
            if 200 < pos[0] < 480 and 180 < pos[1] < 470:
                clickSound.play()
                coinCounter += coinsForClick

            # Increase the number of AutoClickers and change the price
            if 490 < pos[0] < 670 and 40 < pos[1] < 90 and coinCounter >= autoClickMultiplierPrice:
                buySound.play()
                coinCounter -= autoClickMultiplierPrice
                autoClickMultiplierPrice = int(autoClickMultiplierPrice * 1.5)
                autoClickMultiplierX += 1
                # autoClick() code

            # Increase the number of Multipliers and change the price
            elif 490 < pos[0] < 670 and 445 < pos[1] < 495 and coinCounter >= MultiplierMultiplierPrice:
                buySound.play()
                coinCounter -= MultiplierMultiplierPrice
                MultiplierMultiplierPrice = int(MultiplierMultiplierPrice * 1.6)
                multiplierMultiplierX += 1
                if coinsForClick == 1:
                    coinsForClick = 2
                else:
                    coinsForClick = int(coinsForClick * 1.5)

            else:
                break

        # get lvl 2
        if coinCounter >= 1000:
            if lvl2Counter == False:
                lvl += 1
                lvl2Counter = True

        # get lvl 3
        if coinCounter >= 10000:
            if lvl3Counter == False:
                lvl += 1
                lvl3Counter = True

        # get lvl 4
        if coinCounter >= 100000:
            if lvl4Counter == False:
                lvl += 1
                lvl4Counter = True

        # get lvl 5
        if coinCounter >= 1000000:
            if lvl5Counter == False:
                lvl += 1
                lvl5Counter = True

    # number but round
    #coinCounterShort = shorten_number(coinCounter)

    # Draw everything
    screen.blit(bg, (0, 0))

    if coinCounter >= 1000 and coinCounter <= 9999:
        boy = boy2

    elif coinCounter >= 10000 and coinCounter <= 99999:
        boy = boy3

    screen.blit(pygame.transform.scale(boy, (350, 350)), (170, 150))

    textSurface = coins.render(str(coinCounter), False, (235, 235, 235))
    screen.blit(textSurface, (240, -15))

    screen.blit(autoClick, (480, 0))
    screen.blit(autoClick, (480, 400))
    screen.blit(textAutoClicker, (490, -5))
    screen.blit(textMultiplier, (490, 400))

    screen.blit(buyButton, (490, 40))
    screen.blit(buyButton, (490, 445))
    screen.blit(textBUYFor, (490, 40))
    screen.blit(textBUYFor, (500, 450))

    # Auto Clicker info X multiplier Price Rect
    #screen.blit(autoClickMultiplierBack, (610, 47))

    # Auto Clicker info X multiplier
    textAutoClickerInfoX = autoClickInfo.render(str(autoClickMultiplierX), False, (255, 255, 255))
    screen.blit(textAutoClickerInfoX, (660, -3))

    textAutoClickMultiplierPriceInfo = autoClickInfo.render(str(autoClickMultiplierPrice), False, (255, 255, 255))
    screen.blit(textAutoClickMultiplierPriceInfo, (610, 47))

    # Multiplier info X multiplier Price
    textMultiplierMultiplierPriceInfo = autoClickInfo.render(str(MultiplierMultiplierPrice), False, (255, 255, 255))
    screen.blit(textMultiplierMultiplierPriceInfo, (610, 450))

    # Multiplier X info multiplier
    textMultiplierXInfo = autoClickInfo.render(str(multiplierMultiplierX), False, (255, 255, 255))
    screen.blit(textMultiplierXInfo, (640, 400))

    screen.blit(textLvl, (0, 0))
    # lvl info text rect

    # lvl info number
    textlvlNumberInfo = autoClickInfo.render(str(lvl), False, (255, 255, 255))
    screen.blit(textlvlNumberInfo, (60, 0))

    pygame.display.update()

    pygame.display.flip()

    clock.tick(20)

pygame.quit()
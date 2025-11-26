
import pygame
import math
# pygame setup
pygame.init()
screenWidth = 1200
screenHeight = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
screen.fill((79, 91, 102))  # background color
#--------------------------------
fieldWidth = screenWidth * 2/3
fieldHeight = fieldWidth

unscaledField = pygame.image.load("images/field.jpeg").convert_alpha()
unrotatedField = pygame.transform.scale(unscaledField, (int(fieldWidth), int(fieldHeight)))
field = pygame.transform.rotate(unrotatedField, 90)


coordinates = []
steps = []
firstClick = True


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

displayButton = Button(850, 100, pygame.image.load("images/displaySteps.png"), 0.75)


def drawArrow(surface, startPos, endPos):
    color = (0,0,0) 
    lineWidth = 2
    headSize = 10

    pygame.draw.line(surface, color, startPos, endPos, lineWidth) #body of arrow
    #calculate angle of arrow
    angle = math.degrees(math.atan2(endPos[1]-startPos[1], endPos[0]-startPos[0]))
    #calculate the endpoint of the left side of the arrowhead
    leftX = endPos[0] - headSize * math.cos(math.radians(angle - 30))
    leftY = endPos[1] - headSize * math.sin(math.radians(angle - 30))
    #calculate the endpoint of the right side of the arrowhead 
    rightX = endPos[0] - headSize * math.cos(math.radians(angle + 30))
    rightY = endPos[1] - headSize * math.sin(math.radians(angle + 30))
    #draw the two sides of the arrowhead
    pygame.draw.line(surface, color, endPos, (leftX, leftY), lineWidth)
    pygame.draw.line(surface, color, endPos, (rightX, rightY), lineWidth)
    

def printMovement():
    start = coordinates[-2]
    end = coordinates[-1]
    deltaX = end[0] - start[0]
    deltaY = end[1] - start[1]
    distance = math.sqrt(deltaX**2 + deltaY**2)
    angle = math.degrees(math.atan2(deltaY, deltaX))


    #field is 464x464 pixels
    #field is 144x144 inches
    pixelsPerInch = 464 / 144

    distanceInInches = distance / pixelsPerInch
    step = f"Move {distanceInInches:.2f} inches at {angle:.2f} degrees"
    print(step)
    steps.append(step)



running = True

while running:
    # poll for events
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONUP and not firstClick:
            coordinates.append(pygame.mouse.get_pos())

            start = coordinates[-2]
            end = coordinates[-1]
            drawArrow(field, start, end)
            printMovement()
            
        if event.type == pygame.MOUSEBUTTONUP and firstClick:
            firstClick = False
            coordinates.append(pygame.mouse.get_pos())
            pygame.draw.circle(field, (255,0,0), coordinates[0], 6)

    # RENDER YOUR
    screen.blit(field, (0, 0))
    displayButton.draw()
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


        
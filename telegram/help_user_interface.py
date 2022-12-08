import pygame
import camera.image as cam_image
import camera.video as cam_video
from API import API as api
import datetime as dt

import requests

pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)
API_KEY = api.API_MAIN_KEY


class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def revert(self, text, pos, font, bg="black"):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.feedback = self.feedback
        self.feedback = "HELP"
        self.change_text(text, bg)
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        #self.change_text(self.feedback, bg="red")
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(button1.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="green")

    def send_msg(self, event, alert):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    token = API_KEY
                    chat_id = api.CHAT_ID
                    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + alert
                    results = requests.get(url_req)
                    print(results.json())

    def send_photo(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    cam_image.image_monitor()
                    token = API_KEY
                    chat_id = api.CHAT_ID
                    file = {'photo': open("image.jpg", "rb")}
                    url_req = requests.post("https://api.telegram.org/bot" + token + "/sendPhoto?chat_id="
                                            + chat_id, files=file)
                    print(url_req.json())

    def send_video(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    cam_video.video_monitor()
                    token = API_KEY
                    chat_id = api.CHAT_ID
                    file = {'video': open("video.mp4", "rb")}
                    url_req = requests.post("https://api.telegram.org/bot" + token + "/sendVideo?chat_id="
                                            + chat_id, files=file)
                    print(url_req.json())


def mainloop():
    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            button1.click(event)
        button1.show()
        clock.tick(30)
        pygame.display.update()
        button1.send_msg(event, alert="ALERT: HELP " + str(dt.datetime.now()))
        clock.tick(30)
        pygame.display.update()
        button1.send_photo(event)
        button1.send_video(event)
        i += 1
        print(i)
        if i == 1000:
            button1.revert(text="HELP",pos=(250, 300), font=100,
                           bg="red")
            i = 0

button1 = Button(
    "HELP",
    (250, 300),
    font=100,
    bg="red",
    feedback="HELP")

mainloop()

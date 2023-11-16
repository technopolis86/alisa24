import random
import pygame

pygame.init()
pygame.display.set_caption('Загрузка рисунка')
size = width, height = 500, 500
screen = pygame.display.set_mode((size))

# создаем спрайты
all_sprites = pygame.sprite.Group()




def load_image(name, colorkey=None):
    fullname = 'data' + '/' + name
    try:
        image = pygame.image.load(fullname).convert()
    except FileNotFoundError:
        message = f"Файл с изображением '{fullname}' не найден"
        print(message)
        raise SystemExit()

    # обесцветка
    if colorkey:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image('bomb2.png')
    image_boom = load_image('boom.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        while True:
            self.rect.topleft = (random.randint(0, width - self.rect.width),
                                 random.randint(0, height - self.rect.height))
            if len(pygame.sprite.spritecollide(self, all_sprites, False)) == 1:
                break

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            self.image = self.image_boom


def main():
    for i in range(10):
        Bomb(all_sprites)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in all_sprites:
                    bomb.get_event(event)
        screen.fill('white')

        # запускаем всех спрайтов
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
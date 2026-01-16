

def handle_input(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        self.x -= self.speed
    if keys[pygame.K_RIGHT]:
        self.x += self.speed
    if keys[pygame.K_UP]:
        self.y -= self.speed
    if keys[pygame.K_DOWN]:
        self.y += self.speed
    pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
    return pygame.Rect(self.x, self.y, self.width, self.height)

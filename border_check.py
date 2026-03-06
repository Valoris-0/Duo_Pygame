import settings


def check(x, y, width, height):
    if x < 0 or x + width > settings.WIDTH:
        return False
    if y < 0 or y + height > settings.HEIGHT:
        return False
    if x > 360: 
        return False
    if y > 340:
        return False
    return True

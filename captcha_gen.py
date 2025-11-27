import os
import random
import string
import math
from PIL import Image, ImageDraw, ImageFont, ImageOps

class CaptchaGen:
    def __init__(self, output_dir='generated_captchas', width=160, height=60, font_size=40):
        self.output_dir = output_dir
        self.width = width
        self.height = height
        self.font_size = font_size
        os.makedirs(self.output_dir, exist_ok=True)

        # Multiple fonts for variation
        self.fonts = []
        common_fonts = ["arial.ttf", "times.ttf", "calibri.ttf", "verdana.ttf"]

        for f in common_fonts:
            try:
                self.fonts.append(ImageFont.truetype(f, font_size))
            except:
                pass

        if not self.fonts:
            self.fonts = [ImageFont.load_default()]

    def _random_text(self, length=4):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def _add_background_noise(self, img):
        draw = ImageDraw.Draw(img)

        dot_count = random.randint(500, 700)

        for _ in range(dot_count):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            shade = random.randint(60, 120)
            draw.point((x, y), fill=(shade, shade, shade))

        for _ in range(random.randint(6, 10)):
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)

            line_color = (
                random.randint(60, 120),
                random.randint(60, 120),
                random.randint(60, 120)
            )
            draw.line((x1, y1, x2, y2), fill=line_color, width=1)

    def _warp_image(self, img):
        """ Mild sine distortion """
        w, h = img.size
        amplitude = random.uniform(0.5, 2.0)
        frequency = random.uniform(0.02, 0.1)

        warped = Image.new("RGB", (w, h), (255, 255, 255))
        pixels = warped.load()
        src = img.load()

        for x in range(w):
            offset = int(amplitude * math.sin(2 * math.pi * frequency * x))
            for y in range(h):
                ny = y + offset
                if 0 <= ny < h:
                    pixels[x, y] = src[x, ny]

        return warped

    def generate_one(self, text=None, length=4, save=True):
        if text is None:
            text = self._random_text(length)

        captcha = Image.new("RGB", (self.width, self.height), (255, 255, 255))

        self._add_background_noise(captcha)

        char_imgs = []

        for c in text:
            font = random.choice(self.fonts)

            canvas = Image.new("RGBA", (self.font_size * 3, self.font_size * 3), (255, 255, 255, 0))
            draw = ImageDraw.Draw(canvas)

            color = (
                random.randint(0, 50),
                random.randint(0, 50),
                random.randint(0, 50),
                255
            )

            light_stroke = (
                random.randint(180, 220),
                random.randint(180, 220),
                random.randint(180, 220)
            )

            y_offset = random.randint(-3, 3)

            draw.text(
                (self.font_size, self.font_size + y_offset),
                c,
                font=font,
                fill=color,
                stroke_width=1,
                stroke_fill=light_stroke
            )

            angle = random.uniform(-15, 15)
            rotated = canvas.rotate(angle, expand=True)
            rotated = rotated.crop(rotated.getbbox())

            char_imgs.append(rotated)

        total_char_width = sum(img.width for img in char_imgs)
        available_space = self.width - total_char_width
        space = max(1, available_space // (len(text) + 1))

        x = space
        for img in char_imgs:
            y = (self.height - img.height) // 2
            captcha.paste(img, (x, y), img)
            x += img.width + space

        captcha = self._warp_image(captcha)

        if save:
            captcha.save(os.path.join(self.output_dir, f"{text}.jpg"), "JPEG")

        return captcha, text

    def generate_many(self, count, length=4):
        for _ in range(count):
            self.generate_one(length=length)

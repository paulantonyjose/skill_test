from django.db import models
from django.core.validators import FileExtensionValidator
import os
from PIL import Image

import io



class WebPConverter:
    def convert_to_webp(self, imagefield):
        with imagefield.open() as f:
            img = Image.open(f)

            buffer = io.BytesIO()

            img.save(buffer, 'webp')

        buffer.seek(0)

        return buffer


# Create your models here.
class TableThree(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(
        upload_to='images/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'png']),])
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Convert the image to WebP format before saving
        converter = WebPConverter()
        webp_buffer = converter.convert_to_webp(self.image)

        self.image.save(f'{self.image.name.split(".")[0]}.webp', webp_buffer, save=False)

        super().save(*args, **kwargs)

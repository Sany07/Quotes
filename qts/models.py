from django.db import models


class Catagory(models.Model):
    catagory=models.CharField(max_length=30)

    def __str__(self):
        return self.catagory

class Quotes(models.Model):
    author=models.CharField(max_length=50)
    quote=models.TextField()

    quote_catagory=models.ForeignKey('Catagory',
        on_delete=models.CASCADE
    )

    
    def __str__(self):
        if len(self.quote)> 50:
            return self.quote[:50]+ "..."
        else:
            return self.quote


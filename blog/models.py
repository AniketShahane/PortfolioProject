from django.db import models

class Blog(models.Model):
    #we'll have title, publication date, image, body
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to="images/", null=True)
    body = models.TextField(max_length=1000,null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]+'...'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, 20%y')

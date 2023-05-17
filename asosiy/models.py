from django.db import models

class Togri(models.Model):
    soz = models.CharField(max_length=150)
    # ntogri = models.ForeignKey(Notogri,on_delete=models.CASCADE)
    def __str__(self):
        return self.soz
class Notogri(models.Model):
    soz = models.CharField(max_length=150)
    t_soz = models.ForeignKey(Togri,on_delete=models.CASCADE)
    def __str__(self):
        return self.soz


from django.db import models

class BasicElement(models.Model):
    """
    name = (AND/OR)(2/4/8/16)[NOT]
    """
    name = models.CharField(max_length=64)
    input_numbers = models.PositiveIntegerField()
    inverse = models.BooleanField()
    its_and = models.BooleanField()
    picture = models.ImageField(upload_to='elements/')
    description = models.TextField()

    def __str__(self):
        return self.name

    def result(self, *inputs):
        """
        returns True if all inputs are True and self.its_and or at list one input True and not self.its_and.
        Also inverse result if self.inverse
        """
        return bool((int(self.inverse) + ((bool(sum(inputs))) if self.its_and else (bool(sum(inputs) == len(inputs))))) % 2)

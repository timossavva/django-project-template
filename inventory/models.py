from django.db import models
from django.utils.safestring import mark_safe


class Type(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    CHILD = 'child'
    gender = models.CharField(
        max_length=6,
        choices=[
            (MALE, 'Ανδρικό'),
            (FEMALE, 'Γύναικείο'),
            (CHILD, 'Παιδικό')
        ]
    )
    MID_SEASON = 'spring'
    SUMMER = 'summer'
    FALL = 'fall'
    WINTER = 'winter'
    season = models.CharField(
        max_length=6,
        choices=[
            (WINTER, 'Χειμωνιάτικο'),
            (SUMMER, 'Καλοκαιρινό'),
            (MID_SEASON, 'Mid-season'),
        ]
    )
    color = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(Type, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)
    quality = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)

    image_1 = models.FileField(upload_to='products/', null=True, blank=True)
    image_2 = models.FileField(upload_to='products/', null=True, blank=True)
    image_3 = models.FileField(upload_to='products/', null=True, blank=True)
    date_of_arrival = models.DateField()
    in_stock = models.BooleanField(default=True)

    def image_tag_color(self):
        if self.color:
            return mark_safe(
                '<div style="background-color:%s;height:70px;width:70px;"></div>' % self.color
            )
        else:
            return 'N/A'

    def image_tag_1(self):
        if self.image_1:
            return mark_safe(
                '<img src="%s" style="height:70px;width:70px"/>' % self.image_1.url)
        else:
            return 'N/A'

    def image_tag_2(self):
        if self.image_2:
            return mark_safe(
                '<img src="%s" style="height:70px;width:70px"/>' % self.image_2.url)
        else:
            return 'N/A'

    def image_tag_3(self):
        if self.image_3:
            return mark_safe(
                '<img src="%s" style="height:70px;width:70px"/>' % self.image_3.url)
        else:
            return 'N/A'

    image_tag_color.short_description = 'Color'
    image_tag_1.short_description = 'image 1'
    image_tag_2.short_description = 'image 2'
    image_tag_3.short_description = 'image 3'

    def __str__(self):
        return '{}'.format(self.id)

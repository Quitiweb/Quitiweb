from django.db import models


TITLE_MAX_LENGTH = 100
TXT_MAX_LENGTH = 3000
GD_MAX_LENGTH = 80


class Hobbies(models.Model):
    title = models.CharField(max_length = TITLE_MAX_LENGTH)

    class Meta:
        verbose_name_plural = 'Hobbies'

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length = TITLE_MAX_LENGTH)
    universityCollege = models.CharField(max_length = TITLE_MAX_LENGTH)
    date = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length = TITLE_MAX_LENGTH)
    role = models.CharField(max_length = TITLE_MAX_LENGTH)
    place = models.CharField(max_length = TITLE_MAX_LENGTH)
    date = models.DateTimeField()
    description = models.TextField(max_length = TXT_MAX_LENGTH)

    class Meta:
        verbose_name_plural = 'Experience'

    def __str__(self):
        return self.title

class Skills(models.Model):
    title = models.CharField(max_length = TITLE_MAX_LENGTH)
    level = models.IntegerField(default = 0)

    class Meta:
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.title

class cv(models.Model):
    title = models.CharField(max_length = TITLE_MAX_LENGTH)
    name = models.CharField(max_length = TITLE_MAX_LENGTH)
    profilePicture = models.CharField(max_length = GD_MAX_LENGTH)
    aboutMeTitle = models.CharField(max_length = TITLE_MAX_LENGTH)
    aboutMeDescription = models.TextField(max_length = TXT_MAX_LENGTH)
    skills = models.ManyToManyField(Skills)
    experience = models.ManyToManyField(Experience)
    education = models.ManyToManyField(Education)
    hobbies = models.ManyToManyField(Hobbies)
    activo = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Curriculum Vitae'

    def __str__(self):
        return self.title
from django.db import models
import datetime


YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]
MONTH_CHOICES = [(r,r) for r in range(1, 13)]

TITLE_MAX_LENGTH = 100
TXT_MAX_LENGTH = 3000
GD_MAX_LENGTH = 80


class Training(models.Model):
    course = models.CharField(max_length = TITLE_MAX_LENGTH)
    company_vendor = models.CharField(max_length = TITLE_MAX_LENGTH)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    month = models.IntegerField(('month'), choices=MONTH_CHOICES, default=datetime.datetime.now().month)

    class Meta:
        verbose_name_plural = 'Training'
        ordering = ('-year','-month',)

    def __str__(self):
        return self.course

class Education(models.Model):
    title = models.CharField(max_length = TITLE_MAX_LENGTH)
    universityCollege = models.CharField(max_length = TITLE_MAX_LENGTH)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    class Meta:
        verbose_name_plural = 'Education'
        ordering = ('-year',)

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length = TITLE_MAX_LENGTH)
    role = models.CharField(max_length = TITLE_MAX_LENGTH)
    place = models.CharField(max_length = TITLE_MAX_LENGTH)
    remote = models.BooleanField(default=False)
    fromDate = models.DateField(default=datetime.date.today)
    toDate = models.DateField(default=datetime.date.today)
    description = models.TextField(max_length = TXT_MAX_LENGTH)

    class Meta:
        verbose_name_plural = 'Experience'
        ordering = ('-toDate',)

    def __str__(self):
        return self.title + ' - ' + self.place + ' - ' + str(self.fromDate)

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
    training = models.ManyToManyField(Training)
    activo = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Curriculum Vitae'

    def __str__(self):
        return self.title
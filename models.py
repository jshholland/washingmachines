from django.db import models
from django.forms import ModelForm

STATE_CHOICES = (
    ('w', 'working'),
    ('b', 'broken'),
)

KIND_CHOICES = (
    ('d', 'dryer'),
    ('w', 'washing machine'),
)


class Machine(models.Model):
    number = models.PositiveSmallIntegerField()
    state = models.CharField(max_length=1, choices=STATE_CHOICES)
    last_updated = models.DateTimeField("last updated")
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)

    def __unicode__(self):
        if self.kind == 'd':
            return u"Dryer {}".format(self.number)
        elif self.kind == 'w':
            return u"Washing machine {}".format(self.number)


class Update(models.Model):
    state = models.CharField(max_length=1, choices=STATE_CHOICES)
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)
    machine = models.ForeignKey(Machine)


class UpdateForm(ModelForm):
    class Meta:
        model = Update
        exclude = ("machine",)
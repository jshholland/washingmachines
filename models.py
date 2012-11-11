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

    def latest_comment(self):
        u = self.update_set.order_by("-time")
        try:
            return u[0].comment
        except IndexError:
            return u""


class Update(models.Model):
    state = models.CharField(max_length=1, choices=STATE_CHOICES)
    comment = models.TextField()
    time = models.DateTimeField(auto_now=True)
    machine = models.ForeignKey(Machine)


class UpdateForm(ModelForm):
    class Meta:
        model = Update
        exclude = ("machine",)

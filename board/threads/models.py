from django.db import models
from django.utils import timezone

# Create your models here.
class Thread(models.Model):
    number_of_OnePost = models.IntegerField(default = 0)
    published_date = models.DateField()
    # first_post = models.ForeignKey(OnePost, on_delete = models.CASCADE)
    def __str__(self):
        return 'id:%d, nop:%d,  pd:%s' % (self.id, self. number_of_OnePost, self.published_date)

class OnePost(models.Model):
    text = models.CharField(max_length=2048)
    published_date = models.DateField()
    thread = models.ForeignKey(Thread, on_delete = models.CASCADE)
    number_of_replies = models.IntegerField()
    #replies = models.ManyToManyField(self)
    def __str__(self):
        return "number of post:%d published:%s text:%s thread owner: %s" % (self.id, self.published_date, self.text, self.thread)


    class Meta:
        verbose_name_plural = "Posts"
'''
class Reply(models.Model):
    number_of_relating_post = models.IntegerField()
    relating_post = models.ForeignKey(OnePost, on_delete = models.CASCADE)
    replying_post = models.ForeignKey(OnePost, on_delete = models.CASCADE)
'''

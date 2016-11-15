# from django.contrib.gis.gdal.libgdal import function

from django.db import models


# Create your models here.



class Area(models.Model):
    city = models.CharField('地区', max_length=20)

    def __str__(self):
        return self.city


class User(models.Model):
    userName = models.CharField('用户名', max_length=20)
    password = models.CharField('密码', max_length=20)
    realName = models.CharField('姓名', max_length=20)
    email = models.EmailField('邮箱')
    area = models.ForeignKey(Area, verbose_name='地区')
    face = models.ImageField('头像', upload_to='face/%Y/%m/%d/', default='', blank=True)
    url = models.CharField('个人主页', max_length=200, default='', blank=True)
    about = models.TextField('关于我', max_length=1000, default='', blank=True)
    addTime = models.DateTimeField('注册时间', auto_now=True)
    friend = models.ManyToManyField('self', verbose_name='朋友')

    def __str__(self):
        return self.realname

    def addTime_format(self):
        return self.addtime.strftime('%Y-%m-%d %H:%M-%s')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, modify_pwd=True):
        if modify_pwd:
            from utils.comm import md5_encode
            self.password = md5_encode(self.password)
        self.about = self.about[:20]
        super(User, self).save()

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户'

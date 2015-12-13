from django.db import models



# 类: DailyMemo
class DailyMemo(models.Model):
	date = models.DateField(verbose_name='日期')
	time = models.TimeField(verbose_name='时间')
	title = models.CharField(verbose_name='标题', max_length=100)
	content = models.TextField(verbose_name='内容')
	value = models.IntegerField(verbose_name='价值')



# END

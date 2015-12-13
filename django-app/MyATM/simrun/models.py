from django.db import models



# 【策略】类
class Strategy(models.Model):
	name = models.CharField(verbose_name='名称', max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = verbose_name_plural = '策略（Strategy）'



# 【商品】类
class Symbol(models.Model):
	name = models.CharField(verbose_name='名称', max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = verbose_name_plural = '商品（Symbol）'



# 【模拟运行】类
class SimRun(models.Model):
	strategy = models.ForeignKey(Strategy, verbose_name='策略')
	symbol = models.ForeignKey(Symbol, verbose_name='商品')
	period = models.CharField(verbose_name='周期', max_length=10, choices=(('m1', '一分钟'), ('d1', '一天')))
	bgnDttm = models.DateTimeField(verbose_name='开始时间')
	endDttm = models.DateTimeField(verbose_name='结束时间')
	runDttm = models.DateTimeField(verbose_name='运行时间')

	def __str__(self):
		return self.strategy.name + ':' + self.symbol.name + '.' + self.period

	class Meta:
		verbose_name = verbose_name_plural = '模拟运行（SimRun）'



# 【模拟运行TRADE】类
class SimRunTrade(models.Model):
	simRun = models.ForeignKey(SimRun, verbose_name='模拟运行')



# END

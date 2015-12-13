from django.db import models



# 【SCRIPT/脚本】类
class Script(models.Model):
	name = models.CharField(verbose_name='脚本名', max_length=100)
	title = models.CharField(verbose_name='标题', max_length=100)
	desc = models.TextField(verbose_name='描述')
	code = models.TextField(verbose_name='代码')
	run_engine = models.CharField(verbose_name='运行引擎', max_length=5, choices=(('MC', 'MultiCharts'), ('TB', 'TradeBlazer')))
	source = models.CharField(verbose_name='来源', max_length=100)  # 若取值'run_engine', 则表明是运行引擎原厂提供
	create_date = models.DateField(verbose_name='创建日期')
	modify_date = models.DateField(verbose_name='修改日期')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = verbose_name_plural = '脚本'



# END

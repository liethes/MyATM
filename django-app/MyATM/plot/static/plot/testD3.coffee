# BAR CHART例子
# TANGFENG 2015-12-08

#global_data = []
#
## 函数: 测试
#test = () ->
#	console.log global_data.length
#	global_data.pop()


#
#
#
## 函数: 主程序
#main = () ->
#	width = 960
#	height = 500
#
#	# 设置比例尺
#	y = d3.scale.linear()
#	.range [height, 0]
#
#	# 设置画布
#	chart = d3.select '.chart'
#	.attr 'width', width
#	.attr 'height', height
#
#	# 请求数据
#	d3.tsv 'data.tsv', type, (error, data) ->
#		global_data = data
#		y.domain [0, d3.max(data, (d) -> +d.value)]
#
#		barWidth = width / data.length
#
#		bar = chart.selectAll 'g'
#		.data data
#		.enter().append 'g'
#		.attr 'transform', (d, i) -> "translate(#{i * barWidth}, 0)"
#
#		d3.selectAll('g').exit().remove()
#
#		bar.append 'rect'
#		.attr 'width', barWidth - 1
#		.attr 'height', (d) -> height - y(d.value)
#		.attr 'y', (d) -> y(d.value)
#
#		bar.append 'text'
#		.attr 'x', barWidth / 2
#		.attr 'y', (d) -> y(d.value) + 3
#		.attr 'dy', '.75em'
#		.text (d) -> d.value
#
#	type = (d) ->
#		d.value = +d.value
#		d
#
#
#
## 主程序
#main()
#
#

# END

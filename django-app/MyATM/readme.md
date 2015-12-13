# 对ACE Editor的修改
* 语法定义
	添加mode文件
	添加snippet文件
	在ext-modelist里加一项

* Cursor不要blink, 并且细一点
	ace.js
		14729行: this.isBlinking = true; 改为false
		15449行: border-left: 1px solid;\ 改为1px

* Gutter的鼠标改为row-resize
	ace.js
		15322行: 改为cursor: row-resize;\

* 改theme: twilight
	- 注释不要斜体
	- active line亮一些



# 数据库
sqlite
	admin/ifwedream



# END

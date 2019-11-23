Feature: 后台-案例分享组功能基本检查

	Scenario: 案例分享检查
		When 点开用户管理
		Then 找到分享列表管理
		When 点击分享列表管理
		Then 默认展示案例分享列表页面
		When 指定标题搜索
		Then 搜索结果正确
		When 点击分享
		Then 生成分享链接
		When 分享并查看分享内容
		Then 回到分享页面
		When 回到案例分享页面并退出系统
		Then 回到登录页面




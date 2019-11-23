Feature: 后台-库内创意方功能基本检查

	Scenario: 查看库内创意方
		Given 在后台首页
		When 找到用户管理
		Then 找到发现库内创意方
		When 点击发现库内创意方
		Then 显示发现库内创意方页面
		When 关键词搜索
		Then 校验搜索结果
		When 点击任一案例查看详情
		Then 案例展示正常




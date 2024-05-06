可能有很多不完善的地方，有些功能目前还没有写完，如有修改意见请随时联系我

python 3.10
selenium webdriver（根据chrome的版本来）
可能用到的库：
selenium	4.8.2	（可调整）
pandas	2.0.2	
pypiwin32	223	
pytest	7.3.1	
uiautomator2	2.16.23	2.16.23
unittest  （根据python的版本来）


运行测试内容：

在terminal执行: python test_report.py即可开始测试（直接RUN可能会报错）
目前有的测试内容为test_case_1和test_case_2，其中的测试用例为test*函数（基本的示例）

运行前修改：

test_report.py文件中修改：生成report的位置，希望的测试名称（title变量），description


origin为打开程序导入的xml文件名称，可以自行修改
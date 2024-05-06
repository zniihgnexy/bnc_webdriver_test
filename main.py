import unittest
import HTMLTestRunner
import time
from case_selector import select_test_cases

if __name__ == '__main__':
    # Select test cases
    case_pattern_1 = 'test_case_.py'
    suits = select_test_cases(case_pattern_1)

    # 生成html格式的测试报告
    now_time = time.strftime("%Y%m%d_%H%M%S")
    fp = open('./report/' + now_time + '_result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description="运行环境：Windows 10, Chrome 浏览器")
    runner.run(suits)
    fp.close()

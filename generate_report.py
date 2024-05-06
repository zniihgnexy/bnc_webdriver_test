import unittest
import HTMLTestRunner
import time
from case_selector import select_test_cases


def generate_report(suits):
    # 生成html格式的测试报告
    now_time = time.strftime("%Y%m%d_%H%M%S")
    fp = open('./report/' + now_time + '_result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告',
                                           description="运行环境：Windows 10, Chrome 浏览器")
    runner.run(suits)
    fp.close()

if __name__ == '__main__':
    # Select test cases
    case_pattern_1 = 'test_case_1.py'
    suits1 = select_test_cases(case_pattern_1)
    generate_report(suits1)

    case_pattern_2 = 'test_case_2.py'
    suits2 = select_test_cases(case_pattern_2)
    generate_report(suits2)




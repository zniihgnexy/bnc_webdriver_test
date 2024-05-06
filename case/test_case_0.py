# coding:utf-8
import unittest
from time import sleep
from selenium import webdriver
from ui_operations import click, load_xml_file, export_xml_file, search_text, check_box_status, move_slider, copy_web_path, test_import_xml, test_checkbox_selected
from time import sleep

close_QRcode_frame = '//*[@class="ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close"]'
close_messagewindow_xpath = '//*[@class="ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close"]'
close_load_successful_dialog = '/html/body/div[6]/div[1]/button'

import_button = '//*[@id="import_json"]'
export_button = '//*[@id="export_json"]'

rl_channel_correction_feature = '/html/body/div[2]/div[2]/div/div[1]/label[1]/span[1]'
high_pass_filter_feature = '/html/body/div[2]/div[2]/div/div[1]/label[2]/span[1]'

slider_xpath = '//*[@class="ui-slider-handle ui-corner-all ui-state-default"]'

class Test_init(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.binary_location = 'C:/Users/xxzhen/AppData/Local/Programs/bncTuningTool/bncTuningTool.exe'
        self.driver = webdriver.Chrome('C:/Users/xxzhen/python3.10/Scripts/chromedriver.exe',
                              options=options)

    def tearDown(self):
        self.driver.quit()

    def test_initprogramme_1(self):

        # 连接mobil的二维码界面关闭
        click(self.driver, close_QRcode_frame)

        # load xml
        click(self.driver, import_button)
        load_xml_file(self.driver, 'C:\\Users\\xxzhen\\PycharmProjects\\electron\\export.xml')
        click(self.driver, close_load_successful_dialog)

        # 1-pass
        # preprocess button
        click(self.driver, rl_channel_correction_feature)
        # test_checkbox_selected(rl_channel_correction_feature)

        click(self.driver, high_pass_filter_feature)
        # test_checkbox_selected(high_pass_filter_feature)

        sleep(5)




if __name__ == '__main__':
    unittest.main()
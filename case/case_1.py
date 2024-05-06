# coding:utf-8
from connection_webdriver_phone import connect_webdriver, connect_phone
import unittest
from time import sleep
from selenium import webdriver
from ui_operations import click, load_xml_file, export_xml_file, search_text, check_box_status, move_slider, copy_web_path, test_import_xml, test_checkbox_selected
from time import sleep
import uiautomator2 as u2
from selenium.webdriver.common.by import By
import win32gui
import win32con
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui

close_QRcode_frame = '//*[@class="ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close"]'
import_button = '//*[@id="import_json"]'
message_dialog_xpath = '/html/body/div[6]/div[2]/p/sapn'
export_button = '/html/body/div[1]/button[2]'
close_message_dialog = '/html/body/div[6]/div[1]/button'
rl_channel_correction_feature = '/html/body/div[2]/div[2]/div/div[1]/label[1]/span[1]'
high_pass_filter_feature = '/html/body/div[2]/div[2]/div/div[1]/label[2]/span[1]'
slider_xpath = '//*[@class="ui-slider-handle ui-corner-all ui-state-default"]'

class Test_init(unittest.TestCase):
    #def setUp(self):
        #copy_web_path()

    def test_initprogramme_1(self):
        # 连接WebDriver
        dr = connect_webdriver()

        # 连接手机
        #connect_phone()

        # 连接mobil的二维码界面关闭
        click(dr, close_QRcode_frame)

        # load xml
        click(dr, import_button)
        load_xml_file(dr, 'C:\\Users\\xxzhen\\PycharmProjects\\electron\\export.xml')
        test_import_xml(message_dialog_xpath)
        click(dr, close_message_dialog)

        # 1-pass
        # preprocess button
        click(dr, rl_channel_correction_feature)
        # test_checkbox_selected(rl_channel_correction_feature)

        click(dr, high_pass_filter_feature)
        # test_checkbox_selected(high_pass_filter_feature)

        # 定义滑块的 XPath
        #move_slider(dr, slider_xpath, 0.5)

        # export
        # click(dr, export_button)
        # export_xml_file(dr, 'result-2')
        sleep(5)

        dr.quit()


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
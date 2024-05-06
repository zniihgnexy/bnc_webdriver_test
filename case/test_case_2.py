# coding:utf-8
import unittest
from time import sleep
from selenium import webdriver
from connection import connect_phone, dr
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

class Test_button(unittest.TestCase):
    #def setUp(self):
        #copy_web_path()

    def test_one_pass_button(self):
        #connect_webdriver()

        # 1-pass
        # preprocess button
        click(dr, rl_channel_correction_feature)
        # test_checkbox_selected(rl_channel_correction_feature)

        click(dr, high_pass_filter_feature)
        # test_checkbox_selected(high_pass_filter_feature)

        dr.quit()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
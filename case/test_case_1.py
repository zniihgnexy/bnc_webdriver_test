# coding:utf-8
import sys
import unittest
from time import sleep
from selenium import webdriver
from connection import connect_phone, dr
from ui_operations import click, is_popup_displayed,test_checkbox_not_selected, window_is_close, load_xml_file, export_xml_file, search_text, check_box_status, move_slider, copy_web_path, test_import_xml, test_checkbox_selected
from time import sleep
import uiautomator2 as u2
from selenium.webdriver.common.by import By
import win32gui
import win32con
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui

sys.setrecursionlimit(3000)

QRcode_frame = '//*[@class="ui-dialog ui-corner-all ui-widget ui-widget-content ui-front ui-draggable ui-resizable"]'
close_QRcode_frame = '//*[@class="ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close"]'
close_messagewindow_xpath = '//*[@class="ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close"]'
close_load_successful_dialog = '/html/body/div[6]/div[1]/button'

import_button = '//*[@id="import_json"]'
export_button = '//*[@id="export_json"]'

rl_channel_correction_feature = '//*[@id="ui-id-13"]/label[1]'
high_pass_filter_feature = '//*[@id="ui-id-13"]/label[2]'
feature_class_name = 'ui-checkboxradio-label ui-corner-all ui-button ui-widget ui-checkboxradio-checked ui-state-active'

slider_xpath = '//*[@class="ui-slider-handle ui-corner-all ui-state-default"]'


class Test_init(unittest.TestCase):

    def test_initprogramme_1(self):

        click(dr, close_QRcode_frame)
        window_is_close(dr, QRcode_frame)

        # load xml
        click(dr, import_button)
        #load_xml_file(dr, 'C:\\Users\\xxzhen\\Desktop\\bnc\\origin.xml')
        load_xml_file()
        sleep(2)
        click(dr, close_load_successful_dialog)

        #test_checkbox_selected(dr, rl_channel_correction_feature)

        click(dr, rl_channel_correction_feature)
        #test_checkbox_not_selected(dr, rl_channel_correction_feature)

        click(dr, rl_channel_correction_feature)
        #test_checkbox_not_selected(dr, high_pass_filter_feature)

        export_xml_file()

        sleep(5)

    def tearDown(self):
        dr.quit()

if __name__ == '__main__':
    unittest.main()
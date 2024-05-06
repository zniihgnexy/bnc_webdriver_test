# coding:utf-8
import unittest
from time import sleep
from selenium import webdriver
from connection import connect_phone, dr
from ui_operations import click, load_xml_file, export_xml_file, search_text, check_box_status, move_slider, copy_web_path, test_import_xml, test_checkbox_selected, page_down
from time import sleep
import uiautomator2 as u2
from selenium.webdriver.common.by import By
import win32gui
import win32con
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui


class Test_page_move(unittest.TestCase):
    #def setUp(self):
        #copy_web_path()
    path = copy_web_path()
    print(path)

    def test_page_down(self):
        page_down()

        #dr.quit()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
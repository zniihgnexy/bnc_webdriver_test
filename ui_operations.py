from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import win32gui
import win32con
from selenium.webdriver.common.action_chains import ActionChains
from connection import dr
import pyperclip
import uiautomator2 as u2
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import pyautogui
from datetime import datetime
import time
import os

def configure_logger():
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    logger = logging.getLogger("test_case_logger")
    logger.setLevel(logging.INFO)

    log_folder = "log"
    os.makedirs(log_folder, exist_ok=True)  # 创建 log 文件夹，如果不存在的话
    log_file_name = os.path.join(log_folder, f"{current_time}_logger.log")
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def click(driver, xpath):
    logger = configure_logger()
    logger.info(f"Clicking element with XPath: {xpath}")
    try:
        close_button = driver.find_element(By.XPATH, xpath)
        close_button.click()
        logger.info("Click action successful")

    except Exception as e:
        logger.error(f"Click action failed: {str(e)}")


def load_xml_file():
    logger = configure_logger()
    logger.info("Loading XML file")
    try:
        while True:
            if pyautogui.getWindowsWithTitle("open"):
                break

        window = pyautogui.getWindowsWithTitle("open")[0]
        window.activate()

        pyautogui.typewrite("origin")
        time.sleep(0.5)
        pyautogui.press("enter", presses=2, interval=0.1)

    except Exception as e:
        logger.error(f"Failed to load XML file: {str(e)}")


def export_xml_file():
    logger = configure_logger()
    logger.info("Exporting XML file")
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    while True:
        if pyautogui.getWindowsWithTitle("open"):
            break

    window = pyautogui.getWindowsWithTitle("open")[0]
    window.activate()

    file_name = f"{current_time}_result.xml"
    pyautogui.typewrite(file_name)
    time.sleep(0.5)
    pyautogui.press("enter", presses=2, interval=0.1)


def search_text(dr, xpath):
    element = dr.find_element(By.XPATH, xpath)
    text = element.text
    return text


def check_box_status(dr, xpath):#checkbox的控制
    checkbox_before_click = check_box_status(dr, xpath)
    click(dr, xpath)
    checkbox_after_click = check_box_status(dr, xpath)
    # 判断是否成功点击了按钮
    assert checkbox_before_click != checkbox_after_click, f"未成功点击复选框 {xpath}"


def move_slider(driver, slider_xpath_1, target_percent):
    x_position = 1650 * (1 - target_percent)

    # 标签定位滑块id
    span = driver.find_element(By.XPATH, slider_xpath_1)

    # 定位起始元素
    source = driver.find_element(By.XPATH, slider_xpath_1)
    # 让鼠标移动到起点元素上
    pyautogui.moveTo(span.location['x'], span.location['y'] + 50, duration=1)
    # 定位要拖拽到的位置元素
    target = driver.find_element(By.XPATH, slider_xpath_1)

    pyautogui.dragTo(span.location['x'] - x_position, span.location['y'] + 50, duration=1)
    sleep(1)

def copy_web_path():
    click(dr, '//*[@id="cp"]')
    mobile_path = get_mobile_path_from_clipboard()
    print(mobile_path)
    d = u2.connect()
    d(text="Chrome").click()
    d(resourceId="com.android.chrome:id/search_box_text").click()
    d(resourceId="com.android.chrome:id/url_bar").click()
    d.send_keys(mobile_path, clear=True)
    d.press("enter")

def get_mobile_path_from_clipboard():
    mobile_path = pyperclip.paste()
    return mobile_path

def test_import_xml(output_box_xpath):

    output_text = search_text(dr, output_box_xpath)
    expected_output = "Import XML Successfully!!!"
    assert output_text == expected_output, f"Output text mismatch. Expected: {expected_output}, Actual: {output_text}"

def test_checkbox_selected(driver, checkbox_xpath):
    button = driver.find_element(By.XPATH, checkbox_xpath)
    is_selected = button.is_selected()

    if is_selected:
        print(f"Button with XPath {checkbox_xpath} is selected")
    else:
        print(f"Button with XPath {checkbox_xpath} is not selected")


def test_checkbox_not_selected(driver, checkbox_xpath):
    checkbox_status = check_box_status(dr, checkbox_xpath)
    assert not checkbox_status, f"复选框 {checkbox_xpath} 未选中"

def check_click(before_click_status, after_click_status, error_message):
    # 判断点击前后的状态是否有变化
    if before_click_status != after_click_status:
        print("点击事件执行成功")
    else:
        raise AssertionError(error_message)

def is_popup_displayed(driver, popup_xpath):
    popup_element = driver.find_element(By.XPATH, popup_xpath)
    return popup_element.is_displayed()

def window_is_close(dr, xpath):
    is_displayed = is_popup_displayed(dr, xpath)
    if not is_displayed:
        print("Window closed successfully")
    else:
        raise AssertionError(f"Popup with XPath {xpath} is still displayed")

def check_window(driver, popup_xpath):
    # 判断弹窗是否存在
    popup_element = driver.find_element(By.XPATH, popup_xpath)
    assert popup_element.is_displayed(), f"弹窗 {popup_xpath} 未显示"

    # 等待弹窗消失
    wait.until(EC.invisibility_of_element_located((By.XPATH, popup_xpath)))

    # 判断弹窗是否成功关闭
    assert not popup_element.is_displayed(), f"弹窗 {popup_xpath} 未成功关闭"

def page_down():

    pyautogui.moveTo(1907, 317, duration=1)
    pyautogui.dragTo(1907, 1000, duration=2)
    sleep(1)

def page_up():

    pyautogui.moveTo(1907, 1000, duration=1)
    pyautogui.dragTo(1907, 317, duration=2)
    sleep(1)
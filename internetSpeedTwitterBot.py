import time
import os
from os.path import join, dirname
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

chrome_driver_path = os.environ.get('CHROME_DRIVER_PATH')
USER_NAME = os.environ.get('USER_NAME')
USER_PASSWORD = os.environ.get('USER_PASSWORD')
USER_EMAIL = os.environ.get('USER_EMAIL')
PROMISED_DOWN = os.environ.get('PROMISED_DOWN')
PROMISED_UP = os.environ.get('PROMISED_UP')

service = Service(chrome_driver_path)


class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.promised_down = int(PROMISED_DOWN)
        self.down = 0
        self.promised_up = int(PROMISED_UP)
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(60)
        down_speed = float(self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        up_speed = float(self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        self.down = down_speed
        self.up = up_speed
        print(f'Up: {self.up} / {self.promised_up}')
        print(f'Down: {self.down} / {self.promised_down}')

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(2)
        field = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        field.click()
        field.send_keys(f'{USER_NAME}')
        time.sleep(1)
        field.send_keys(Keys.ENTER)

        # time.sleep(2)
        # field = self.driver.find_element(
        #     By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        # field.send_keys(USER_EMAIL)
        # time.sleep(2)
        # field.send_keys(Keys.ENTER)

        time.sleep(2)
        pass_field = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_field.send_keys(USER_PASSWORD)
        time.sleep(2)
        pass_field.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        time.sleep(2)
        message_field = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        time.sleep(1)
        message_field.send_keys(
            f'Hey #Spectrum, why is my internet speed {self.down} down / {self.up} up when I pay for {self.promised_down} down / {self.promised_up} up?')
        self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click()

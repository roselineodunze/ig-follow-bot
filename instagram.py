from selenium import webdriver
from selenium.webdriver.common.by import By
import time

email = "roselinedemoacct@gmail.com"
password = "Roseline@04"
class InstagramBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login_ig(self):
        self.driver.get("https://www.instagram.com/accounts/login/?hl=en")
        time.sleep(4)
        username = self.driver.find_elements(By.TAG_NAME, "input")
        username[0].send_keys(email)
        username[1].send_keys(password)
        time.sleep(2)
        login = self.driver.find_elements(By.TAG_NAME, "button")[1]
        login.click()

    def followers(self):
        time.sleep(10)
        self.driver.get("https://www.instagram.com/whytmanga/followers/")
        time.sleep(10)
        follower = self.driver.find_elements(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        time.sleep(5)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower)
            time.sleep(2)
        follow_button = self.driver.find_elements(By.CSS_SELECTOR,"._aano button")
        for button in follow_button:
            button.click()
        time.sleep(2)

    def check_new_following(self):
        self.driver.get("https://www.instagram.com/roselineaprogrammer/")
        time.sleep(2)
        following = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_HU"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/ul/li[3]/a/span/span/span')
        return f"You have followed {following} new people."


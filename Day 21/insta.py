import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from conf import INSTA_USERNAME
import time
import os
import requests
from urllib.parse import urlparse

my_password = getpass.getpass('What is your password?')
browser = webdriver.Chrome()
url = 'https://www.instagram.com'
browser.get(url)

# login to instagram
time.sleep(2)
username_el = browser.find_element(By.NAME, 'username')
username_el.send_keys(INSTA_USERNAME)

password_el = browser.find_element(By.NAME,'password')
password_el.send_keys(my_password)

time.sleep(1.5)
submit_btn_el = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_btn_el.click()

body_el = browser.find_element(By.CSS_SELECTOR, 'body')
html_text = body_el.get_attribute('innerHTML')

# follow someone
def click_to_follow(browser):
    my_follow_btn_xpath = "//*[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    follow_btn_elements = browser.find_elements(By.XPATH, my_follow_btn_xpath)
    for btn in follow_btn_elements:
        time.sleep(2) # self throttle
        try:
            btn.click()
        except:
            pass

time.sleep(2)
the_user_url = 'https://www.instagram.com/lovekamaria/'
browser.get(the_user_url)
click_to_follow(browser)

time.sleep(2)
new_user_url = 'https://www.instagram.com/allsmilesonme/'
browser.get(new_user_url)

# get posts from an instagram page
post_url_pattern = 'https://www.instagram.com/p/<post-slug-id>'
post_xpath_str = "//a[contains(@href, '/p')]"
post_links = browser.find_elements(By.XPATH, post_xpath_str)
post_link_el = None

if len(post_links) > 0:
    post_link_el = post_links[0]

if post_link_el != None:
    post_href = post_link_el.get_attribute("href")
    browser.get(post_href)

video_els = browser.find_elements(By.XPATH, "//video")
image_els = browser.find_elements(By.XPATH, "//img")
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

def scrape_and_save(elements):
    for el in elements:
        url = el.get_attribute('src')
        base_url = urlparse(url).path
        filename = os.path.basename(base_url)
        filepath = os.path.join(data_dir, filename)
        if os.path.exists(filepath):
            continue
        with requests.get(url, stream=True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

scrape_and_save(image_els)
# scrape_and_save(video_els)

"""
<textarea aria-label="Add a comment…" placeholder="Add a comment…" class="Ypffh" autocomplete="off" autocorrect="off" style="height: 18px;"></textarea>
"""
def automate_comment(browser, content="Yessss, love this!"):
    time.sleep(3)
    comment_xpath_str = "//textarea[contains(@placeholder, 'Add a comment')]"
    comment_el = browser.find_element(By.XPATH, comment_xpath_str)
    comment_el.send_keys(content)
    submit_btns_xpath = "//button[type='submit']"
    submit_btns_els = browser.find_elements(By.CSS_SELECTOR, submit_btns_xpath)
    time.sleep(2)
    for btn in submit_btns_els:
        try:
            btn.click()
        except:
            pass

def automate_likes(browser):
    like_heart_svg_xpath = "//*[contains(@aria-label, 'Like')]"
    all_like_hearts_elements = browser.find_elements(By.XPATH, like_heart_svg_xpath)
    max_heart_h = -1
    for heart_el in all_like_hearts_elements:
        h = heart_el.get_attribute("height")
        current_h = int(h)
        if current_h > max_heart_h:
            max_heart_h = current_h
    all_like_hearts_elements = browser.find_elements(By.XPATH,like_heart_svg_xpath)
    for heart_el in all_like_hearts_elements:
        h = heart_el.get_attribute("height")
        if h == max_heart_h or h == f"{max_heart_h}":
            parent_button = heart_el.find_element(By.XPATH, '..')
            time.sleep(2)
            try:
                parent_button.click()
            except:
                pass


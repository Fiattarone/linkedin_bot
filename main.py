from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

EMAIL: str
PHONE_NUMBER: str
PASSWORD: str

# In progress and needs perfection.
# SUCCESS: One click applications
# WIP: Multi page applications

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, service=Service(executable_path="C:/Development/chromedriver.exe"))
driver.get("https://www.linkedin.com/")

login_field = driver.find_element(by=By.NAME, value="session_key")
login_field.send_keys(EMAIL)
password_field = driver.find_element(by=By.NAME, value="session_password")
password_field.send_keys(PASSWORD)

driver.find_element(by=By.CLASS_NAME, value="sign-in-form__submit-button").click()
time.sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a').click()
time.sleep(3)
search = driver.find_element(by=By.CLASS_NAME, value="jobs-search-box__text-input")

search.send_keys("Python Developer")
search.send_keys(Keys.ENTER)

time.sleep(3)
filters = driver.find_elements(by=By.CLASS_NAME, value="artdeco-pill")
# print([button.text for button in filters])
filters[1].click()
date_dropdown = driver.find_elements(by=By.CLASS_NAME, value="search-reusables__value-label")
# print([button.text for button in date_dropdown])
date_dropdown[3].click()
results = driver.find_element(by=By.CLASS_NAME, value="ml2")
results.click()

time.sleep(1)
filters = driver.find_elements(by=By.CLASS_NAME, value="artdeco-pill")
filters[2].click()

# entry_level = driver.find_element(by=By.CSS_SELECTOR, value="label[for='experience-2']")
# entry_level.click()
#
# associate = driver.find_element(by=By.CSS_SELECTOR, value="label[for='experience-3']")
# associate.click()
#
# # action = webdriver.ActionChains(driver)
# new_results = driver.find_element(by=By.CSS_SELECTOR, value="[type='button']")
# time.sleep(1)
# print([item.text for item in new_results])
# new_result.click()
# # action.move_to_element(new_results).click().perform()

filters = driver.find_elements(by=By.CLASS_NAME, value="artdeco-pill")
filters[6].click()

time.sleep(1)
# job_listings =

for i in range(len(driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item"))):
    try:
        driver.find_elements(by=By.CLASS_NAME, value="jobs-search-results__list-item")[i].click()
        time.sleep(1)
        driver.find_element(by=By.CLASS_NAME, value="jobs-apply-button--top-card").click()
        phone = driver.find_element(by=By.CLASS_NAME, value="fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE_NUMBER)
        submit = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        submit.click()

        try:
            if driver.find_element(
                by=By.CLASS_NAME,
                value="t-16 t-bold"
            ).text == "Home address":
                city = driver.find_element(by=By.CSS_SELECTOR, value="div input[class='artdeco-typeahead__input ']")

            time.sleep(1)
            submit = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
            submit.click()
            try:
                time.sleep(1)
                if driver.find_element(
                        by=By.CSS_SELECTOR,
                        value="label span[class='t-14']"
                ).text == "Do you work with a third party employer (C2C)?":
                    print("Text matched for C2C Employer.")
                    driver.find_element(by=By.CSS_SELECTOR, value="div select option[value='No']").click()
                    submit = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
                    submit.click()
                    try:
                        time.sleep(1)
                        submit = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
                        submit.click()
                    except NoSuchElementException:
                        print("Not the end of application.")
                        continue
                else:
                    print("No text matched for 3rd page.")
            except NoSuchElementException:
                print("Didn't have C2C Employer text.")
                continue
        except NoSuchElementException:
            print("Didn't have 2nd Next.")
            continue

        time.sleep(1)
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()
        time.sleep(1)
    except NoSuchElementException:
        print("No App button, skipping.")
        continue





# for job in job_listings:
#     print(f"Saved: {job.text}")
#     driver.execute_script("arguments[0].click();" , job)
#     time.sleep(3)
time.sleep(600)

driver.close()

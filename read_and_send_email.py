import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from popupmsg import root

SUBJECTS = ["lucallonso@gmail.com"]
# def send_mail():
driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
email = 'lucallonso@gmail.com'
def find_and_send(name, text):
    elem = driver.find_element_by_name(name)
    elem.clear()
    return elem.send_keys(text)

def send_button(name):
    driver.implicitly_wait(10)
    button = driver.find_element_by_class_name(name)
    return button.click()

driver.get("https://mail.ktga.kz")
elem1 = find_and_send('username', 'k.amanova@ktga.kz')
elem2 = find_and_send('password', 'K.,k.;bpym999')
enter = send_button('signinTxt')

""" IN EMAIL"""
find_button = driver.find_element_by_xpath(
    '//*[@title="BotagozZTU@halykbank.kz"]').click()
# find_dates = driver.find_elements_by_class_name('listItemDefaultBackground')
find_dates = driver.find_elements_by_xpath(
            '//div[contains(@class, "_lvv_w") or contains(@class, "listItemDefaultBackground")]'
)
subjects = "Нургалиев Айдос Давлетович", "Осербаев Даулет Сеитказиевич"
today = datetime.datetime.today().strftime("%d.%m.%Y")
for date in find_dates:
    date.click()
    driver.implicitly_wait(5)
    # Ищет есть ли пересланное сообщение
    is_stash = driver.find_elements_by_xpath(
        '//div[@class="_rp_g4"]'
    )
    # Заголовок письма
    header_text = driver.find_element_by_xpath(
        "//div[contains(@class, 'allowTextSelection') and contains(@aria-label, 'Панель чтения')]//div[@class='_rp_l']//span[@role='heading']"
    ).text
    if is_stash and "Реестр принятых платежей" not in header_text:
        continue

    # Ищет дату и сверяет с текущей
    fd = driver.find_elements_by_xpath(
        '//span[contains(@title, "%s")]' % today
    )
    # Сохраняет в папку айди письма. Сделано для успешного получения и отправки больше 1 письма
    for i in fd:
        with open('using_ids.txt', 'r+') as file:
            text = file.read()
            if str(i.id) in text:
                continue
            else:
                file.write('\n' + str(i.id) + '\n')

        btn = driver.find_element_by_xpath(
            '//button[contains(@title, "Дополнительные действия") and contains(@type, "button") and contains(@aria-label, "Другие действия")]'
        ).click()
        btn1 = driver.find_element_by_xpath(
            '//*[contains(@aria-label, "Контекстное меню") and contains(@class, "_fce_y")]'
        )
        btn1.find_element_by_xpath("//div[@role='menuitem']//button//div//span[text()='Переслать']").click()

        send_email_button = driver.find_element_by_xpath(
            '//input[contains(@aria-label, "Кому")]'
        )
        for subject in SUBJECTS:
            send_email_button.send_keys(subject)
            time.sleep(0.1)
            send_email_button.send_keys(Keys.RETURN)

        btn_send = driver.find_elements_by_xpath(
            '//div[contains(@class, "_mcp_H2")]//button[contains(@class, "_mcp_62 o365button o365buttonOutlined ms-font-m ms-fwt-sb ms-fcl-w ms-bgc-tp ms-bcl-tp ms-bgc-td-f ms-bcl-tdr-f") and contains(@title, "Отправить") and contains(@type, "button") and contains(@aria-label, "Отправить")]'
        )[1].click()



# import schedule
# import time
#
# def job():
#     print("I'm working...")
#
# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

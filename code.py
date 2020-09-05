from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random


def goToChat(driver, name):
    count = int(input('Enter the number of times to send message: '))
    input('Press a key after scanning QR code')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    return count


def sendMessage(driver, name):
    msg = input('Enter your message: ')
    count = goToChat(driver, name)

    msg_box = driver.find_element_by_xpath(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "_3uMse", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "selectable-text", " " ))]')
    for _ in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_1U1xa')
        button.click()


def sendSticker(driver, name):
    count = goToChat(driver, name)
    input("Go to the sticker tab")
    # gotosticker

    sticker = driver.find_elements_by_class_name("_2EemV")
    total = len(sticker)
    for _ in range(count):
        n = random.randint(0, total-1)
        sticker[n].click()


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://web.whatsapp.com/')

    name = input('Enter the name of user or group : ')
    print("1. To send message")
    print("2. To send random sticker")
    type = int(input("Enter the type:"))

    if type == 1:
        sendMessage(driver, name)
    if type == 2:
        sendSticker(driver, name)


if __name__ == "__main__":
    main()

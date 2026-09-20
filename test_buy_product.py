from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_buy_product(browser, url):
    wait = WebDriverWait(browser, 10)

    browser.get(url)

    wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")

    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "inventory_list")))

    add_to_cart = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_to_cart.click()

    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "shopping_cart_badge"), "1"))

    cart_link = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_link.click()

    wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "cart_list")))

    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_button.click()

    wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

    browser.find_element(By.ID, "first-name").send_keys("Ivan")
    browser.find_element(By.ID, "last-name").send_keys("Ivanov")
    browser.find_element(By.ID, "postal-code").send_keys("123456")

    continue_button = wait.until(
        EC.element_to_be_clickable((By.ID, "continue")))
    continue_button.click()

    wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "summary_total_label")))

    finish_button = wait.until(
        EC.element_to_be_clickable((By.ID, "finish")))
    finish_button.click()

    complete_header = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text

    assert complete_header == "Thank you for your order!", \
        f"Ожидался 'Thank you for your order!', получено: '{complete_header}'"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


# creacion de la userinterfaces donde se mapea los elementos y de le damos de paso una accion a realizar
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.nombreCompleto_input_xpath = "//input[@id= 'full-name']"
        self.email_input_xpath = "//input[@id= 'email']"
        self.password_input_xpath = "//input[@id= 'password']"
        self.confirm_password_input_xpath = "//input[@id= 'confirm-password']"
        self.login_button_xpath = "//*[contains(@class, 'btn') and contains(@class, 'btn-primary') and (@type = 'submit')]"
        self.message_no_mach_xpath = "//*[contains(text(), 'Passwords do not match')]"
        self.message_successful_xpath = "//*[contains(text(), 'Successful registration!')]"
        self.message_user_not_xpath = "//*[contains(text(), 'User not found')]"
        self.name_user_xpath = "//h2[text() = 'Carlos Amaya']"
        self.avatar_xpath = "//*[contains(@class, 'btn btn-ghost btn-circle avatar')]"
        self.logout_xpath = "//li[a[text() = 'Logout']]"
        self.close_alert = "//div[@role='alert' and .//div[contains(text(), 'Successful registration!')]]//button[@aria-label='Close']"
        self.close_alert_error = "//div[@role='alert' and .//div[contains(text(), 'User not found')]]//button[@aria-label='Close']"



    def enter_nombreCompleto(self, nombreCompleto):
        nombreCompleto_input_xpath = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.nombreCompleto_input_xpath))
        )
        nombreCompleto_input_xpath.clear()
        nombreCompleto_input_xpath.send_keys(nombreCompleto)


    def enter_email(self, email):
        email_input_xpath = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.email_input_xpath))
        )
        email_input_xpath.clear()
        email_input_xpath.send_keys(email)

    def enter_password(self, password):
        password_input_xpath = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.password_input_xpath))
        )
        password_input_xpath.clear()
        password_input_xpath.send_keys(password)

    def confirm_password(self, confPassword):
        confirm_password_input_xpath = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.confirm_password_input_xpath))
        )
        confirm_password_input_xpath.clear()
        confirm_password_input_xpath.send_keys(confPassword)

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button_xpath))
        )
        login_button.click()

    def verify_password_no_match_message(self):
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.message_no_mach_xpath))
        )
        return error_message.is_displayed()

    def verify_successful_message(self):
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.message_successful_xpath))
        )
        return error_message.is_displayed()

    def verify_user_not_message(self):
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.message_user_not_xpath))
        )
        return error_message.is_displayed()

    def verify_user_name(self, expected_name):
        user_name_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.name_user_xpath))
        )
        actual_name = user_name_element.text
        return actual_name == expected_name
    def click_avatar_perfil(self):
        avatar_perfil = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.avatar_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", avatar_perfil)
        avatar_perfil = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.avatar_xpath))
        )
        avatar_perfil.click()

    def click_logout_perfil(self):
        salir_perfil = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.logout_xpath))
        )

        salir_perfil.click()

    def click_close_alert(self):
        close_alert_pass = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.close_alert))
        )
        close_alert_pass.click()

    def click_close_alert_error(self):
        close_button_error = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.close_alert_error))
        )
        close_button_error.click()

def login(self, nombreCompleto, email, password, confPassword):
    self.enter_nombreCompleto(nombreCompleto)
    self.enter_email(email)
    self.enter_password(password)
    self.confirm_password(confPassword)
    self.click_login_button()
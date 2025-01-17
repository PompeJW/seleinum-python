import logging
import os
import time
import unittest

import self
import xmlrunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from drivers.ChromeDrivers import ChromeDriver
from pages.login_page import LoginPage
from utils.Constantes import URL_REGISTRO, REGISTRO_FULL_NAME, EMAIL_USUARIO, CONTRASEÑA, NOMBRE_INCOMPLETO, CONTRASEÑA_ERRONEA, CONTRASEÑA_DIFERENTE, EMAIL_ERRONEO

class TestLogin(unittest.TestCase):
    #seteamos el driver de chrome con una libreria para no tener que andar sufriendo con la version de chrome
    def setUp(self):
        self.driver = ChromeDriver.get_driver()
        self.login_page = LoginPage(self.driver)
    # al finalizar quitamos el driver
    def tearDown(self):
        self.driver.quit()
    #aca creamos el scenario para la prueba, podemos crear varios escenarios que validen aspecto por aparte, pero
    # si podemos reutilizar codifgo y que todo se valide en conjunto es mejor, como lo es el caso


    def test_registro(self):
        self.login_page.open(URL_REGISTRO)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.login_page.nombreCompleto_input_xpath))
        )
        self.login_page.enter_nombreCompleto(NOMBRE_INCOMPLETO)
        self.login_page.enter_email(EMAIL_USUARIO)
        self.login_page.enter_password(CONTRASEÑA_ERRONEA)
        self.login_page.confirm_password(CONTRASEÑA_DIFERENTE)

        time.sleep(1)

        self.assertTrue(self.login_page.verify_password_no_match_message(), "El mensaje de error 'Passwords do not match' debería aparecer")
        time.sleep(1)

        submit_button = self.driver.find_element(By.XPATH, self.login_page.login_button_xpath)
        self.assertFalse(submit_button.is_enabled(), "El botón de registro debería estar deshabilitado")
        time.sleep(1)
        self.login_page.enter_nombreCompleto(REGISTRO_FULL_NAME)
        submit_button = self.driver.find_element(By.XPATH, self.login_page.login_button_xpath)
        self.assertFalse(submit_button.is_enabled(), "El botón de registro debería estar deshabilitado")
        time.sleep(1)

        self.login_page.enter_password(CONTRASEÑA)
        self.login_page.confirm_password(CONTRASEÑA)
        submit_button = self.driver.find_element(By.XPATH, self.login_page.login_button_xpath)
        self.assertTrue(submit_button.is_enabled(), "El botón de registro debería estar habilitado")
        time.sleep(1)

        self.login_page.click_login_button()

        self.assertTrue(self.login_page.verify_successful_message(),"El mensaje Succesful debe aparecer")
        self.login_page.click_close_alert()

        self.login_page.enter_email(EMAIL_ERRONEO)
        self.login_page.enter_password(CONTRASEÑA)
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.verify_user_not_message(),"El mensaje de usuario no existe debe aparecer")
        self.login_page.click_close_alert_error()
        self.login_page.enter_email(EMAIL_USUARIO)
        self.login_page.click_login_button()

        time.sleep(5)
        logging.info("Verificando que el nombre de usuario sea correcto")
        self.assertTrue(self.login_page.verify_user_name(REGISTRO_FULL_NAME), "El nombre de usuario debería ser correcto")
        self.login_page.click_avatar_perfil()
        time.sleep(3)
        self.login_page.click_logout_perfil()




        time.sleep(10)

if __name__ == "__main__":

    os.makedirs('test-reports', exist_ok=True)
    with open('test-reports/test_registro.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self , by_locator):
        WebDriverWait ( self.driver , 5 ).until ( ec.presence_of_element_located ( by_locator ) ).click ()

    def do_send_keys(self , by_locator , text):
        WebDriverWait ( self.driver , 5 ).until ( ec.visibility_of_element_located ( by_locator ) ).send_keys ( text )

    def get_element_text(self, by_locator):
        ele = WebDriverWait(self.driver, 2).until((ec.presence_of_element_located(by_locator)))
        return ele.text

    def is_visible(self , by_locator):
        element = WebDriverWait ( self.driver , 5 ).until ( ec.visibility_of_element_located ( by_locator ) )
        return bool ( element )

    def get_element(self , by_locator):
        element = WebDriverWait ( self.driver , 5 ).until ( ec.presence_of_element_located ( by_locator ) )
        return element


    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(ec.title_is(title))
        return self.driver.title


    def do_clear(self , by_locator):
        WebDriverWait ( self.driver , 5 ).until ( ec.visibility_of_element_located ( by_locator ) ).clear ()

    # def take_screenshot(self , file):
    #     WebDriverWait(self.driver, 5).until(pyscreenshot.grab( self.driver ).save( file ))
    #     return self.driver.save_screenshot(file)





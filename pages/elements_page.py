from components.components import WebElement
from pages.base_page import BasePage


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/elements"
        super().__init__(driver, self.base_url)

        self.elements_page = WebElement(driver, '#app > div > div >div.row > div.col-12.mt-4.col-md-6')
        self.elements_page_1 = WebElement(driver, 'div.playgound-header > div')

        self.icon = WebElement(driver, 'header > a > ing')
        self.btn_sidebar = WebElement(driver, 'div:ntn-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:ntn-child(1) > div > ul > #item-0 > span')

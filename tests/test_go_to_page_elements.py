from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_go_to_page_elements(browser):
    # 22
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_element.click()
    assert elements_page.equal_url()

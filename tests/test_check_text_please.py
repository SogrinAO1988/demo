from pages.elements_page import ElementsPage


def test_page_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.elements_page_1.get_text() == 'Elements'

    assert elements_page.icon.exist()
    # assert elements_page.btn_sidebar.exist()
    # assert elements_page.btn_sidebar_first_textbox.exist()

from pages.swag_labs import SwagLabs


def test_icon_exist(browser):

    demo_page = SwagLabs(browser)
    demo_page.visit()

    assert demo_page.test_exist_icon()
    assert demo_page.test_name_exist()
    assert demo_page.test_password_exist()



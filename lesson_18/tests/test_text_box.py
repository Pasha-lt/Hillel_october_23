from Hillel_october_23.lesson_18.TextBoxPage import TextBoxPage

import time
class TestTextBox:

    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Pavlo")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_fullname()
        assert name_field.replace("Name:", "") == "Pavlo"

    def test_email_fill_and_check(self, chrome):
        #todo
        pass

    def test_curr_addr_fill_and_check(self, chrome):
        #todo
        pass

    def test_perm_addr_fill_and_check(self, chrome):
        #todo
        pass
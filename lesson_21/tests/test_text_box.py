import pytest

from Hillel_october_23.lesson_20.TextBoxPage import TextBoxPage

class TestTextBox:

    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Pavlo")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_fullname()
        assert name_field.replace("Name:", "") == "Pavlo"

    @pytest.mark.parametrize("email", ["i@meta", "wrong email"])
    def test_email_fill_and_check_negative(self, chrome, email):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_email_field(email)
        page.scroll_down()
        page.click_submit()
        class_of_field = page.get_email_field_element().get_attribute("class")
        assert "error" in class_of_field



    # def test_email_fill_and_check(self, chrome):
    #     #todo HW
    #     pass
    #
    # def test_curr_addr_fill_and_check(self, chrome):
    #     # todo HW
    #     pass
    #
    # def test_perm_addr_fill_and_check(self, chrome):
    #     # todo HW
    #     pass



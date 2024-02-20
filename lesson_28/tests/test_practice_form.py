import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Hillel_october_23.lesson_27.src.pages.page_practice_form import PagePracticeForm

@pytest.mark.usefixtures("firefox")
class TestPracticeForm:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PagePracticeForm(driver=self.driver)


    # def test_(self):
    #     state = "NCR"
    #     self.page.open()
    #     self.page.set_state_via_input()
    #     self.page.set_state_from_dropdown()
    #     self.page.show_filtered_results_in_dropdown(state)
    #     results = self.page.get_result_from_dropdown()
    #     assert "NCR" in results[0]
    #     assert "NCR" in str(results)

    def test_upload_file(self):
        self.page.open()
        upload_button = self.driver.find_element(By.CSS_SELECTOR, "input#uploadPicture")
        upload_button.send_keys("/Users/pavlokostyshen/Desktop/2.png")
        file_name = upload_button.get_attribute("value")
        self.driver.save_screenshot("12.png")
        assert "2.png" in file_name
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class Component:
    def __init__(self, driver: WebDriver = None, locator: tuple=None) -> None:
        if driver:
            self.driver: WebDriver = driver
            if locator:
                self.locator = locator
                self.element: WebElement = self.driver.find_element(*self.locator)
        self._actions = ActionChains(driver=driver)

    def type_of(self) -> str:
        """визначаємо який тип віджета в нас є"""
        return self.__class__.__name__

    def scroll_to(self) -> None:
        """проскролюємо до елемента 1-й випадок. якщо він наприклад внизу сторінки,
        то скролить вверх і коли бачить елемент зупиняється"""
        self._actions.scroll_to_element(self.element)

    def scroll_into_view(self) -> None:
        """проскролюємо до елемента за допомогою джаваскріпт коду на сторінці.
        Скролить з запасом і дає нам більшу імовірність що ми достукаємось до елементу якщо він перекритий"""
        self.driver.execute_script("arguments[0].scrollIntoView();", self.element)

class Button(Component):
    def __init__(self, driver: WebDriver = None, locator: tuple = None):
        super().__init__(driver=driver, locator=locator)

    def hover(self):
        self._actions.move_to_element(self.element).perform()

    def click(self):
        self.element.click()

    def doubleclick(self):
        self._actions.double_click(self.element).perform()

    def right_click(self):
        self._actions.context_click(self.element)

    def get_attribute(self, attr):
        return self.element.get_attribute(attr)


class TextField(Component):

    def __init__(self, driver: WebDriver, locator: tuple):
        super().__init__(driver=driver, locator=locator)
        self.__actions = ActionChains(driver=driver)
        self.field: WebElement = self.driver.find_element(*self.locator)

    def clear(self) -> None:
        self.field.clear()

    def set_value(self, value: str) -> None:
        self.clear()
        self.field.send_keys(value)

    def send_keys(self, val: str) -> None:
        self.field.send_keys(val)

    def get_value(self) -> str:
        return self.field.get_attribute('value')

    def value_of_css_property(self, prop: str) -> str:
        return self.field.value_of_css_property(property_name=prop)


class TextArea(TextField):
    def __init__(self, driver: WebDriver, locator: tuple):
        super().__init__(driver, locator)


class CheckBox(Component):
    def __init__(self, driver: WebDriver, locator: tuple, name: str = None):
        super().__init__(driver, locator)
        self.locator = locator
        by, loc = locator
        self.label = self.driver.find_element(by, loc)
        self.input_loc = '//input[@type="checkbox"]'
        self.input = self.label.find_element(By.XPATH, self.input_loc)
        self.named_label = '[contains(@for, "{}")]'
        self.named_input = '[contains(@id, "{}")]'
        if name:
            loc += self.named_label.format(name)
            self.label = self.driver.find_element(by, loc)
            self.input = self.label.find_element(By.XPATH, f'{self.input_loc}{self.named_input.format(name)}')
        # replace value in double-quotes with new value: re.sub(r'"[^"]+"', f'"new_val"', loc)

    def __change_checkbox_selection_state(self, name: str) -> None:
        by, loc = self.locator
        if name:
            loc += self.named_label.format(name)
        label = self.driver.find_element(by, loc)
        label.click()

    def is_selected(self, name: str = None) -> bool:
        if name:
            input_loc = f'{self.input_loc}{self.named_input.format(name)}'
            input_ = self.label.find_element(By.XPATH, input_loc)
            return input_.is_selected()
        return self.input.is_selected()

    def select(self, name: str) -> None:
        if not self.is_selected(name):
            self.__change_checkbox_selection_state(name)

    def deselect(self, name: str) -> None:
        if self.is_selected(name):
            self.__change_checkbox_selection_state(name)

class ExpandableTreeElement(Component):

    def __init__(self, driver: WebDriver = None, locator: tuple = None, name: str = None):
        super().__init__(driver, locator)
        self.folder_loc = '//label[contains(@for, "tree-node-{folder}")]'
        if name:
            self.folder_loc = f'//label[contains(@for, "tree-node-{name}")]'
        self.folder_expand_button_loc = f'{self.folder_loc}//ancestor::span/button'
        self.expand_status_loc = '//*[contains(@class, "expand-{}")]'

    def __change_folder_expand_state(self, name: str = None, open_: bool = True) -> None:
        if name:
            folder = self.driver.find_element(By.XPATH, self.folder_expand_button_loc.format(folder=name))
        else:
            folder = self.driver.find_element(By.XPATH, self.folder_expand_button_loc)
        try:
            if open_:
                folder.find_element(By.XPATH, self.expand_status_loc.format('close')).click()
            else:
                folder.find_element(By.XPATH, self.expand_status_loc.format('open')).click()
        except NoSuchElementException:
            pass

    def expand_folder(self, name) -> None:
        self.__change_folder_expand_state(name=name, open_=True)

    def collapse_folder(self, name) -> None:
        self.__change_folder_expand_state(name=name, open_=False)

    def __change_folder_selection_state(self, name, enabled=False) -> bool:
        folder = self.driver.find_element(By.XPATH, self.folder_loc.format(folder=name))
        input_el = folder.find_element(By.XPATH, '//input')
        if enabled:
            if not input_el.is_selected():
                folder.click()
                return input_el.is_selected()
        else:
            if input_el.is_selected():
                folder.click()
                return not input_el.is_selected()

    def mark_folder(self, name) -> bool:
        state = self.__change_folder_selection_state(name, enabled=True)
        return state

    def unmark_folder(self, name) -> bool:
        state = self.__change_folder_selection_state(name, enabled=False)
        return state

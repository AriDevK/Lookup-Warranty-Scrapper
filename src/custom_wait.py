from selenium.webdriver.support.wait import WebElement

class ElementHasStyle(object):
  def __init__(self, locator: WebElement, css_styles: str):
    self.locator = locator
    self.css_styles = css_styles

  def __call__(self, driver):
    element: WebElement = driver.find_element(*self.locator)

    if element.get_attribute('style') == 'display: block; color: red;':
        raise ValueError('No data found')

    if self.css_styles == element.get_attribute('style'):
        return element
    else:
        return False

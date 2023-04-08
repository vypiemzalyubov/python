from selenium.webdriver.common.by import By

# 7.1. Найдите кпопку c текстом "Gold". Попробуйте подобрать как минимум 2 разных XPATH и/или CSS-селекторов
#      http://suninjuly.github.io/xpath_examples

# By.CSS_SELECTOR:

By.CSS_SELECTOR, "body div:nth-child(2) button:nth-child(3))"
By.CSS_SELECTOR, "body div:nth-child(2) button:nth-last-child(2)"

# By.XPATH:

By.XPATH, "//button[contains(text(), 'Gold')]"
By.XPATH, "//body//div[2]//button[last()-1]"


# 7.2. Найдите элемент с текстом "Fully charged cat". Чем больше разных XPATH и/или CSS-селекторов сможете подобрать, тем лучше
#      http://suninjuly.github.io/cats.html

# By.XPATH:

By.XPATH, "//img[@src='images/fully-charged-cat.jpg']/parent::div/div/p"
By.XPATH, "//p[contains(text(), 'Fully')]"
By.XPATH, "//p[text()='Fully charged cat']"
By.XPATH, "//div[@class='container']//div[5]"
By.XPATH, "//div[@class='container']//div[last()-1]"

# By.CSS_SELECTOR

By.CSS_SELECTOR, "div[class='col-sm-4']:nth-child(5) p"
By.CSS_SELECTOR, "div[class='row'] div[class='col-sm-4']:nth-child(5) p"
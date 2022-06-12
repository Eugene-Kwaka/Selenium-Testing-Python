# Pytest is used for Unit Testing and provides mechanism for Parameterized testing
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
# Keys enable me to perform relevant keyboard actions on WebElements in the DOM
from selenium.webdriver.common.keys import Keys
# Suspends the execution for a specified time duration. NOT CONSIDERED SELENIUM BEST PRACTICE
from time import sleep




def test_lambdatest_google():
    # creating an instance of Google Chrome Browser
    chrome_driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    # Visit the Url where I will conduct the test
    chrome_driver.get('https://www.google.com')
    # This will maximize the window interface of the driver class in this case it's Chrome
    chrome_driver.maximize_window()
    # An exception will be raised if the window title does not match to the title specified.
    if not "Google" in chrome_driver.title:
       raise Exception("Could not load page")
    # The Google search form will be fetched by its element's NAME which is "q"
    element = chrome_driver.find_element_by_name("q")
    # Send Keys is used to INPUT THE SEARCH TERM in the search box that was located using its NAME "q" with "find_element_by_name"
    element.send_keys("LambdaTest")
    # To submit in the form I will use "Submit()" method
    element.submit()
    # Check if the LambdaTest Home Page is open
    title = "Most Powerful Cross Browser Testing Tool Online | LambdaTest"
     # The POM BUILDER is used to instantly generate locators including XPath, CSS Selector for use in Selenium
    # LambdaTest Link found using the POM BUILDER in the Chrome Browser
    lt_link = chrome_driver.find_element_by_xpath("//h3[.='LambdaTest: Most Powerful Cross Browser Testing Tool Online']")
    # Since the link was shown by the POM BUILDER, I will click on it
    lt_link.click()

    sleep(5)

    assert title == chrome_driver.title

    sleep(2)
    
    # Then I will terminate the instance of Firefox browser using the "quit() method"
    chrome_driver.quit()

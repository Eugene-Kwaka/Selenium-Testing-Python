# Pytest is used for Unit Testing and provides mechanism for Parameterized testing
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
# Keys enable me to perform relevant keyboard actions on WeebElements in the DOM
from selenium.webdriver.common.keys import Keys
# Suspends the execution for a specified time duration. NOT CONSIDERED SELENIUM BEST PRACTICE
from time import sleep



def test_lambdatest_todo_app():
    # creating an instance of the Firefox Browser
    ff_driver = webdriver.Firefox(executable_path='C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe')
    # The url used is the LambdaTest TodoPage
    ff_driver.get('https://lambdatest.github.io/sample-todo-app/')
    # This will maximize the window interface of the driver class in this case it's FIREFOX
    ff_driver.maximize_window()
    # I will find an element by its NAME property in Firefox and check the checkbox
    ff_driver.find_element_by_name("li1").click()
    ff_driver.find_element_by_name("li2").click()
    # The window title is compared to the expected in the Url which is:
    title = "Sample page - lambdatest.com"
    # I will assert that the title has that name
    assert title  == ff_driver.title
    # New item added to the Todo List then the WebElement is located using the "find_element" methpd and the ID property
    sample_text = "Happy Testing at LambdaTest"
    # The Id used by the form is "sampletodotext"
    email_text_field = ff_driver.find_element_by_id("sampletodotext")
    # I will add the new Todo item(sample_text) by using send_keys() function.
    email_text_field.send_keys(sample_text)

    sleep(5)

    # To click the Add Button, I need to identify it by its id then click
    ff_driver.find_element_by_id("addbutton").click()

    sleep(5)

    # To read the text of the new todo item added, we use "getText method". 
    # In this case the new item is the 6th item in the list will be displayed
    output_str = ff_driver.find_element_by_name("li6").text
    # Write out the output string defined above
    sys.stderr.write(output_str)

    sleep(2)

    # Then I will terminate the instance of Firefox browser using the "quit() method"
    ff_driver.quit()



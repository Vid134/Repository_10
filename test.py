import pytest    ##importing the pytest framework to write test functions and fixtures
from selenium import webdriver    ##Imports main selenium webdriver class which is used to control browser
from selenium.webdriver.chrome.service import Service   ##Service is used to run chrome driver properly
from selenium.webdriver.chrome.options import Options    ##Options allows us to configure chrome
from selenium.webdriver.common.by import By      ##By is used to locate elements like id,name
from selenium.webdriver.support.ui import WebDriverWait  ##webdriver allows us to wait until elements or conditions appear
from selenium.webdriver.support import expected_conditions as EC   ##Ec provides prebuilt conditions
from selenium.webdriver.common.action_chains import ActionChains   ##action chains is used for advanced interactions
from webdriver_manager.chrome import ChromeDriverManager    ### webdriver-manager will download the matching ChromeDriver for you.


@pytest.fixture       ## PyTest fixture to create and tear down the WebDriver for each test.
def driver():


    options = Options()  ##Creates a chrome options object i.e allows configuring chrome browser
    options.add_argument("--start-maximized")   ##starts chrome in fullscreen mode for better interaction


    service = Service(ChromeDriverManager().install())   #Create Service object using webdriver-manager to auto-download driver


    driver = webdriver.Chrome(service=service, options=options)   #  Start Chrome browser


    driver.get("https://jqueryui.com/droppable/")  #  Navigate to the droppable demo page

    # Wait for the iframe to be present and switch into it.
    #    The droppable demo is placed inside an iframe on this page.
    wait = WebDriverWait(driver, 10)
    # iframe has class "demo-frame" on this site; using CSS selector is stable.
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.demo-frame")))


    yield driver   # Yield the driver to the test. After the test finishes, code after yield runs.


    driver.quit()   ##quit the browser


def test_drag_and_drop_positive(driver):
    """
    Positive test case:
    Drag the white box into the yellow box and verify the text changes to "Dropped!".
    """
    # Find draggable and droppable elements by id inside the iframe
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    # Performing the drag and drop using ActionChains
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()

    # Wait until the droppable text contains "Dropped"
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, "droppable"), "Dropped"))

    # Assert the drop happened (text changes to "Dropped!" in the demo)
    assert "Dropped" in target.text


def test_drag_and_drop_negative_wrong_location(driver):
    """
    Negative test case:
    Drag the white box to a nearby offset (not on the yellow box) and verify it did not drop.

    """
    # Find draggable and droppable elements by id inside the iframe
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    # Intentionally drag by an offset that does NOT land on the target.
    # You can adjust offset values if required by screen resolution.
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(source, -300, 0).perform()
    ##i gave this value cause i know this will not land on target ensuring drop fails

    # Small wait to let any UI updates happen
    WebDriverWait(driver, 2)

    ## Assert original text remains (negative case)
    # The droppable's default text on this demo is "Drop here"
    assert "Drop here" in target.text or "Drop here" in target.get_attribute("innerText")


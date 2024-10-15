# test_selenium.py
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_search():
    # Initialize the WebDriver (e.g., using Chrome)
    driver = webdriver.Chrome()

    try:
        # Open Google homepage
        driver.get("https://www.google.com")

        # Assert that the title contains 'Google'
        assert "Google" in driver.title

        print("Test Passed: Google page opened successfully and title is correct.")

    except Exception as e:
        print(f"Test Failed: {e}")
    
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_google_search()

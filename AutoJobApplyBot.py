import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# LinkedIn Configuration
linkedin_url = driver.get("https://www.linkedin.com/")
def apply_on_linkedin(job_title):
    try:
        driver.get(linkedin_url)
        for cookie in linkedin_cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        
        # Search for job
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "jobs-search-box-keyword-id-ember24"))
        )
        search_box.send_keys(job_title)
        search_box.submit()
        
        # Wait for job search results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "jobResults"))
        )
        
        # Apply for job
        apply_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-control-name='jobdetails_apply_button']"))
        )
        apply_button.click()
        
        # Confirm application
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-control-name='confirm_apply_button']"))
        )
        confirm_button.click()
        
        print(f"Applied for {job_title} on LinkedIn")
    except TimeoutException:
        print(f"Failed to apply for {job_title} on LinkedIn")
    except Exception as e:
        print(f"Error applying for {job_title} on LinkedIn: {e}")
linkedin_cookies = driver.get_cookies()

# Internshala Configuration
internshala_url = driver.get("https://internshala.com/")

def apply_on_internshala(job_title):
    try:
        driver.get(internshala_url)
        for cookie in internshala_cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        
        # Search for job
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search_bar"))
        )
        search_box.send_keys(job_title)
        search_box.submit()
        
        # Wait for job search results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "job_list"))
        )
        
        # Apply for job
        apply_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='apply_button']"))
        )
        apply_button.click()
        
        # Confirm application
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='confirm_apply_button']"))
        )
        confirm_button.click()
        
        print(f"Applied for {job_title} on Internshala")
    except TimeoutException:
        print(f"Failed to apply for {job_title} on Internshala")
    except Exception as e:
        print(f"Error applying for {job_title} on Internshala: {e}")
internshala_cookies = driver.get_cookies()

# Set cookies for the program
linkedin_cookies = [cookie["value"] for cookie in linkedin_cookies]
internshala_cookies = [cookie["value"] for cookie in internshala_cookies]


job_title = "Software Engineer"
apply_on_linkedin(job_title)
apply_on_internshala(job_title)

# Close WebDriver
try:
    driver.quit()
except Exception as e:
    print(f"Error quitting driver: {e}")
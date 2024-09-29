import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# LinkedIn Configuration
linkedin_url = "https://www.linkedin.com/"
driver.get(linkedin_url)
linkedin_cookies = driver.get_cookies()
linkedin_cookies = [{'name': cookie['name'], 'value': cookie['value'], 'domain': cookie['domain'], 'path': cookie['path']} for cookie in linkedin_cookies]

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
        
        logging.info(f"Applied for {job_title} on LinkedIn")
    except TimeoutException:
        logging.error(f"Failed to apply for {job_title} on LinkedIn (Timeout)")
    except Exception as e:
        logging.error(f"Error applying for {job_title} on LinkedIn: {e}")

# Internshala Configuration
internshala_url = "https://internshala.com/"
driver.get(internshala_url)
internshala_cookies = driver.get_cookies()
internshala_cookies = [{'name': cookie['name'], 'value': cookie['value'], 'domain': cookie['domain'], 'path': cookie['path']} for cookie in internshala_cookies]

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
        
        logging.info(f"Applied for {job_title} on Internshala")
    except TimeoutException:
        logging.error(f"Failed to apply for {job_title} on Internshala (Timeout)")
    except Exception as e:
        logging.error(f"Error applying for {job_title} on Internshala: {e}")

def main():
    job_title = input("Enter the job title: ")
    if job_title:
        apply_on_linkedin(job_title)
        apply_on_internshala(job_title)
    else:
        logging.error("Job title is required")

if __name__ == "__main__":
    try:
        main()
    finally:
        try:
            driver.quit()
        except Exception as e:
            logging.error(f"Error quitting driver: {e}")

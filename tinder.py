from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from credentials import *
from time import sleep
import random
import openai




openai.api_key = "YOUR_API_KEY"


URL = "https://tinder.com"
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.maximize_window()
browser.get(URL)
actions = ActionChains(browser)

sleep(5)
cookies = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]")
cookies.click()
sleep(3)
login = browser.find_element(By.XPATH,"//*[text()='Log in']")
login.click()
sleep(4)
facebook = browser.find_element(By.XPATH,"//*[text()='Login with Facebook']")
facebook.click()
sleep(4)

browser.switch_to.window(browser.window_handles[1])

sleep(3)
email = browser.find_element(By.XPATH,"//*[@id='email']")
email.send_keys(EMAIL)
password = browser.find_element(By.XPATH,"//*[@id='pass']")
password.send_keys(PASSWORD+Keys.ENTER)
sleep(10)




# Wait for the main page to load
sleep(10)

# Loop to swipe, like and dislike profiles
for i in range(10):
    try:
        like_button = browser.find_element_by_xpath("//button[@aria-label='Like']")
        like_button.click()
        print("Liked profile")
    except:
        try:
            dislike_button = browser.find_element_by_xpath("//button[@aria-label='Nope']")
            dislike_button.click()
            print("Disliked profile")
        except:
            print("No more profiles to swipe")

        sleep(2)

# Find matches and start conversation
matches_button = browser.find_element_by_xpath("//a[@href='/app/matches']")
matches_button.click()

sleep(5)

# Click on the first match and send a message
match_card = browser.find_element_by_xpath("//div[@class='matchListItem']//a")
match_card.click()

sleep(5)



# Wait for the user to log in and navigate to the message screen
sleep(10) # increase or decrease as necessary
matches_button = browser.find_element_by_xpath('//*[@id="match-tab"]')
matches_button.click()

# Wait for the user to find a match and navigate to the chat screen
sleep(10) # increase or decrease as necessary
match = browser.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/span/span')
match.click()

# Start a conversation with a match using OpenAI API
prompt = "Hello, I'm so excited to match with you! What's your name?"
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5
)
message = response.choices[0].text.strip()
chat_input = browser.find_element_by_xpath('//*[@id="chat-text-area"]')
chat_input.send_keys(message)
send_button = browser.find_element_by_xpath('//*[@id="SendMessageForm"]/div[2]/button')
send_button.click()

# Continuously reply to messages with romantic responses using OpenAI API
while True:
    sleep(10) # increase or decrease as necessary
    messages = browser.find_elements_by_xpath('//*[@id="chat-messages"]/div/div')
    last_message = messages[-1].find_element_by_xpath('.//span').text
    prompt = f"I think you're so {last_message}! What do you think?"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5
    )
    message = response.choices[0].text.strip()
    chat_input = browser.find_element_by_xpath('//*[@id="chat-text-area"]')
    chat_input.send_keys(message)
    send_button = browser.find_element_by_xpath('//*[@id="SendMessageForm"]/div[2]/button')
    send_button.click()


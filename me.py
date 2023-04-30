body = browser.find_element(By.TAG_NAME,"body")


def press(key):
    actions.send_keys(key)
    actions.perform()

def like(times = 100,city=None):
    likes = 0
    dislikes = 0
    notinterested = True
    for i in range(times):
       
        try:
            # Open Profile
            press(Keys.ARROW_UP)
            sleep(3)
            if (city is None):
                press(Keys.ARROW_RIGHT)
                likes +=1
                sleep(3)
            else:
                try:
                    browser.find_element(By.XPATH,f"//*[text()='Lives in {city}']").is_displayed()
                    print("Found")
                    # Like profile
                    press(Keys.ARROW_RIGHT)
                    likes +=1
                    sleep(3)

                except NoSuchElementException:
                    print("Not found")
                    # Dislike profile
                    press(Keys.ARROW_LEFT)
                    dislikes +=1
                    sleep(3)
            

            # This popup happens only once that's why we will stop this test after it's displayed
            if (notinterested):
                try:
                    browser.find_element(By.XPATH,"//div[text()='Not interested']").is_displayed()
                    press(Keys.ESCAPE)
                    print("Not interested is displayed")
                    notinterested = False
                    sleep(2)
                except NoSuchElementException:
                    print("Not interested isn't displayed")

            # This pop that let's you know that you're out of likes -> we will break when that's happen
            try:
                browser.find_element(By.XPATH,"//*[text()='No Thanks']").is_displayed()
                press(Keys.ESCAPE)
                print("Out of Likes")
                break
            except NoSuchElementException:
                print("Still likes")
                sleep(5)

        except:

            print("Exception raised in like function")
            
          
    # print out the number of likes and dislikes    
    print(f"You have liked : {likes} and disliked : {dislikes}")

def dislike(times = 100):

    notinterested = True
    for i in range(times):

        try:            

            # This popup happens only once that's why we will stop this test after it's displayed
            if (notinterested):
                try:
                    browser.find_element(By.XPATH,"//div[text()='Not interested']").is_displayed()
                    press(Keys.ESCAPE)
                    print("Not interested is displayed")
                    notinterested = False
                    sleep(2)
                except NoSuchElementException:
                    print("Not interested isn't displayed")

            # This pop that let's you know that you're out of likes -> we will break when that's happen
            try:
                browser.find_element(By.XPATH,"//*[text()='No Thanks']").is_displayed()
                press(Keys.ESCAPE)
                print("Out of Likes")
                break
            except NoSuchElementException:
                print("Still likes")
                sleep(5)
            
            # dislike
            press(Keys.ARROW_LEFT)
            sleep(2)
        except:

            print("Exception raised in like function")

def message():
    try:
        
        matches_panel = browser.find_element(By.XPATH,"//button[text()='Matches']")
        matches_panel.click()
        matches = browser.find_elements(By.CLASS_NAME,"matchListItem")
        
        for match in matches:
            matches_panel.click()
            if("Likes" not in match.accessible_name):
                match.click()
                sleep(4)
                name = browser.find_element(By.TAG_NAME,"h1").accessible_name
                pickupline = random.choice(PICKUPLINES)
                msg = f"Hi {name} {pickupline}"
                press(msg)
                send = browser.find_element(By.XPATH,"//*[@id='c-1351236777']/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button[2]")
                send.click()

                sleep(3)
        print("Messages were sent successfully  ")
    except:
        print("Exception raised in message function")




like(10,"Lappeenranta")

message()
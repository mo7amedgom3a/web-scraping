import mechanicalsoup
import time

browser = mechanicalsoup.StatefulBrowser()

login_url = "http://localhost:5000"

username = "user1"
password = "password1"

num_requests = 100

# Interval between requests in seconds
request_interval = 2

def perform_login_and_scrape():
    browser.open(login_url)

    browser.select_form('form')

    browser["username"] = username
    browser["password"] = password

    response = browser.submit_selected()

    if response.status_code == 429:
        print("Too many requests. Please try again later.")
        display_angry_cat()
        return False
    elif response.status_code == 200 and "Welcome" in browser.get_current_page().text:
        print("Successfully logged in and accessed the dashboard!")
        # Extract the dashboard message
        message = browser.get_current_page().find("p").text
        print(f"Dashboard Message: {message}")
        return True
    else:
        print("Login failed or unexpected response.")
        return False

def display_angry_cat():
    print("""
       |\---/|
       | ,_, |
        \_`_/-..----.
     ___/ `   ' ,""+ \  
    (__...'   __\    |`.___.';
      (_,...'(_,.`__)/'.....+
    """)
    print("Angry cat says: Please try again later!")

if __name__ == "__main__":
    for i in range(num_requests):
        print(f"Attempt {i+1}:")
        if perform_login_and_scrape():
            break
        time.sleep(request_interval)

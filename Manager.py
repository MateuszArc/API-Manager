import requests
import html
import webbrowser

class API_MANAGER:
    def __init__(self, url_of_api, amount, type):
        self.API = url_of_api
        self.data = None
        self.response = None
        self.parameters = {
            "amount":amount,
            "type":type
        }

    def open_in_browser(self):
        webbrowser.open(self.API)
        webbrowser.open_new_tab(self.API)

    def connect(self):
        self.response = requests.get(self.API, params=self.parameters)
        if self.response.status_code == 200:
            return self.response.json()
        return False

    def get_data(self):
        try:
            self.data = self.connect() 
        except:
            return False
        
    def format_data(self):
        self.data = html.unescape(self.data)

    def return_data(self):
        return self.data

"""test = API_MANAGER(url_of_api="https://opentdb.com/api.php?amount=20&category=15&type=boolean", amount=10, type="boolean")
test.get_data()
test.format_data()
print(test.data)"""
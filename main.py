#-------------------------CONSTANTS-------------------------#
from Manager import API_MANAGER
from tkinter import *
from tkinter import messagebox 
from constants import *
import time
import html
import replit
import requests

#-------------------------Combining all things to make App work -------------------------#
if __name__ == "__main__":
    try:
        data = ""

        def get_data():
            global api_url_entry
            api = api_url_entry.get()
            if api == "":
                messagebox.showerror(title=App_Name, message="Don't leave API field empty!")
            else:
                manager = API_MANAGER(api, 20, "boolean")
                check = requests.get(api).status_code
                if check == 200:
                    global data
                    data = manager.get_data()
                    messagebox.showinfo(title=App_Name, message="Data downloaded correctly!")                
                else:
                    if check == 400:
                        messagebox.showerror(title="API Manager Error", message=f"Error Number: {check}\nAPI:{api}\nReason: Bad Request to API!")
                    elif check == 401:
                        messagebox.showerror(title="API Manager Error", message=f"Error Number: {check}\nAPI:{api}\nReason: You don't have permission to connect to this API!")
                    elif check == 402:
                        messagebox.showerror(title="API Manager Error", message=f"Error Number: {check}\nAPI:{api}\nReason: You need to pay to connect to API!")
                    elif check == 403:
                        messagebox.showerror(title="API Manager Error", message=f"Error Number: {check}\nAPI:{api}\nReason: The API doesn't want to connect!")
                    elif check == 404:
                        messagebox.showerror(title="API Manager Error", message=f"Error Number: {check}\nAPI:{api}\nReason: The API is nowhere to be found!")
                    else:
                        messagebox.showerror(title="API Manager Error", message=f"Error Number: {check}\nAPI:{api}\nReason: The API just stepped on a LEGO...")

        def return_data():
            global api_url_entry
            api = api_url_entry.get()
            if api == "":
                messagebox.showerror(title="Error!", message="Don't leave API field empty!")
            else:
                manager = API_MANAGER(api, 20, "boolean")
                manager.get_data()
                data = manager.data
                if not data == None:
                    data = html.unescape(str(data))
                    print(data)
                else:
                    refreshing_info = messagebox.showinfo(title=App_Name,message="App is refreshing...")
                    time.sleep(0.1)
                    
        def clear_api_entry():
            global api_url_entry
            api_url_entry.delete(0,"end")

        def write_data_to_file():
            try:
                global api_url_entry
                api = api_url_entry.get()
                manager = API_MANAGER(api, 20, "boolean")
                manager.get_data()
                data = manager.data
                with open(f"API_Data.txt", 'w') as file:
                    file.write(html.unescape(str(data)))
            except:
                exit()


        window = Tk()
        window.config(padx=100, pady=200, bg=THEME_COLOR)
        window.title(App_Name)
        canvas = Canvas(width=500, height=800)
        
        GetDataButton = Button(text="Get Data From -->",command=get_data)
        GetDataButton.grid(column=1, row=2)
        ReturnDataButton = Button(text="Return Data",command=return_data)
        ReturnDataButton.grid(column=4,row=3)
        WriteToFileButton = Button(text="Write Data to file",command=write_data_to_file)
        WriteToFileButton.grid(column=3,row=3)
        deleteEntryButton = Button(text="Clear API entry",command=clear_api_entry)
        deleteEntryButton.grid(column=4,row=2)

        other_label = Label(text="Other Operations")
        other_label.grid(column=3,row=2)

        api_url_entry = Entry(width=35)
        api_url_entry.grid(column=2, row=2)


        mainloop()
    except:
        print("Error in Application!")
    else:
        print("Great!")
    finally:
        print("Ty For Using API Manager :D")
    print("Press *Enter* to exit")
    input()
    replit.clear()
    
    #Few APIs:
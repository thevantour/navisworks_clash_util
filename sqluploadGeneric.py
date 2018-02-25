# pyinstaller -F -w -n <file name.exe> --icon <ico file name> main.py 
from tkinter import filedialog
from tkinter import *
import pandas as pd
import sqlalchemy

#%%
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        
    def init_window(self):
        self.master.title("Clash Grouper SQL Uploader")
        self.pack(fill = BOTH, expand = 1)

        # File Menu
        menu = Menu(self.master)
        self.master.config(menu = menu)
        
        # Exit Button - runs client_exit
        file = Menu(menu)
        file.add_command(label = 'Exit', command = self.client_exit)
        menu.add_cascade(label='File', menu=file)
        
        analysis = Menu(menu)
        analysis.add_command(label='Cost Breakdown')
        menu.add_cascade(label='Analysis', menu = analysis)
        
        # Directions Text Box
        directions = Label(root, justify = LEFT, 
                           text="\n--------------------------------------------------------------------------------")
        directions.place(x = 5, y = 0)
        
        # Import File Button - runs open_file
        importButton = Button(root, text = 'Select File', command = self.import_file)
        importButton.place(x = 5, y= 45)        
        
        # Table Name Entry Box
        mainJobLabel = Label(root, justify = LEFT, text = "Table Name: ")
        mainJobLabel.place(x = 5, y = 75)
        global jobVar
        jobVar = StringVar()
        jobEntryBox = Entry(root, textvariable=jobVar, width = 30)
        jobEntryBox.pack()
        jobEntryBox.place(x = 80, y = 75)
        jobVar.set("<Input Table Name>")
        
        # Convert Button - runs convert_file 
        convertButton = Button(root, text = 'Convert and Save', command = self.convert_file)
        convertButton.place(x = 5, y= 110)
        
        # Email Text Box
        email = Label(root, justify = LEFT, 
                           text="Questions, errors, or comments? Email me --> graham.rose@whiting-turner.com")
        email.place(x = 5, y = 155)


#%%        
    # Exit Function    
    def client_exit(self):
        root.destroy()
    
    # Import File Function
    def import_file(self):
        global df
        file_path_string = filedialog.askopenfilename()
        df = pd.read_csv(file_path_string,encoding='utf-8', header = None)
        
    # Convert File to CMiC format
    def convert_file(self):
        
        # Define globals
        global export
        global df
        
        global jobVar
        table_name = str(jobVar.get())
        df2 = pd.DataFrame(data = [1,2,3])       
        Engine = sqlalchemy.create_engine("mssql+pyodbc://<user>:<pass>@<address>/<database>?driver=ODBC Driver 13 for SQL Server", echo=False)
        print("writing to sql")
        
        df2.to_sql(table_name, con = Engine, if_exists = 'replace')
        print("write complete")

        
        
        
#        file_path_string = filedialog.asksaveasfilename()
#        export.to_csv(str(file_path_string), index = False, header = False)
        
#%%    
root = Tk()
root.geometry("440x180")
app = Window(root)
root.mainloop()


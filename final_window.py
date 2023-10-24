# examples for code pulled from :
# https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
# https://stackoverflow.com/questions/42828416/print-output-in-gui-interface-tkinter-python
# https://realpython.com/python-gui-tkinter/#controlling-layout-with-geometry-managers
# https://www.geeksforgeeks.org/python-gui-tkinter/ 


import tkinter as tk

from final_state import State

from final_map import Map


    

   
            
class FinalWindow:
    
    def __init__(self):
        """initializes the interactive window """
        self.mainwindow = tk.Tk()

    def windowmaker(self):
        """makes the window """
        self.mainwindow.title('States')
        self.mainwindow.resizable(0, 0)
        self.buttonsMainWindow()
        self.mainwindow.mainloop()

    def createNewWindow(self, button):
        """ creates each individual state's pop up window for when button is pressed """
        newWindow = tk.Toplevel(self.mainwindow)
        state = button['text']
        newWindow.title(state)
        states = State()
        printed_winner = states.print_winner(state)
        printed_loser = states.print_loser(state)
        printed_masks = states.print_masks(state)
        statelabel = tk.Label(master = newWindow, text = state)
        statelabel.grid(row = 0, column = 0)
        winnerlabel = tk.Label(master = newWindow, text= printed_winner)
        winnerlabel.grid(row = 1, column = 0)
        loserlabel = tk.Label(master = newWindow, text= printed_loser)
        loserlabel.grid(row = 2, column = 0)
        maskslabel = tk.Label(master = newWindow, text= printed_masks)
        maskslabel.grid(row = 3, column = 0)
        
    
    
    def makeMap(self):
        usmap = Map()
        usmap.makemap()
     
    def buttonsMainWindow(self):
        """ creates and adds all the buttons for the main window """
        alabama = tk.Button(master=self.mainwindow, text='Alabama', width = 10, command = lambda: self.createNewWindow(alabama))
        alabama.grid(row = 1, column = 0) 
        alaska = tk.Button(master=self.mainwindow, text='Alaska', width = 10, command = lambda: self.createNewWindow(alabama))
        alaska.grid(row = 1 , column = 1)
        arizona = tk.Button(master=self.mainwindow, text='Arizona', width = 10, command = lambda: self.createNewWindow(arizona))
        arizona.grid(row = 1 , column = 2)
        arkansas  = tk.Button(master=self.mainwindow, text='Arkansas', width = 10, command = lambda: self.createNewWindow(arkansas))
        arkansas.grid(row = 1 , column = 3)
        california = tk.Button(master=self.mainwindow, text='California', width = 10, command = lambda: self.createNewWindow(california))
        california.grid(row = 1 , column = 4)
        colorado  = tk.Button(master=self.mainwindow, text='Colorado', width = 10, command = lambda: self.createNewWindow(colorado))
        colorado.grid(row = 1 , column = 5)
        connecticut = tk.Button(master=self.mainwindow, text='Connecticut', width = 10, command = lambda: self.createNewWindow(connecticut))
        connecticut.grid(row = 1 , column = 6)
        delaware = tk.Button(master=self.mainwindow, text='Delaware', width = 10, command = lambda: self.createNewWindow(delaware))
        delaware.grid(row = 1 , column = 7)
        florida = tk.Button(master=self.mainwindow, text='Florida', width = 10, command = lambda: self.createNewWindow(florida))
        florida.grid(row = 1 , column = 8)
        georgia = tk.Button(master=self.mainwindow, text='Georgia', width = 10, command = lambda: self.createNewWindow(georgia))
        georgia.grid(row = 2 , column = 0)
        hawaii = tk.Button(master=self.mainwindow, text='Hawaii', width = 10, command = lambda: self.createNewWindow(hawaii))
        hawaii.grid(row = 2 , column = 1)
        idaho = tk.Button(master=self.mainwindow, text='Idaho', width = 10, command = lambda: self.createNewWindow(idaho))
        idaho.grid(row = 2 , column = 2)
        illinois = tk.Button(master=self.mainwindow, text='Illinois', width = 10, command = lambda: self.createNewWindow(illinois))
        illinois.grid(row = 2 , column =3)
        indiana = tk.Button(master=self.mainwindow, text='Indiana', width = 10, command = lambda: self.createNewWindow(indiana))
        indiana.grid(row = 2 , column = 4)
        iowa = tk.Button(master=self.mainwindow, text='Iowa', width = 10, command = lambda: self.createNewWindow(iowa))
        iowa.grid(row = 2 , column = 5)
        kansas = tk.Button(master=self.mainwindow, text='Kansas', width = 10, command = lambda: self.createNewWindow(kansas))
        kansas.grid(row = 2 , column = 6)
        kentucky = tk.Button(master=self.mainwindow, text='Kentucky', width = 10, command = lambda: self.createNewWindow(kentucky))
        kentucky.grid(row = 2 , column = 7)
        louisiana = tk.Button(master=self.mainwindow, text='Louisiana', width = 10, command = lambda: self.createNewWindow(louisiana))
        louisiana.grid(row = 2 , column = 8)
        maine = tk.Button(master=self.mainwindow, text='Maine', width = 10, command = lambda: self.createNewWindow(maine))
        maine.grid(row = 3 , column = 0)
        maryland = tk.Button(master=self.mainwindow, text='Maryland', width = 10, command = lambda: self.createNewWindow(maryland))
        maryland.grid(row = 3 , column = 1)
        massachusetts = tk.Button(master=self.mainwindow, text='Massachusetts', width = 10, command = lambda: self.createNewWindow(massachusetts))
        massachusetts.grid(row = 3 , column = 2)
        michigan = tk.Button(master=self.mainwindow, text='Michigan', width = 10, command = lambda: self.createNewWindow(michigan))
        michigan.grid(row = 3 , column = 3)
        minnesota = tk.Button(master=self.mainwindow, text='Minnesota', width = 10, command = lambda: self.createNewWindow(minnesota))
        minnesota.grid(row = 3 , column = 4)
        mississippi = tk.Button(master=self.mainwindow, text='Mississippi', width = 10, command = lambda: self.createNewWindow(mississippi))
        mississippi.grid(row = 3 , column = 5)
        missouri = tk.Button(master=self.mainwindow, text='Missouri', width = 10, command = lambda: self.createNewWindow(missouri))
        missouri.grid(row = 3 , column = 6)
        montana = tk.Button(master=self.mainwindow, text='Montana', width = 10, command = lambda: self.createNewWindow(montana))
        montana.grid(row = 3 , column = 7)
        nebraska= tk.Button(master=self.mainwindow, text='Nebraska', width = 10, command = lambda: self.createNewWindow(nebraska))
        nebraska.grid(row = 3 , column = 8)
        nevada = tk.Button(master=self.mainwindow, text='Nevada', width = 10, command = lambda: self.createNewWindow(nevada))
        nevada.grid(row = 4 , column = 0)
        newhampshire= tk.Button(master=self.mainwindow, text='New Hampshire', width = 10, command = lambda: self.createNewWindow(newhampshire))
        newhampshire.grid(row = 4 , column = 1)
        newjersey = tk.Button(master=self.mainwindow, text='New Jersey', width = 10, command = lambda: self.createNewWindow(newjersey))
        newjersey.grid(row = 4 , column = 2)
        newmexico= tk.Button(master=self.mainwindow, text='New Mexico', width = 10, command = lambda: self.createNewWindow(newmexico))
        newmexico.grid(row = 4 , column = 3)
        newyork= tk.Button(master=self.mainwindow, text='New York', width = 10, command = lambda: self.createNewWindow(newyork))
        newyork.grid(row = 4 , column = 4)
        northcarolina= tk.Button(master=self.mainwindow, text='North Carolina', width = 10, command = lambda: self.createNewWindow(northcarolina))
        northcarolina.grid(row = 4 , column = 5)
        northdakota= tk.Button(master=self.mainwindow, text='North Dakota', width = 10, command = lambda: self.createNewWindow(northdakota))
        northdakota.grid(row = 4 , column = 6)
        ohio = tk.Button(master=self.mainwindow, text='Ohio', width = 10, command = lambda: self.createNewWindow(ohio))
        ohio.grid(row = 4 , column = 7)
        oklahoma= tk.Button(master=self.mainwindow, text='Oklahoma', width = 10, command = lambda: self.createNewWindow(oklahoma))
        oklahoma.grid(row = 4 , column = 8)
        oregon= tk.Button(master=self.mainwindow, text='Oregon', width = 10, command = lambda: self.createNewWindow(oregon))
        oregon.grid(row = 5 , column = 0)
        pennsylvania= tk.Button(master=self.mainwindow, text='Pennsylvania', width = 10, command = lambda: self.createNewWindow(pennsylvania))
        pennsylvania.grid(row = 5 , column = 1)
        rhodeisland = tk.Button(master=self.mainwindow, text='Rhode Island', width = 10, command = lambda: self.createNewWindow(rhodeisland))
        rhodeisland.grid(row = 5 , column = 2)
        southcarolina= tk.Button(master=self.mainwindow, text='South Carolina', width = 10, command = lambda: self.createNewWindow(southcarolina))
        southcarolina.grid(row = 5 , column = 3)
        southdakota= tk.Button(master=self.mainwindow, text='South Dakota', width = 10, command = lambda: self.createNewWindow(southdakota))
        southdakota.grid(row = 5 , column = 4)
        tennessee= tk.Button(master=self.mainwindow, text='Tennessee', width = 10, command = lambda: self.createNewWindow(tennessee))
        tennessee.grid(row = 5 , column = 5)
        texas= tk.Button(master=self.mainwindow, text='Texas', width = 10, command = lambda: self.createNewWindow(texas))
        texas.grid(row = 5 , column = 6)
        utah= tk.Button(master=self.mainwindow, text='Utah', width = 10, command = lambda: self.createNewWindow(utah))
        utah.grid(row = 5 , column = 7)
        vermont= tk.Button(master=self.mainwindow, text='Vermont', width = 10, command = lambda: self.createNewWindow(vermont))
        vermont.grid(row = 5 , column = 8)
        virginia= tk.Button(master=self.mainwindow, text='Virginia', width = 10, command = lambda: self.createNewWindow(virginia))
        virginia.grid(row = 6 , column = 0)
        washington= tk.Button(master=self.mainwindow, text='Washington', width = 10, command = lambda: self.createNewWindow(washington))
        washington.grid(row = 6 , column = 1)
        washingtondc= tk.Button(master=self.mainwindow, text='Washington D.C.', width = 10, command = lambda: self.createNewWindow(washingtondc))
        washingtondc.grid(row = 6 , column = 2)
        westvirginia= tk.Button(master=self.mainwindow, text='West Virginia', width = 10, command = lambda: self.createNewWindow(westvirginia))
        westvirginia.grid(row = 6 , column = 3)
        wisconsin= tk.Button(master=self.mainwindow, text='Wisconsin', width = 10, command = lambda: self.createNewWindow(wisconsin))
        wisconsin.grid(row = 6 , column = 4)
        wyoming= tk.Button(master=self.mainwindow, text='Wyoming', width = 10, command = lambda: self.createNewWindow(wyoming))
        wyoming.grid(row = 6 , column = 5)
        makemap = tk.Button(master = self.mainwindow, text ='Map of Winners', width = 10, command = self.makeMap)
        makemap.grid(row = 0, column = 4)
    
        
    








if __name__ == "__main__":
    
    
    window = FinalWindow()
    window.windowmaker()
    
    
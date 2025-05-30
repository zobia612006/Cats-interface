import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Cat:
    #PRIVATE CatName : STRING
    #PRIVATE FurColour : INTEGER
    #PRIVATE EyeColour : INTEGER
    #PRIVATE Age : INTEGER
    #PRIVATE Breed : STRING

    def __init__(self,cn,fc,ec,a,b,p):
        self.__CatName=cn
        self.__FurColour=fc
        self.__EyeColour=ec
        self.__Age= a
        self.__Breed=b
        self.__Price=p

    def GetCatName(self):
        return self.__CatName
    
    def GetFurColour(self):
        return self.__FurColour
    
    def GetEyeColour(self):
        return self.__EyeColour
    
    def GetAge(self):
        return self.__Age
    
    def GetBreed(self):
        return self.__Breed
    
    def GetPrice(self):
        return self.__Price
    
def ReadData():
    CatArray=[] #Array of objects 9 elements type Cat
    try:
        file=open(r"C:\Users\zobia\OneDrive\Desktop\okay06\Cats.txt","r")
        for i in range(86):
            line= file.readline().strip()
            CatName,FurColour,EyeColour,Age,Breed,Price= line.split(',')
            CatObject= Cat(CatName,FurColour,EyeColour,int(Age),Breed,Price)
            CatArray.append(CatObject)
        file.close()
    except IOError:
        print("file not found")
        messagebox.showerror("Error :" , "File not found")
    return CatArray

def PrintCats(CatObject):
    return CatObject.GetCatName() + " is a " + CatObject.GetBreed() + " cat of age " + str(CatObject.GetAge()) + " and has " + CatObject.GetFurColour() + " fur. It has " + CatObject.GetEyeColour() + " eyes and it's price is " + str(CatObject.GetPrice()) + "\n"
   


def ChooseCats(Arrayx,Breed,FurColour,EyeColour):
    ApprovedCats=[]
    for cat in Arrayx:
        if (cat.GetBreed().lower()== Breed.lower() and  cat.GetFurColour().lower()== FurColour.lower() and cat.GetEyeColour().lower()== EyeColour.lower()):
            ApprovedCats.append(cat)
    return ApprovedCats

def SearchCats():
    global Cats,CatNames
    Breed= BreedEntry.get()
    FurColour=FurColourEntry.get()
    EyeColour=EyeColourEntry.get()

    FoundCats= ChooseCats(Cats,Breed,FurColour,EyeColour)

    result_text.delete(1.0,tk.END)
    CatNames.clear()

    if FoundCats:
        for cat in FoundCats:
            result_text.insert(tk.END,PrintCats(cat))
            CatNames.append(cat.GetCatName())
        ComboBox['values']= CatNames

    else:
        result_text.insert(tk.END, "Sorry, no cats fulfill your requirements.\n")
        ComboBox['values']=[]

def ConfirmSelection():
    global Cats
    SelectedCatName=ComboBox.get()
    for cat in Cats:
        if cat.GetCatName()==SelectedCatName:
            Price=cat.GetPrice()
            messagebox.showinfo("Purchase Confirmed", f"You have chosen the cat: {SelectedCatName}, Price: {Price}")

Cats=ReadData()
CatNames=[]

window= tk.Tk()
window.title("Find Your Cat!")
window.geometry("600x600")
window.configure(bg='#fefef7')

Heading=tk.Label(window, text="Choose your cat!", font=("Arial",20,"bold"), bg='#fefef7',fg='#A0522D')
Heading.pack(pady=10)

tk.Label(window,text="Breed(Persian, Burmese, Sphynx, Bengal or Ragdoll):" , bg= '#fefef7', fg='#A0522D').pack(pady=5)
BreedEntry=tk.Entry(window)
BreedEntry.pack(pady=5)

tk.Label(window, text="FurColour(black, brown, orange, white, gray):", bg='#fefef7', fg='#A0522D').pack(pady=5)
FurColourEntry= tk.Entry(window)
FurColourEntry.pack(pady=5)

tk.Label(window, text="EyeColour(hazel, orange, gray, blue, green):", bg='#fefef7', fg='#A0522D').pack(pady=5)
EyeColourEntry= tk.Entry(window)
EyeColourEntry.pack(pady=5)

Search= tk.Button(window, text= "Search Cats", command= SearchCats, bg= '#D3B8A1', fg= 'black')
Search.pack(pady=10)

result_text= tk.Text(window, width=50, height=10, bg= '#f5f5dc', fg='black')
result_text.pack(pady=10)

ComboBoxLabel= tk.Label(window, text="Select Cat:" , bg='#fefef7', fg= '#A0522D')
ComboBoxLabel.pack(pady=5)
ComboBox=ttk.Combobox(window)
ComboBox.pack(pady=5)

ConfirmButton=tk.Button(window,text= "Buy Cat", command= ConfirmSelection, bg='#D3B8A1', fg='black')
ConfirmButton.pack(pady=10)

window.mainloop()

























    








    






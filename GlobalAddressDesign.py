
# coding: utf-8

# In[ ]:

from tkinter import *
from tkinter import ttk

class GlobalAddress_Design(Frame):
    #========================================#
    #GUI configurations (Design)
    #========================================#
    def initUI(self):
        Frame.__init__(self)
        self.master.title("Global Address Batch")
#         self.master.grid_rowconfigure(0,weight =1)
        self.master.grid_columnconfigure(1, weight = 1)
        self.master.grid_columnconfigure(2, weight = 1)
        self.master.grid_columnconfigure(3, weight = 1)
        #Left and Right Frames
        lFrame = Frame(self.master)
        lFrame.grid(column=1,row=0)
        mFrame = Frame(self.master)
        mFrame.grid(column=2,row = 0)
        rFrame = Frame(self.master)
        rFrame.grid(column = 3 , row = 0 )

        #========================================#
        #File
        #========================================#
        inputFrame = Frame(lFrame,bd = 2)
        
        lblLicense = Label(inputFrame,text = "Set License String")
        lblLicense.pack()
        self.txtLicense = Entry(inputFrame,width = 30)
##        self.txtLicense.bind('<Return>' , (lamda event: self.fetch())
        self.txtLicense.insert(END,"ENTER_LICENSE")
        self.txtLicense.pack()
        
        inputFrame.pack()
        
        #========================================#
        #File
        #========================================#
        fileFrame = Frame(lFrame,bd = 1,pady = 30, relief = 'groove')
        
        lblInputFile = Label(fileFrame, text = "Input File", font = 'Helvetica 12 bold')
        lblInputFile.pack()

        browseFrame = Frame(fileFrame,bd = 1)
        
        btnBrowse = Button(browseFrame,text = "Input File", command = self.browse_button)
        btnBrowse.pack(side = 'left', anchor = W,padx = 5)
        
        self.lblFilePath= Label(browseFrame,width = 30,relief = "sunken", anchor = "w")
        self.lblFilePath.pack(side = 'left')
        browseFrame.pack(padx =10)
        
        lblDelimiters = Label(fileFrame, text="Delimiters")
        lblDelimiters.pack()
        self.cmbDelim = ttk.Combobox(fileFrame,values = ["Comma","Tab","Pipe"])
        self.cmbDelim.current(0)
        self.cmbDelim.pack() 

        lblTextQualifier = Label(fileFrame, text = "Text Qualifier")
        lblTextQualifier.pack()
        self.cmbTextQualifier = ttk.Combobox(fileFrame, values=["None","Double Quote"])
        self.cmbTextQualifier.current(1)
        self.cmbTextQualifier.pack()
        
        lblOutputFile = Label(fileFrame, text = "Output File", font = 'Helvetica 12 bold')
        lblOutputFile.pack()
        
        outputFrame = Frame(fileFrame,bd = 1)
        
        btnOutput = Button(outputFrame,text = "Output File", command = self.outputFile_button)
        btnOutput.pack(side = 'left', anchor = W,padx = 5)
        
        self.lblOutputFilePath= Label(outputFrame,width = 30,relief = "sunken", anchor = "w")
        self.lblOutputFilePath.pack(side = 'left')
        outputFrame.pack(padx =10)
        
        fileFrame.pack(expand = 1, padx = 20, pady = 20)
        
        #========================================#
        #Options
        #========================================#
        oFrame = Frame(lFrame,bd = 1, relief = 'groove')
        
        lblOptions = Label(oFrame, text = "OPTIONS", font = 'Helvetica 12 bold')
        lblOptions.pack()
        
#         #Filler        
#         fillerFrame = Frame(oFrame)
#         lblBlank4 = Label(fillerFrame)
#         lblBlank4.pack(side = 'left')
#         lblBlank5 = Label(fillerFrame)
#         lblBlank5.pack(side= 'left',expand = 1)
#         fillerFrame.pack()
        
                
        lblDeliveryLines = Label(oFrame, text = "Delivery Lines")
        lblDeliveryLines.pack()
        self.cmbDeliveryLines = ttk.Combobox(oFrame,values = ['Off','On'])
        self.cmbDeliveryLines.pack()
        self.cmbDeliveryLines.current(0)
        
        lblLineSeparator = Label(oFrame, text = "Line Separator")
        lblLineSeparator.pack()
        self.cmbLineSeparator = ttk.Combobox(oFrame, values = ['SEMICOLON', 'PIPE', 'CR' , 'LF', 'CRLF', 'TAB' ,'BR'])
        self.cmbLineSeparator.pack()
        self.cmbLineSeparator.current(0)
        
        lblOutputScript = Label(oFrame, text = "Output Script")
        lblOutputScript.pack()
        self.cmbOutputScript = ttk.Combobox(oFrame, values = ['NoChange','Latin','Native'])
        self.cmbOutputScript.pack()
        self.cmbOutputScript.current(0)
        
        lblOutputGeo = Label(oFrame, text = "Output Geo")
        lblOutputGeo.pack()
        self.cmbOutputGeo = ttk.Combobox(oFrame, values = ['On','Off'])
        self.cmbOutputGeo.pack()
        self.cmbOutputGeo.current(0)
        
        lblCountryOrigin = Label(oFrame, text = "Country of Origin")
        lblCountryOrigin.pack()

        
        self.txtCountry = Entry(oFrame,width = 30)
##        self.txtCountry.bind('<Return>' , (lamda event: self.fetch2())
        self.txtCountry.insert(END,"")
##        self.txtCountry.bind('<Return>', self.show_output)
        self.txtCountry.pack()
        
        oFrame.pack()
        
        #========================================#
        #COMBO BOXES
        #========================================#
        cmbFrame = Frame(mFrame,bd = 1)
        
        #INPUT ADDRESSES
        lblAdd1 = Label(cmbFrame,text = "Address 1")
        lblAdd1.pack()
        self.cmbAdd1 = ttk.Combobox(cmbFrame,postcommand = self.populateComboBox)
        self.cmbAdd1.pack()
        
        lblAdd2 = Label(cmbFrame,text = "Address 2")
        lblAdd2.pack()
        self.cmbAdd2 = ttk.Combobox(cmbFrame,postcommand = self.populateComboBox)
        self.cmbAdd2.pack()
        
        lblAdd3 = Label(cmbFrame,text = "Address 3")
        lblAdd3.pack()
        self.cmbAdd3 = ttk.Combobox(cmbFrame,postcommand = self.populateComboBox)
        self.cmbAdd3.pack()
        
        lblAdd4 = Label(cmbFrame,text = "Address 4")
        lblAdd4.pack()
        self.cmbAdd4 = ttk.Combobox(cmbFrame,postcommand = self.populateComboBox)
        self.cmbAdd4.pack()
        
        lblAdd5 = Label(cmbFrame,text = "Address 5")
        lblAdd5.pack()
        self.cmbAdd5 = ttk.Combobox(cmbFrame,postcommand = self.populateComboBox)
        self.cmbAdd5.pack()
        
        lblAdd6 = Label(cmbFrame,text = "Address 6")
        lblAdd6.pack()
        self.cmbAdd6 = ttk.Combobox(cmbFrame,postcommand = self.populateComboBox)
        self.cmbAdd6.pack()
        
        lblAdd7 = Label(cmbFrame,text = "Address 7")
        lblAdd7.pack()
        self.cmbAdd7 = ttk.Combobox(cmbFrame,postcommand = self.populateComboBox)
        self.cmbAdd7.pack()
        
        lblAdd8 = Label(cmbFrame,text = "Address 8")
        lblAdd8.pack()
        self.cmbAdd8 = ttk.Combobox(cmbFrame,postcommand = self.populateComboBox)
        self.cmbAdd8.pack()
        
        cmbFrame.pack(pady=20)
        
        #Area
        areaFrame = Frame(rFrame,bd = 0)
        lblDDL = Label(areaFrame,text = "Double Dependent Locality")
        lblDDL.pack()
        self.cmbDDL = ttk.Combobox(areaFrame,postcommand = self.populateComboBox)
        self.cmbDDL.pack()

        lblDL = Label(areaFrame,text = "Dependent Locality")
        lblDL.pack()
        self.cmbDL = ttk.Combobox(areaFrame,postcommand = self.populateComboBox)
        self.cmbDL.pack()
        
        lblLoc = Label(areaFrame,text = "Locality")
        lblLoc.pack()
        self.cmbLoc = ttk.Combobox(areaFrame,postcommand = self.populateComboBox)
        self.cmbLoc.pack()
        
        lblSAA = Label(areaFrame,text = "Sub-Administrative Area")
        lblSAA.pack()
        self.cmbSAA = ttk.Combobox(areaFrame,postcommand = self.populateComboBox)
        self.cmbSAA.pack()

        lblAA = Label(areaFrame,text = "Administrative Area")
        lblAA.pack()
        self.cmbAA = ttk.Combobox(areaFrame,postcommand = self.populateComboBox)
        self.cmbAA.pack()

        lblSNA = Label(areaFrame,text = "Sub-National Area")
        lblSNA.pack()
        self.cmbSNA = ttk.Combobox(areaFrame,postcommand = self.populateComboBox)
        self.cmbSNA.pack()

        lblCN = Label(areaFrame,text = "Country")
        lblCN.pack()
        self.cmbCN = ttk.Combobox(areaFrame,postcommand = self.populateComboBox)
        self.cmbCN.pack()

        lblPC = Label(areaFrame,text = "Postal Code")
        lblPC.pack()
        self.cmbPC = ttk.Combobox(areaFrame,postcommand = self.populateComboBox)
        self.cmbPC.pack()
        
        areaFrame.pack(expand=1,padx = 30)
        
        lblBlank = Label(mFrame, width = 15, height = 5)
        lblBlank.pack()
        lblBlank1 = Label(mFrame)
        lblBlank1.pack()
        lblBlank2 = Label(rFrame)
        lblBlank2.pack()
        #Processing Frame
        
        btnProcess = Button(rFrame,text = "RUN",bd = 3, command = self.Process,width = 15, height = 5)
        btnProcess.pack()


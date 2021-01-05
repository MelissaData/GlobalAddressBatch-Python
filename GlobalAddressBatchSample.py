import GlobalAddressDesign  #Holds the design for GUI
import json
import csv
import os


from urllib.request import Request, urlopen  
from tkinter import *
from tkinter import filedialog, ttk, messagebox
print ("PYTHON 3")
    

    
#========================================#
#Global Address Batch GUI
#========================================#
class GlobalAddressBatchGUI(GlobalAddressDesign.GlobalAddress_Design):

    def __init__(self):
        GlobalAddressDesign.GlobalAddress_Design.__init__(self)
        self.checkCmd = IntVar()
        self.initUI()
        self.fileName = ''
        self.outputFile = ''
        self.options = ''
        self.headers = []
        self.writtenHeaders = False
                
    #========================================#
    #OpenFileDialog
    #========================================#
    def browse_button(self):
        # Get the delimiter and text qualifier for the file
        delims = [',' , '\t' , '|']
        quote= [ 'QUOTE_NONE', "QUOTE_ALL"]
        self.inputDelim = delims[self.cmbDelim.current()]
        self.inputQuotes = quote[self.cmbTextQualifier.current()]
        self.fileName = filedialog.askopenfilename()
        print(self.fileName)
        self.populateComboBox()
        self.lblFilePath['text'] = self.fileName

        #For Testing
        #AUTO MAPPING.  parameter input = index of combo box
        #self.cmbAdd1.current(5)
        #self.cmbAdd2.current(6)
        #self.cmbAdd3.current(7)
        #self.cmbLoc.current(8)
        #self.cmbAA.current(9)
        #self.cmbCN.current(10)
        #self.cmbPC.current(11)
    #========================================#
    #OutputFileDialog
    #========================================#
    def outputFile_button(self):
        output = filedialog.asksaveasfile()
        self.outputFile = output.name
        self.lblOutputFilePath['text'] = self.outputFile
        print (self.outputFile)
    
    #Add Headers to the Combo Box
    def populateComboBox(self):
        with open(self.fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.inputDelim,quoting = csv.QUOTE_ALL )
            header = next(csv_reader)
            count  =0
            for item in header:
                header[count] = item.strip()
                count+=1
                
            self.header = header
        #add blank
        header = [""] + header
        self.cmbAdd1['values'] = header
        self.cmbAdd2['values'] = header
        self.cmbAdd3['values'] = header
        self.cmbAdd4['values'] = header
        self.cmbAdd5['values'] = header
        self.cmbAdd6['values'] = header
        self.cmbAdd7['values'] = header
        self.cmbAdd8['values'] = header
        self.cmbDDL['values'] = header
        self.cmbDL['values'] = header
        self.cmbLoc['values'] = header
        self.cmbSAA['values'] = header
        self.cmbAA['values'] = header
        self.cmbSNA['values'] = header
        self.cmbCN['values'] = header
        self.cmbPC['values'] = header
        self.cmbLN['values'] = header


    #========================================#
    #Generate the Options
    #========================================# 
    def generateOptions(self):
        ''' Generates the option parameters for the JSON Batch'''
        inputOptions = []
        #DELIVERY LINES
        if self.cmbDeliveryLines.current() == 1:
            inputOptions.append("DeliveryLines:On")
        #LINE SEPARATOR
        inputOptions.append("LineSeparator:{0}".format(self.cmbLineSeparator.get()))
        delLines = "OutputScript:"
        #DELIVERY LINE
        if self.cmbDeliveryLines.current() == 1:
            inputOptions.append(delLines+"LATN")
        elif self.cmbDeliveryLines.current() ==2:
            inputOptions.append(delLines+"NATIVE")
        #OutputGeo
        if self.cmbOutputGeo.current() == 1:
            inputOptions.append("OutputGeo:Off")
        inputOptions.append("CountryOfOrigin:{0}".format(self.txtCountry.get()))
        #USExtras
        if self.cmbUSExtras.current() == 0:
            inputOptions.append("USExtras:ON")
        #Convert to string
        finalOptions = ''
        for option in inputOptions:
            finalOptions += option +','
        #print("FINAL OPTIONS: " ,finalOptions)
        if finalOptions[-1:] == ',':
            finalOptions = finalOptions[:-1]
        self.options = str(finalOptions)
        
    #========================================#
    #Generate Headers
    #========================================# 
    def generateHeadersDict(self):
        '''Get the column names for all of the mapped in fields'''
        inputDict = {}
        inputDict['AddressLine1'] = self.cmbAdd1.get()
        inputDict['AddressLine2'] = self.cmbAdd2.get()
        inputDict['AddressLine3'] = self.cmbAdd3.get()
        inputDict['AddressLine4'] = self.cmbAdd4.get()
        inputDict['AddressLine5'] = self.cmbAdd5.get()
        inputDict['AddressLine6'] = self.cmbAdd6.get()
        inputDict['AddressLine7'] = self.cmbAdd7.get()
        inputDict['AddressLine8'] = self.cmbAdd8.get()
        inputDict['DependentLocality'] = self.cmbDL.get()
        inputDict['DoubleDependentLocality'] = self.cmbDDL.get()
        inputDict['Locality'] = self.cmbLoc.get()
        inputDict['SubAdministrativeArea'] = self.cmbSAA.get()
        inputDict['SubNationalArea'] = self.cmbSNA.get()
        inputDict['PostalCode'] = self.cmbPC.get()
        inputDict['Country'] = self.cmbCN.get()
        inputDict['Last'] = self.cmbLN.get()
        delList = []
        #search for empty mappings and delete them from the dictionary
        for key, value in inputDict.items():
            if len(value) <= 0:
                delList.append(key)
        for item in delList:
            inputDict.pop(item)
        return inputDict
    
    #========================================#
    #Button even for Run
    #========================================# 
    def Process(self):
        #VARIABLES
        Records = []          
        counter = 0
        totalCount = 0
        
        '''Start Batch Processing'''
        #Check to see if License is inputted and Country is mapped
        licenseChecker = True
        countryChecker = True
        checker = True
        message = ''
        if self.txtLicense.get().strip() == "ENTER_LICENSE":
            licenseChecker = False
            checker = licenseChecker
            message += "Please Enter a License String\n"
        if len(self.cmbCN.get()) < 1:
            countryChecker = False
            checker = countryChecker
            message += "Please Map in Country\n"
        if not checker:
            messagebox.showinfo("WARNING",message)
        #PASS : License is inputted and country is mapped
        else:   
            #CHECK whether the minimum parameters are set.
            f = self.lblOutputFilePath.cget("text")
            #If no output file is specified
            if  f == "":       
                 listFileName = os.path.splitext(self.fileName)
                 newOutputFile = listFileName[0]+"_Output"+listFileName[1]
                 self.outputFile = newOutputFile
                 print(newOutputFile)
            #Generate the options
            self.generateOptions()
            #Generate the dictionary "skeleton"/"frame" to be used for the JSON Batch
            headerDict = self.generateHeadersDict()
            inputParamList = []
            for key in headerDict:
                inputParamList.append(key)
            #This will hold the "Records" in the JSON batch
                
            #==========================================#
            #ITERATE THROUGH CSV FILE HERE!
            #==========================================#
            
            with open(self.fileName,'r', encoding = "utf-8" ) as f:
                reader = csv.DictReader(f,delimiter=self.inputDelim,quoting = csv.QUOTE_ALL)
                #iterate through the CSV file
                for rows in reader:
                    inputRecord = {}
                    #If the row Counter hits 100 records send a request and write row
					#IF Multithreaded, we can add records to a queue here
                    if counter >= 100:
                        results = self.sendBatchRequest(Records)
                        self.writeRow(results)
                        counter = 0
                        Records = []
                        print("Processed {0} rows".format(totalCount))
                    #Creating one record in JSON format here
                    for header in inputParamList:
                        inputRecord[header] = rows[ headerDict[header] ]
                    #Append inputRecord to Records Array
                    Records.append(inputRecord)
                    counter+=1
                    totalCount+=1
                #If there are any leftover records after batch processing
                if counter <99 and counter >0:
                    results = self.sendBatchRequest(Records)
                    self.writeRow(results)   
            print("FINISHED")
        
    #========================================#
    #CSV Writer
    #========================================#      
    def writeRow(self, results):
        '''Writes to CSV file using DictWriter'''
        outputCsv = self.outputFile
        with open(outputCsv,'a', encoding = "utf-8",newline='') as w:      #Write csv file
            responseData = results['Records']
            #Get the headers from the response
            if len(responseData) > 0:
                keys = responseData[0].keys()
                
            #Create a new DictWriter and write rows
            writer = csv.DictWriter(w,delimiter=self.inputDelim,quoting = csv.QUOTE_ALL, fieldnames = keys)

            #make sure we only add headers once
            if not self.writtenHeaders:
                writer.writeheader()
                self.writtenHeaders = True
            for row in responseData:
                writer.writerow(row)

                
    #========================================#
    #BATCH REQUEST
    #========================================#      
    def sendBatchRequest(self, inputRecords):
        '''Batch Request with Json'''
        URL = r'http://address.melissadata.net/v3/WEB/GlobalAddress/doglobaladdress'
        jsonBatchDict = {"TransmissionReference" : "GlobalAddressBatch",
                     "CustomerID" : self.txtLicense.get().rstrip(),
                     "Options" : self.options,
                     "Records" :[]}
        
        jsonBatchDict["Records"] = inputRecords
##        headers = {'Accept': 'application/json'}
        try:
            r = Request(url = URL, data= json.dumps(jsonBatchDict).encode('utf-8'))
            r.add_header('Accept','application/json')
            content = urlopen(r)
            print("Status Code : ", content.getcode())
            json_data= json.loads(content.read())
        except Exception as e:
            print("FAILED!\n{}".format(str(e)))
        return json_data
        
#========================================#
#Main
#========================================# 
def main():
    root = Tk()
    root.rowconfigure(0,weight=1)
    root.columnconfigure(3,weight=1)
    root.style = ttk.Style()
    root.style.theme_use("alt")
    root.geometry("750x750")
    app = GlobalAddressBatchGUI()
    root.mainloop()

if __name__ == '__main__':
    main()

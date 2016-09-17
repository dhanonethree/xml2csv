import xml.etree.ElementTree as ET
import csv

tree = ET.parse('D:\\Danny\\PublicSplit110\\20160810_Public03.xml')
root = tree.getroot()

with open('D:\\Danny\\pub_final31.csv', 'w',newline='') as f:
    writer = csv.writer(f)
    row = ["ABR_recordLastUpdatedDate","ABR_replaced","ABN_status","ABN_ABNStatusFromDate","ABN","EntityTypeInd","EntityTypeText","MainEntity_NonIndividualName","MainEntity_NonIndividualNameText","LegalEntity_IndividualName_Type","LegalEntity_NameTitle","LegalEntity_GivenName","LegalEntity_FamilyName","ASICNumberType","ASICNumber","GST_status","GSTStatusFromDate","DGRStatusFromDate","DGR_NonIndividualName_Type","DGR_NonIndividualNameText","BusinessAddress_State","BusinessAddress_Postcode","OtherEntity_NonIndividualName_Type","OtherEntity_NonIndividualNameText"]
    writer.writerow(row)
    
    #Gname = ""
    for ABR in root.iter('ABR'):
               row = []
          # row.append(ABR.attrib['recordLastUpdatedDate'])
              
               row.append(ABR.get('recordLastUpdatedDate'))#ABR record last update
               row.append(ABR.get('replaced'))# ABR replaced
               
               flag = 1
               for ABN in ABR.iter('ABN'):
                   flag = 0
                   row.append(ABN.get('status'))#ABN status
                   row.append(ABN.get('ABNStatusFromDate'))#ABNstatusfromdate
                   row.append(ABN.text)#ABN value
               if(flag):       
                   row.append("NA")
                   row.append("NA")
                   row.append("NA")
               
               flag = 1    
               for  EType in ABR.iter('EntityTypeInd'):
                   flag = 0
                   row.append(EType.text)#EntiTypeInd
               if(flag):       
                   row.append("NA")
               flag = 1    
               for  EType in ABR.iter('EntityTypeText'):
                   flag = 0
                   row.append(EType.text)#EntityTypeText
               if(flag):       
                   row.append("NA")
               
               flag = 1
               for MainEntity in ABR.iter('MainEntity'):
                   flag = 1
                   for NonIndividualName in MainEntity.iter('NonIndividualName'): 
                       flag = 0
                       row.append(NonIndividualName.get('type'))
                   if(flag):       
                       row.append("NA")
                   for NonIndividualNameText in MainEntity.iter('NonIndividualNameText'):
                       flag = 0
                       row.append(NonIndividualNameText.text)
                   if(flag):       
                       row.append("NA")
               if(flag):       
                   row.append("NA")       
                   row.append("NA")
                       
               
               flag = 1
               for LegalEntity in ABR.iter('IndividualName'):
                   flag = 0
                   row.append(LegalEntity.get('type'))
               if(flag):       
                   row.append("NA")
               flag = 1    
               for NameTitle in ABR.iter('NameTitle'):#LegalEntity Name Title
                   flag = 0
                   row.append(NameTitle.text)
               if(flag):       
                   row.append("NA")
               flag = 1    
               Gname = str()
               for GivenName in ABR.iter('GivenName'):#LegalEntity GivenName
                   flag = 0
                   Gname = GivenName.text+" "+Gname
               if(flag==0):                    
                   row.append(Gname)
               if(flag):       
                   row.append("NA")
               flag = 1    
               for FamilyName in ABR.iter('FamilyName'):#LegalEntiy FamilyName
                   flag = 0
                   row.append(FamilyName.text)
               if(flag):       
                   row.append("NA")    
               
               flag = 1
               for ASICNumber in ABR.iter('ASICNumber'):
                   flag = 0
                   row.append(ASICNumber.get('ASICNumberType'))#ASICNumberType
               if(flag):       
                   row.append("NA")
               flag = 1
               for ASICNumber in ABR.iter('ASICNumber'):
                   flag = 0
                   row.append(ASICNumber.text)   
               if(flag):       
                   row.append("NA")    
               
               flag = 1
               for GST in ABR.iter('GST'):
                   flag = 0
                   row.append(GST.get('status'))
               if(flag):       
                   row.append("NA")
               flag = 1    
               for GST in ABR.iter('GST'):
                   flag = 0
                   row.append(GST.get('GSTStatusFromDate'))
               if(flag):       
                   row.append("NA")    
               
               flag = 1
               for DGR in ABR.iter('DGR'):
                   flag = 0
                   row.append(DGR.get('DGRStatusFromDate')) 
               if(flag):       
                   row.append("NA")
               if(flag):       
                   row.append("NA")
               if(flag):       
                   row.append("NA")    
               
               flag = 1    
               for DGR in ABR.iter('DGR'):
                   flag = 1
                   for NonIndividualName in DGR.iter('NonIndividualName'): 
                       flag = 0
                       row.append(NonIndividualName.get('type'))
                   if(flag):       
                       row.append("NA")
                   flag = 1   
                   for NonIndividualNameText in DGR.iter('NonIndividualNameText'): 
                       flag = 0
                       row.append(NonIndividualNameText.text)    
                   if(flag):       
                       row.append("NA")
                   
                       
               
                    
               
               flag = 1
               for BusinessAddress in ABR.iter('State'):
                   flag = 0
                   row.append(BusinessAddress.text)
               if(flag):       
                   row.append("NA")
               flag = 1    
               for BusinessAddress in ABR.iter('Postcode'):
                   flag = 0
                   row.append(BusinessAddress.text)
               if(flag):       
                   row.append("NA")
                   
               flag = 1
               for OtherEntity in ABR.iter('OtherEntity'):
                   flag = 1
                   for NonIndividualName in OtherEntity.iter('NonIndividualName'):
                       flag = 0
                       #NINTypes += NIN.text + "," NonIndividualName.get('type')
                       row.append(NonIndividualName.get('type'))
                   if(flag):       
                       row.append("NA")
                   flag = 1
                   for NonIndividualName in OtherEntity.iter('NonIndividualName'):
                       for NonIndividualNameText in NonIndividualName.iter('NonIndividualNameText'):
                           flag = 0
                           row.append(NonIndividualNameText.text)
                       if(flag):       
                           row.append("NA")
               if(flag):       
                   row.append("NA")
               if(flag):       
                   row.append("NA") 
                   
               writer.writerow(row)

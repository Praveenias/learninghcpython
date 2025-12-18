import pandas as pd
import math
import os
import glob
#folderpath="E:\iLensys\Malvern\input1"
#directory_path=''

#Read all file from input directory
def get_files(directory_path):
    df_list = []
    #directory_path = input('Enter directory path: ')
    filenames = glob.glob(directory_path + '/*.xl*')
    number_of_files = len(filenames)
    for f in filenames:
        data = pd.read_excel(f,header=None)
        df_list.append(data)
    return df_list,directory_path

#df_list,directory_path=get_files()
def filenameextract(directory_path):
    filenames=[]
    for f in glob.glob(directory_path+"/*.xl*"):
        filenames.append((os.path.basename(f).split('/')[-1]).split('.')[0])
    return filenames
#filenames=filenameextract()


#Skip beginning lines and start reading RAW table
def dfcreate(df):
    Manuflist=['Manufacturer','MANUFACTURER','manufacturer','Manufacturers.Mfr. Name','mfr','Mfr Name','mfr.','MFR','Mfr.','MFR.','manufacture','Manufacture','MANUFACTUR','manf','MANF','MANF.','manf.','Manf','Manf.','Manufacturer Name']
    contains_value = df.isin(Manuflist).any(axis=1)
    index_of_true = contains_value[contains_value].index
    newlist=[]
    dfcol=df.iloc[index_of_true]
    dfcol=dfcol.iloc[0]
    for val in dfcol:
        newlist.append(val)
    newlist=[x for x in newlist if x == x]
    flag=0
    dfupdated=pd.DataFrame()
    for (index, row) in df.iterrows():
        if(~(row.isin(Manuflist).any())and flag==0):#row[0]!=newlist[0]and flag==0):
                #print(row[0])
           continue
        else:
           flag=1
        dfupdated=pd.concat([dfupdated,pd.DataFrame([row])],ignore_index = True)

        #dfupdated=pd.concat([dfupdated,pd.DataFrame([row])],ignore_index = True)
    #print(dfupdated)
    return dfupdated,newlist

def dfallfiles(filenames,df_list):
    dfupdated=pd.DataFrame()
    #for i in range(len(filenames)):
    df,elem=dfcreate(df_list)
    columnheading=df.loc[0]
    df=df.set_axis(labels=columnheading,axis=1) #make row 0 as heading
    #print(df.columns)
    df.drop(index=df.index[0], axis=0,inplace=True) #drop row0
    df['FILENAME'] = filenames #store filename in df
    df.columns=df.columns.str.upper()
    elem=list(map(str.upper,elem))
    Manuflist=['Manufacturers.Mfr. Name','mfr','Mfr Name','mfr.','MFR','Mfr.','MFR.','manufactur','Manufactur','MANUFACTUR','manf','MANF','MANF.','manf.','Manf','Manf.','Manufacturer Name','MANUFACTURER','Manufacturer','manufacturer']
    for item in Manuflist:
        if item in elem:
            df = df.rename(columns={item : 'MANUFACTURER'})
    ManPNlist=['MANUFACTURER PN','MAN. PART NO.','PARTNUMBER','MPN','PART NUMBER','Part No.','PART NO.','MANPARTNUM','MANUFACTURERS.MFR. PART NUMBER','MANUFACTURER PART NO.','\'MANUFACTURE P/N','MANUFACTURER PART NUMBER','MANUFACTURER ITEM NUMBER','MFR PART NUMBER','MANUFACTURER\'S PART NUMBER']
    for item in ManPNlist:
        if item in elem:
            df = df.rename(columns={item : 'MANFPN'})
    Qnlist=['QUANTITY','QTY PER','\'QTY.','QTY.','ESULT QTY/PN']
    for item in Qnlist:
        if item in elem:
            df = df.rename(columns={item : 'QTY'})
    df.columns=df.columns.str.replace(' ', '_')
    #print(df.columns)
    df = df.dropna(how='all',subset=['MANUFACTURER','MANFPN']) #if man is empty drop the row
    for k in range(len(Manuflist)):
        i=df[((df.MANUFACTURER == Manuflist[k]))].index #drop in between row with column heading
        df=df.drop(i)
    materiallist=['See Material Spec.','SEE MATERIAL SPEC.','See Material Spec','SEE MATERIAL SPEC','see material spec','see material spec.']
    for k in range(len(materiallist)):
        j=df[((df.MANFPN == materiallist[k]))].index #drop in between row with column heading
        df=df.drop(j)
    df=df[['MANUFACTURER','DESCRIPTION','MANFPN','QTY','FILENAME']]
    dfupdated=pd.concat([dfupdated,df],ignore_index = True) #append from all files
    return dfupdated
#dfallfiles()
#handle rows with merged values
def mergedrows(dfupdated):
    for i in range(0, len(dfupdated)):
        if(pd.isna(dfupdated.DESCRIPTION.values[i])):
            dfupdated.DESCRIPTION.values[i]=dfupdated.DESCRIPTION.values[i-1]
            dfupdated.QTY.values[i]=dfupdated.QTY.values[i-1]
            if(pd.isna(dfupdated.MANUFACTURER.values[i])):
                dfupdated.MANUFACTURER.values[i]=dfupdated.MANUFACTURER.values[i-1]
    return dfupdated
#mergedrows()
#Load in ATOM Template
def atomconvert(dfupdated):
    part=1
    dfnew = pd.DataFrame(columns = ['Customer Part number', 'Part Revision', 'Level','Customer part number description','Manufacturer name','Manufacturer part number','Quantity','Proactive Analysis','Total Inventory','EAU','Critical Component','Supplier Internal Partnumber','Supplier Partnumber','Supplier Manufacturer','Supplier Lead Time','Supplier Stock','Supplier Monthly Usage','Supplier Cover Months','Supplier Cover Date','Inventory Date','Check Date life cycle','Check Date Stock','LTB Possibility','OPO','Remark'])
    dfupdated['MATCH']= dfupdated['FILENAME'].shift(1)==dfupdated['FILENAME']
    duplicatepartno={}
    for (index, row) in dfupdated.iterrows():
        Customerpartnumberdescription=row['DESCRIPTION']
        partno=row['FILENAME']
        if row['MATCH']==False:
            duplicatepartno={}
            part=1
        if Customerpartnumberdescription in duplicatepartno.keys(): #duplicate key dont cretae partno
            CustomerPartnumber=duplicatepartno[Customerpartnumberdescription]
        else:
            CustomerPartnumber=partno+"_Part-"+str(part)
            part+=1
        duplicatepartno[Customerpartnumberdescription]=CustomerPartnumber
        Quantity=row['QTY']
        Manufacturername = row['MANUFACTURER']
        Manufacturerpartnumber = row['MANFPN']
        if(pd.isna(Manufacturername) or pd.isna(Manufacturerpartnumber)):
            continue
        dfnew=pd.concat([dfnew,pd.DataFrame([{'Customer Part number':str(CustomerPartnumber).strip(),'Customer part number description':Customerpartnumberdescription.strip(),'Manufacturer name':Manufacturername.strip(),'Manufacturer part number':str(Manufacturerpartnumber).strip(),'Quantity':str(Quantity).strip(),}])],ignore_index = True)
    return dfnew

#atomconvert()
def formatting(dfnew):
    appended_df=pd.DataFrame()
    dfnew.T.reset_index().T.reset_index(drop=True)
    df1=pd.DataFrame({'Customer Part number':'Mandatory: Part number as maintained by the customer','Part Revision':'Optional: Customer part number revision. Default: Null','Level':'Optional: For multilevel BOM, it represents level. Default: 1','Customer part number description':'Optional : Description as given by customer','Manufacturer name':'Mandatory: If normalized manufacturer name matches the normalized name in manufacturer table then Match else no match','Manufacturer part number':'Mandatory: If normalized  partnumber matches the number in m master component then match else no match','Quantity':'Mandatory: Quantity Per PCBA. Allowed values: Positive integer ( 0 or more ). Empty values not allowed','Proactive Analysis':'Mandatory: Whether to do Risk analysis or not.   Allowed Values: Yes, No. Empty values not allowed','CM or Internal cost tool UOM':'Optional: Units of Measure. Allowed values : Restricted to Each alone','CM or Internal cost tool Currency Type':'Optional : CM/ Internal Cost tool Currency Type. Allowed values : Restricted to USD alone','CM or Internal cost tool Minimum Order Quantity':'Optional','CM or Internal cost tool Average Price':'Optional :  CM/ Internal Cost tool Average Price - - Need to be floating point number. Do not use Rs, $ , Euro or other currency symbols. Default: Null','CM or Internal cost tool Current Half Yearly Price':'Optional :  CM/ Internal Cost tool Current Half yearly price - Need to be floating point number. Do not use Rs, $ , Euro or other currency symbols. Default: Null','CM or Internal cost tool Previous Half Yearly Price':'Optional :  CM/ Internal Cost tool Previous Half Yealy Price - Need to be floating point number. Do not use Rs, $ , Euro or other currency symbols. Default: Null','Cost Data Source':'Optional','CM or Internal cost tool Check Date Current HF Price':'Optional - date column  (dd-mmm-yy) format','CM or Internal cost tool Check Date Previous HF Price':'Optional - date column  (dd-mmm-yy) format','Total Inventory':'Optional: Integer number. It is also referred as LifetimePCS. Note: Currently not used. Do not use this column.  This column will be deleted in future','EAU':'Optional: Integer number. Expected Annual Utilization. It is also referred as DemandPCS. Note: Currently not used. Do not use this column.  This column will be deleted in future','Critical Component':'Optional:  Allowed Value: Yes or No.  Check: This may be based on analysis','Supplier Internal Partnumber':'Optional: String','Supplier Partnumber':'Optional: String','Supplier Manufacturer':'Optional: String','Supplier Lead Time':'Optional: LeadTime data provided by the Supplier in no of weeks. Default: Null','Supplier Stock':'Optional: Stock with the supplier. Default: Zero','Supplier Monthly Usage':'Optional: Monthly Usage at Supplier','Supplier Cover Months':'Optional: No.of months Cover available provided by the Supplier','Supplier Cover Date':'Optional:Date provided by the Supplier             (dd-mmm-yy) format','Check Date Supplier':'Optional: date column (dd-mmm-yy) format. When the Data received from CM ( old name: Inventory Date)','Check Date life cycle':'Optional: date column   (dd-mmm-yy) format','Check Date Stock':'Optional: date column  (dd-mmm-yy) format','LTB Possibility':'Optional: Boolean component can become LTB \? Default: False','OPO':'Optional : Open purchase Order. Number','Remark':'Optional: User to maintain any notes'}, index =[1])
    df2 = pd.concat([df1, dfnew]).reset_index(drop = True)
    df2=df2.T.reset_index().T.reset_index(drop=True)
    df3 = df2.reindex(index = [1, 0])
    appended_df=pd.concat([df3,df2],ignore_index=True)
    appended_df=appended_df.drop([2,3])
    appended_df = appended_df.drop_duplicates()
    return appended_df

#def outwrite(out,appended_df):
 #   appended_df.to_excel(out+"/output.xlsx",index=False,header=False)
  #  del appended_df

def main1(input,output):
    df_list,directory_path=get_files(input)
    filenames=filenameextract(directory_path)
    for i in range(len(filenames)):
        dfupdated=dfallfiles(filenames[i],df_list[i])
        dfupdated=mergedrows(dfupdated)
        dfnew=atomconvert(dfupdated)
        appended_df=formatting(dfnew)
        appended_df.to_excel(output+"/"+filenames[i]+"_"+"Scrubbed_"+"BOM.xlsx",sheet_name='Data',index=False,header=False)
        del appended_df

import pandas as pd
import math
import numpy as np
import re
import os
import glob
import math
import argparse


#Read all file from input directory
def get_files(directory_path):
    df_list = []
    #directory_path = input('Enter input directory path: ')
    filenames = glob.glob(directory_path + '/*.xl*')
    #print(filenames)
    #filenames.append(glob.glob(directory_path + ))
    number_of_files = len(filenames)
    for f in filenames:
        data = pd.read_excel(f,header=None)
        df_list.append(data)
    return df_list,directory_path

def get_files1(directory_path):
    df_list = []
    #directory_path = input('Enter output directory path: ')
    filenames = glob.glob(directory_path + '/*.xl*')
    number_of_files = len(filenames)
    for f in filenames:
        data = pd.read_excel(f)
        df_list.append(data)
    return df_list,directory_path


#extract filenames
def filenameextract(directory_path):
    filenames=[]
    for f in glob.glob(directory_path+"/*.xl*"):
        filenames.append((os.path.basename(f).split('/')[-1]).split('.')[0])
    return filenames

#Skip beginning lines and start reading RAW table #called from dfprepare
def dfcreate(df):
    Manuflist=['Manufacturer','Manufacture','Manufacturer_1','Manufacturer 1','MANUFACTURER','manufacturer','Manufacturers.Mfr. Name','mfr','Mfr Name','mfr.','MFR','Mfr.','MFR.','manufactur','Manufactur','MANUFACTUR','manf','MANF','MANF.','Mfr Name','manf.','Manf','Manf.','Manufacturer Name','Qual.Mafr.','AML1','AVL DESCRIPTION']
    #print(df)
    contains_value = df.isin(Manuflist).any(axis=1)
    index_of_true = contains_value[contains_value].index
    newlist=[]
    dfcol=df.iloc[index_of_true]
    dfcol=dfcol.iloc[0]
    for val in dfcol:
        newlist.append(val)
    #print(newlist)
    newlist=[x for x in newlist if x == x]
    flag=0
    dfupdated=pd.DataFrame()
    #append items with keyword manufacturer
    for (index, row) in df.iterrows():
        if(~(row.isin(Manuflist).any())and flag==0):
            continue
        else:
            flag=1
            #print(row)
        dfupdated=pd.concat([dfupdated,pd.DataFrame([row])],ignore_index = True)
        if dfupdated.empty:
            for (index, row) in df.iterrows():
                if(~(row.isin(Manuflist).any())and flag1==0):
                    continue
                else:
                    flag1=1
                dfupdated=pd.concat([dfupdated,pd.DataFrame([row])],ignore_index = True)
    return dfupdated, newlist

def split1(df,newlist):
        splitdf=pd.DataFrame()
        #print(df.columns)
        for index,row in df.iterrows():
                Cpndesc=row['DESCRIPTION']
                Quantity=''
                value=row['AVL DESCRIPTION']
                if(not pd.isna(value)):
                    if "*" in value:
                        Cpn=row['CPN']
                        result = value.split("*")
                        #print(result)
                        second_part_without_bracket = result[0]
                        manuf=result[1]
                        mpn= second_part_without_bracket
                        splitdf=pd.concat([splitdf,pd.DataFrame([{'CPN':Cpn,'DESCRIPTION':Cpndesc,'MANUFACTURER':manuf,'MPN':mpn,'QTY':Quantity}])],ignore_index = True)               
                #print(splitdf)
        return splitdf

def split(df,newlist):
        part=1
        colsplit=countmanuf1(newlist)
        colsplit=[x.upper() for x in colsplit]
        splitdf=pd.DataFrame()
        for index,row in df.iterrows():
            for i in colsplit:
                Cpndesc=row['DESCRIPTION']
                Quantity=row['QTY']
                #colname = row[i]
                value=row[i]
                        #print(value)
                if(not pd.isna(value)):
                    if "[" in value:
                        Cpn=row['LEVEL-1']
                        result = value.split("[")
                        #print(result)
                        second_part = result[1].split("]")
                        second_part_without_bracket = second_part[0]
                        manuf=result[0]
                        mpn= second_part_without_bracket
                        splitdf=pd.concat([splitdf,pd.DataFrame([{'CPN':Cpn,'DESCRIPTION':Cpndesc,'MANUFACTURER':manuf,'MPN':mpn,'QTY':Quantity}])],ignore_index = True)               
                    elif "*" in value:
                        Cpn=row['CPN']
                        result = value.split("*")
                        #print(result)
                        second_part_without_bracket = result[1]
                        manuf=result[0]
                        mpn= second_part_without_bracket
                        splitdf=pd.concat([splitdf,pd.DataFrame([{'CPN':Cpn,'DESCRIPTION':Cpndesc,'MANUFACTURER':manuf,'MPN':mpn,'QTY':Quantity}])],ignore_index = True)               
                #print(splitdf)
        return splitdf

def dfprepare(df,filename):
    df,newlist=dfcreate(df)
    columnheading=df.loc[0]
    values_to_check=['Qual.Mafr.','AML1']
    values_to_check1=['AVL DESCRIPTION']
    df=df.set_axis(axis=1,labels=columnheading) #make row 0 as heading 
    df.drop(index=df.index[0], axis=0,inplace=True) #drop row0
    df.columns=df.columns.str.upper()
    df,newlist=rename(df,newlist)
    df.dropna(how='all', inplace=True)
    #print(df)
    if(columnheading.isin(values_to_check).any()):
        #print("Entery")
        df=split(df,newlist)
        df=dfnew1(df,filename)
    #df=mergedrows(df)
    elif(columnheading.isin(values_to_check1).any()):
        #print("Entery")
        df=split1(df,newlist)
        df=dfnew1(df,filename)
    else:
        count,manulist,partlist=countmanuf(newlist)
        #print(newlist)
        manulist=[x.upper() for x in manulist]
        partlist=[x.upper() for x in partlist]
        df=mergedrows(df)
        df=dfnew(df,manulist,partlist,filename)
        #df=mergedrows(df)
    return df

#called from dfprepare
def rename(df,elem):
    #elem=elem.upper()
    flag=0
    elem=[x.upper() for x in elem]
    Vendpn=['ITEM','VENDPARTNUM','PART NO.','PN','PART NO','ITEM NUMBER','MATERIAL NUMBER','NUMBER','COMPONENTNUMBER']
    Desc=['DESCRIPTION 1','COMMENT','ITEM NAME','MATERIAL DESCRIPTION','SHORT DESCRIPTION']
    for item in Vendpn:
        if item in elem:
            df = df.rename(columns={item : 'CPN'})
            elem.remove(item)
            flag=1
    if flag==0:
        df['CPN']=np.NaN
    for item in Desc:
        if item in elem:
            df=df.rename(columns={item :'DESCRIPTION'})
    Qnlist=['QUANTITY','QTY PER','\'QTY.','QTY.','ESULT QTY/PN','RESULT QTY/PN']
    for item in Qnlist:
        if item in elem:
            df = df.rename(columns={item : 'QTY'})
    return df,elem

#handle rows with merged values
def mergedrows(dfupdated):
    for i in range(0, len(dfupdated)):
            if(pd.isna(dfupdated.DESCRIPTION.values[i])):
                dfupdated.DESCRIPTION.values[i]=dfupdated.DESCRIPTION.values[i-1]
                #dfupdated.COMP_ID.values[i]=dfupdated.COMP_ID.values[i-1]
                #dfupdated.REF.values[i]=dfupdated.REF.values[i-1]
                dfupdated.CPN.values[i]=dfupdated.CPN.values[i-1]
                dfupdated.QTY.values[i]=dfupdated.QTY.values[i-1]
    return dfupdated            

#called from dfprepare
def countmanuf1(val):
    manuflist=[]
    manuword=re.compile('(AML[0-9]*)|(QUAL.MAFR.[0-9]*)')
    # Count the number of occurrences of the word in the header
    for string in val:
        if manuword.search(string):
            manuflist.append(string)
    return manuflist

#called from dfprepare
def countmanuf(val):
    count=0
    manuflist,partlist=[],[]
    manuword=re.compile('(MANUFACTURE)|(MFR NAME)')
    partword=re.compile('(\'MANUFACTURE P/N)|(MANUFACTURE P/N)|(MFR PART NUMBER)|(MANPARTNUM)|(MPN)|(MANUFACTURER PART NO.)|(MANUFACTURER ITEM NUMBER)|(MANUFACTURER PART NUMBER)|(MANUFACTURERS.MFR. PART NUMBER)|(PART[ ]*[NO.](UMBER)*)')
    # Count the number of occurrences of the word in the header
    for string in val:
        #print(string)
        if manuword.search(string):
            manuflist.append(string)
                #continue
            if partword.search(string):
                part=partword.search(string).group()
                if part in manuflist:
                    manuflist.remove(part)
            #print(manuflist)
            #count+=1
        #print(partword.search(string))
        if partword.search(string):
            partlist.append(string)
            #print(partlist)
    #count = len(re.findall(word, val, re.IGNORECASE))
    return count,manuflist,partlist

#called from dfprepare
def dfnew1(df,filename):
    dfnew1 = pd.DataFrame(columns = ['Customer Part number', 'Part Revision', 'Level','Customer part number description','Manufacturer name','Manufacturer part number','Quantity','Proactive Analysis','Critical Component'])
    for index,row in df.iterrows():
        Cpn=row['CPN']
        Cpndesc=row['DESCRIPTION']
        Quantity=row['QTY']
        if '.' in str(Quantity):
             Quantity=math.ceil(row['QTY'])
        Manufacturername = row['MANUFACTURER']
        Manufacturerpartnumber = row['MPN']
        #Level=row['LEVEL']
        dfnew1=pd.concat([dfnew1,pd.DataFrame([{'Customer Part number':Cpn,'Customer part number description':Cpndesc,'Manufacturer name':Manufacturername,'Manufacturer part number':Manufacturerpartnumber,'Quantity':Quantity}])],ignore_index = True)
            #print(dfnew1)
    return dfnew1 

#called from dfprepare
def dfnew(df,manulist,partlist,filename):
    dfnew1 = pd.DataFrame(columns = ['Customer Part number', 'Part Revision', 'Level','Customer part number description','Manufacturer name','Manufacturer part number','Quantity','Proactive Analysis','Critical Component'])
    manulist.sort(key=lambda k: k.replace(' ', ''))
    partlist.sort(key=lambda k: k.replace(' ', ''))
    #print(manulist)
    #print(partlist)
    part=1
    duplicatepartno={}
    for index,row in df.iterrows():
        Cpn=row['CPN']
        Cpndesc=row['DESCRIPTION']
        #if(pd.isna(Cpndesc)):
         #   df = df.drop(df[pd.isna(df['DESCRIPTION'])].index)
        if(pd.isna(Cpn)):
                #print(Cpn)
                if Cpndesc in duplicatepartno.keys(): #duplicate key dont cretae partno
                    Cpn=duplicatepartno[Cpndesc]
                else:
                    Cpn=filename+"_Part-"+str(part)
                    part+=1
                duplicatepartno[Cpndesc]=Cpn
        Quantity=row['QTY']
        if '.' in str(Quantity):
            Quantity=math.ceil(row['QTY'])
        #Level=row['LEVEL']
        for item in range(len(manulist)):
            index=item
            Manufacturername = row[manulist[index]]
            Manufacturerpartnumber = row[partlist[index]]
            Cpndesc=row['DESCRIPTION']
            #print(Manufacturername)
            if(index==0 and pd.isna(Manufacturername) and pd.isna(Manufacturerpartnumber)):
                Manufacturername = 'Unconfirmed'
                Manufacturerpartnumber = 'Unconfirmed'
            elif(pd.isna(Cpndesc)):
                continue
            elif(Manufacturername == 'diverse'):
                #print(Manufacturername)
                continue
            elif(index==0 and pd.isna(Manufacturername)):
                Manufacturername = 'Unconfirmed'
            elif(index==0 and pd.isna(Manufacturerpartnumber)):
                Manufacturerpartnumber='Unconfirmed'
            elif(Manufacturername == 'diverse'):
                #print(Manufacturername)
                continue
            elif(pd.isna(Manufacturername)):
                continue
            #dfupdated=pd.concat([dfupdated,pd.DataFrame([row])],ignore_index = True)
            dfnew1=pd.concat([dfnew1,pd.DataFrame([{'Customer Part number':Cpn,'Customer part number description':Cpndesc,'Manufacturer name':Manufacturername,'Manufacturer part number':Manufacturerpartnumber,'Quantity':Quantity}])],ignore_index = True)
            #print(dfnew1)
    return dfnew1 

def formatting(dfnew):
    appended_df=pd.DataFrame()
    dfnew.T.reset_index().T.reset_index(drop=True)
    df1=pd.DataFrame({'Customer Part number':'Mandatory: Part number as maintained by the customer','Part Revision':'Optional: Customer part number revision. Default: Null','Level':'Optional: For multilevel BOM, it represents level. Default: 1','Customer part number description':'Optional : Description as given by customer','Manufacturer name':'Mandatory: If normalized manufacturer name matches the normalized name in manufacturer table then Match else no match','Manufacturer part number':'Mandatory: If normalized  partnumber matches the number in m master component then match else no match','Quantity':'Mandatory:  Quantity per PCBA. Allowed values:  Positive integer ( 0 or more ).  Empty values not allowed\'','Proactive Analysis':'Mandatory:  Whether to do Risk analysis or not.   Allowed Values: Yes, No. Empty values not allowed','Total Inventory':'Optional: Integer number. It is also referred as LifetimePCS.','EAU':'Optional: Integer number. Expected Annual Utilization. It is also referred as DemandPCS.','Critical Component':'Optional:  Allowed Value: Yes or No.  Check: This may be based on analysis','Supplier Internal Partnumber':'Optional: String','Supplier Partnumber':'Optional: String','Supplier Manufacturer':'Optional: String','Supplier Lead Time':'Optional: LeadTime data provided by the Supplier in no of weeks. Default: Null','Supplier Stock':'Optional: Stock with the supplier. Default: Zero','Supplier Monthly Usage':'Optional: Monthly Usage at Supplier','Supplier Cover Months':'Optional: No.of months Cover available provided by the Supplier','Supplier Cover Date':'Optional:Date provided by the Supplier             (dd-mmm-yy) format','Check Date Supplier':'Optional: date column (dd-mmm-yy) format. When the Data received from CM ( old name: Inventory Date)','Check Date life cycle':'Optional: date column   (dd-mmm-yy) format','Check Date Stock':'Optional: date column  (dd-mmm-yy) format','LTB Possibility':'Optional: Boolean component can become LTB \? Default: False','OPO':'Optional : Open purchase Order. Number','Remark':'Optional: User to maintain any notes'}, index =[1])
    df2 = pd.concat([df1, dfnew]).reset_index(drop = True)
    df2=df2.T.reset_index().T.reset_index(drop=True)
    df3 = df2.reindex(index = [1, 0])
    appended_df=pd.concat([df3,df2],ignore_index=True)
    appended_df=appended_df.drop([2,3])
    appended_df = appended_df.drop_duplicates()
    return appended_df

def bomtodf(atombom):
        df=pd.DataFrame()
        for index,row in atombom.iterrows():
            Cpn=row['Mandatory: Part number as maintained by the customer']
            Cpndesc=row['Optional : Description as given by customer']
            Man=row['Mandatory: If normalized manufacturer name matches the normalized name in manufacturer table then Match else no match']
            Mpn=row['Mandatory: If normalized  partnumber matches the number in m master component then match else no match']
            Qty=row['Mandatory:  Quantity per PCBA. Allowed values:  Positive integer ( 0 or more ).  Empty values not allowed\'']
            #dfupdated=pd.concat([dfupdated,pd.DataFrame([row])],ignore_index = True)
            df=pd.concat([df,pd.DataFrame([{'Cpn':Cpn,'Cpndesc':Cpndesc,'Man':Man,'Mpn':Mpn,'Qty':Qty}])],ignore_index = True)
        return df

def merger(Mpn,df1,df2):
    condition=Mpn
    merged_df = pd.merge(df1, df2)
    specific_value_df = merged_df[merged_df['Mpn'] == condition]
    return specific_value_df

def validate1(rawbom,atombom):
    df=pd.DataFrame()
    subset = pd.merge(rawbom, atombom, how='inner')
    merged_df = pd.DataFrame()
    for index1, row1 in rawbom.iterrows():
        Mpn=row1['Mpn']
        merged_df=merger(Mpn,rawbom,atombom)
        cpn=row1['Cpn']
        value_present = Mpn in merged_df.values
        if(value_present):
            val='Yes'
        else:
            val='No'
        #dfupdated=pd.concat([dfupdated,pd.DataFrame([row])],ignore_index = True)
        df=pd.concat([df,pd.DataFrame([{'Customer Part Number':cpn,'Whether RAW BOM details are matching with ATOM BOM Template?':val}])],ignore_index = True)
    return df    

def validate(rawbom,atombom):
        #valdic={}
        df=pd.DataFrame()
        df1=pd.DataFrame()
        #cpnlist=rawbom['Cpn'].tolist()
        #subset = df1[atombom['Cpn'].isin([cpnlist])]
        #for (index1, row1), (index2, row2) in zip(rawbom.iterrows(), atombom.iterrows()):
        for (index1, row1), (index2, row2) in zip(rawbom.iterrows(), atombom.iterrows()):
            cpn=row1['Cpn']
            if(cpn == 'Unconfirmed'):
                flag=1
            else:
                flag=0
                subset=df1[row1['Cpn']==row2['Cpn']] #atombom['Cpn'].isin([cpn])]
            #print(subset)
            if(row1['Mpn']==subset['Mpn'] and flag==0):
                if(row1['Cpndesc']==subset['Cpndesc'] and row1['Man']==subset['Man'] and  row1['Qty']==subset['Qty'] ):
                    #if(~pd.isna(row1['Cpn'])>0):
                     #   if(row1['Cpn']==row2['Cpn']):
                    val='Yes' 
                else:
                    #valdic[row1['Cpn']]='No'
                    val='No'
            else:
                val='No'
                    #valdic[row1['Cpn']]='No'
            
            df=pd.concat([df,pd.DataFrame([{'Customer Part Number':cpn,'Whether RAW BOM details are matching with ATOM BOM Template?':val}])],ignore_index = True)
        
        return df
from openpyxl import load_workbook
def write2(filenames1,directory_path1,valdata):
    path=directory_path1+"/"+filenames1
    excel_file = path+'.xlsx'
    # Load the existing Excel file
    with pd.ExcelWriter(excel_file, mode='a', engine='openpyxl') as writer:
        # Write the DataFrame to a new sheet
        valdata.to_excel(writer, sheet_name='IPN_Match Status', index=False)

        # Save the changes
        #writer.close()
    
def rename1(df):
    df.rename(columns={'Customer Part number': 'Cpn','Customer part number description':'Cpndesc','Manufacturer name':'Man','Manufacturer part number':'Mpn','Quantity':'Qty'}, inplace=True)
    return df

def clipath():
    parser = argparse.ArgumentParser(description="Script to get input and output file paths.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    args = parser.parse_args()
    input_file_path = args.input_file
    output_file_path = args.output_file
    return input_file_path,output_file_path

def main():
    inpath,outpath=clipath()
    df_list,directory_path=get_files(inpath)
    filenames=filenameextract(directory_path)
    for i in range(len(filenames)):
        df=pd.DataFrame(df_list[i])
        #print(filenames[i])
        df=dfprepare(df,filenames[i])
        df=formatting(df)
        #print(df)
        df.to_excel(outpath+"/"+filenames[i] +"output.xlsx",index=False,header=False)

if __name__ == "__main__":
    main()


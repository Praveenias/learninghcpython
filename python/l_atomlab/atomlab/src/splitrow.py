from help import Help

### Enter input here ###
constantColumn = ['A','B']
repeatedColumn = [['C','K'],['L','R'],['S','Y'],['Z','AF'],['AG','AO'],['AP','AV']]
input_file_name = 'test2.xlsx'
output_file_name = 'output.xlsx'

### ###

IpDict = {'constantColumn':constantColumn,'repeatedColumn':repeatedColumn,
            'input_file_name':input_file_name,'output_file_name':output_file_name }
print("Processing...")
splitrow = Help()
result = splitrow.index(IpDict)

[print(i,':',j) for i,j in result.items()]


#
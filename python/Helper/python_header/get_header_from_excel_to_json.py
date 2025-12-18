import pandas

df = pandas.read_excel('./files/v3/Master_Component_Template.xlsx')
json_data = df.to_json()

# Optional: Save the JSON data to a file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)
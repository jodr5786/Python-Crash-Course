filename = 'smtp_whitelist_updated.txt'
formatted_test = 'smtp_whitelist_updated_formatted.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

txt_string = ''
for line in lines:
    txt_string += (line.strip() + ' ')

formatted_data = open(formatted_test, 'w')
formatted_data.write(txt_string)
formatted_data.close

print(txt_string)
# Image search script by ROO MCQUARRIE 2021

# Modules used within the script
import os
import shutil
import pandas as pd
from datetime import datetime
import time

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.abspath(os.path.dirname(__file__))))

# This is the only dependant line and must be file path to CSV
csv_path_to_sheet = open(os.path.join(__location__, 'IMAGE_SEARCH_SHEET.csv'))

# This is the excel doc containing the search params
df = pd.read_csv(csv_path_to_sheet)

# This is the list of codes to search
search_files = df['item_codes'].to_list()
print(search_files)

# Cell ref for the search directory returned as a str THIS WILL BE CELL ( F 2 )
search_dir_1 = df.iat[0, 5]
print(f"The search dir is :{search_dir_1}")

# Cell ref for the destination folder returned as a str THIS WILL BE ( I 2 )
dest_dir_1 = df.iat[0, 8]
print(f"The destination folder is :{dest_dir_1}")

# Extension list
suf_list = ['-1.jpg', '-2.jpg', '-3.jpg', '-4.jpg', '-5.jpg', '-6.jpg', '-7.jpg']


# Container for the new list of files with extensions
final_files = []
# Item Code plus the extension
for code in search_files:
    for extension in suf_list:
        final_files += [code + extension]
print("SEARCH RETURN POTENTIAL " + str(len(final_files)))

print('''

BY
██████╗  ██████╗  ██████╗ ███╗   ███╗ ██████╗ ██████╗ 
██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║██╔════╝██╔═══██╗
██████╔╝██║   ██║██║   ██║██╔████╔██║██║     ██║   ██║
██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║██║     ██║▄▄ ██║
██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║╚██████╗╚██████╔╝
╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚══▀▀═╝ 
                                                      

SEARCHING...
''')

# Container for the list of found files
list_of_found = []

tic = time.perf_counter()

# Function for the search, 3 Params, files to search, directory, container for found files
def search_and_copy(all_files, search_dir, found_output):
    for root, dirs, files in os.walk(search_dir):
        for _item in files:
            if _item in all_files:
                # If the item is found, notify, and copy to dest
                print("File found in:" + str(os.path.join(root, _item)))
                shutil.copy(os.path.join(root, _item), dest_dir_1)
                found_output += [_item]

#Function call
search_and_copy(all_files=final_files,search_dir=search_dir_1,found_output=list_of_found)

#print(list_of_found)

# Sorts list default
list_of_found.sort()


#Container for final list of files (Tuple)
final_output = []

#Function to compare original list with found list
def compare_result(original_list, images_found, output_list):
     for _item in original_list:
         if _item in os.listdir(images_found):
            # print(f'{_item},FOUND _')
             # Creates tuple
             output_list += [(_item , "FOUND")]
         else:
            # print(f'{_item},NOT FOUND _')
             # Creates tuple
             output_list += [(_item , "NOT FOUND")]


# Function call for results to be compared
compare_result(original_list=final_files, images_found=dest_dir_1, output_list=final_output)

#print(final_output)

output_as_dict = dict(final_output)

#print(output_as_dict)

# Pandas dataframe is created for the Results sheet
df2 = pd.DataFrame(list(final_output),columns=['IMAGE CODE', 'STATUS'])
#print(df2)

# Gets current working dir for the save
save_path = str(os.getcwd())

# Get the date and time to add to the file name
now = datetime.now()

# Format the date and time
the_date_time = now.strftime("%b%d%Y%H%M")

#print(the_date_time)

print('''

BY
██████╗  ██████╗  ██████╗ ███╗   ███╗ ██████╗ ██████╗ 
██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║██╔════╝██╔═══██╗
██████╔╝██║   ██║██║   ██║██╔████╔██║██║     ██║   ██║
██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║██║     ██║▄▄ ██║
██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║╚██████╗╚██████╔╝
╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚══▀▀═╝ 


''')

print(f"Your results can be found here : {save_path}/{the_date_time}_Search_Results.csv")

toc = time.perf_counter()

print(f"We made it in {toc - tic:0.4f} seconds")


# Save csv function 3 params
def save_out(data, unique_id, path):
    data.to_csv((path + '/' + unique_id + '_Search_Results.csv'), index=False)


save_out(data=df2, unique_id=the_date_time, path=save_path)
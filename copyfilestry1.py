import os, shutil

#List of files suffix' that are added to a list of files names form the .txt
sufList = ['-1.jpg', '-2.jpg', '-3.jpg', '-4.jpg', '-5.jpg', '-6.jpg', '-7.jpg']

#This function opens the txt and reads the list of file names a and adds the suffix
#before searching the directory for the file and copying it to the destination.
def origList(addSuf):
    with open('/Users/roomcq/Desktop/myfiles.txt', 'r') as f:
       myFiles = [line.strip() + (addSuf) for line in f]

    for root, dirs, files in os.walk('/Users/roomcq/Desktop/Server'):
       for _item in files:
            if _item in myFiles:
                # If we find it, notify us about it and copy it it to C:\NewPath\
                print('Found file in: ' + str(root) + '/' + str(_item))
                shutil.copy(os.path.abspath(root + '/' + _item), '/Users/roomcq/Desktop/Destination')


origList(sufList[0])
origList(sufList[1])
origList(sufList[2])
origList(sufList[3])
origList(sufList[4])
origList(sufList[5])
origList(sufList[6])

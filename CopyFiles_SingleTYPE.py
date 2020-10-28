import glob
import shutil

#Destination Directory
dest_Dir = "/Users/roomcq/Desktop/Test_PY/test_Server/STUDIO_LIVE/PROCESS"

#Outer destination dir ** for more than 1 possible sub-dir
src_Dir = r'/Users/roomcq/Desktop/Test_PY/test_Server/STUDIO_LIVE/2020/**/_COMPLETE/'

#Specify file types types and wildcards
kindOfFile = '*.jpg'

# returns all dirs and files ending as specified
for file in glob.glob(src_Dir + kindOfFile, recursive=True):
    print(file)
    #copies the files to the destination
    shutil.copy(file, dest_Dir)




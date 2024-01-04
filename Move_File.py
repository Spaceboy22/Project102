import os
import shutil

source = "Document_Files"
os.mkdir("Destination")
destination = 'Destination'

list_of_files = os.listdir(source)
for i in list_of_files:
    name,extension=os.path.splitext(i)
    if extension == '':
        continue
    if extension in ['.pdf', '.docs', '.pptx',]:
        path1 = source +"/"+ i
        path2 = destination + "/" + 'Document_files'
        path3 = destination + "/" + 'Document_files' + "/" + i
        
        if os.path.exists(path2):
            print("Document folder exists\nMoving Files....")
            shutil.move(path1,path3)
            print('Process Completed.....')
        else:
            print("Document Folder doesn't exist")
            os.mkdir(path2)
            print("Document folder has been created\nMoving Files....")
            shutil.move(path1,path3)
            print('Process Completed.....')
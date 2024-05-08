import os
import shutil
import sys


sys.stdout=open('Update.txt', 'w', encoding='utf-8')

def file_organizer():
    dir_being_scanned = r'C:\Users\joshu\Downloads'
    base_dir = r'C:\Users\joshu\OneDrive\Desktop\sorted'

    files=[

    ]
    folders=[

    ]

    #Initializing extensions to be used
    extensions=[
        'py', 
        'txt', 
        'zip',
        'jpg',
        ]

    #Definning directory names
    text_directory='files'
    image_directory='images'
    python_directory='python_projects'
    zip_directory='zip files'


    #Creating file paths
    python_directory=os.path.join(base_dir, python_directory)
    text_directory=os.path.join(base_dir, text_directory)
    image_directory=os.path.join(base_dir, image_directory)

    zip_directory=os.path.join(base_dir, zip_directory)


    #Scanning target directory
    obj=os.scandir(path=dir_being_scanned)


    #Retrieving file names and categorizing them accoringly
    if obj:
        for element in obj:
            if element.is_file():
                files.append(element.name)

            elif element.is_dir():
                folders.append(element.name)
        print(f'The total number of zip directories being moved are: {len(folders)}\n And the number of files being moved are: {len(files)}')

        obj.close()

    #Moving files
    try:
        for file_element in files:
            if file_element.endswith(extensions[0]):
                python_object=os.path.join(dir_being_scanned, file_element)
                shutil.move(python_object, python_directory)
                
            

            elif file_element.endswith(extensions[1]):
                text_objects=os.path.join(dir_being_scanned, file_element)
                shutil.move(text_objects, text_directory)
                
                
            
            elif file_element.endswith(extensions[3]):
                image_object=os.path.join(dir_being_scanned, file_element)
                shutil.move(image_object, image_directory)
                
            
                
        print("All files have been moved accordingly...")

    except Exception as e:
        print(f"There was an error moving the files: {e}")


    #Moving zip directories
    try:
        for dir_element in folders:
            if dir_element.endswith(extensions[2]):
                folder_object=os.path.join(dir_being_scanned, dir_element)
                shutil.move(folder_object, zip_directory)
                
        print('Zip files moved accordingly')

    except Exception as e:
        print(f'There was an error moving the zip directories: {e}')



if __name__ == "main":
    print("Running on main document...")

    file_organizer()
else:
    print("Module has been exported...")

    file_organizer()
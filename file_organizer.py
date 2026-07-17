print("        file organizer           ")




import os 
import shutil
folder=input("Enter folder address :   ").strip().strip('"')

if not os.path.exists(folder):
    print("folder does not exist")
files=os.listdir(folder)
for file in files:
    print(file)
    if file.lower().endswith((".docx",".pdf",".doc",".ppt",".pptx")):
        os.makedirs(os.path.join(folder,"documents"),exist_ok=True)
        path=os.path.join(folder,file)
        if os.path.isfile(path):
        
           destination_dir=os.path.join(folder,"documents")
           destination=os.path.join(destination_dir,file)
           shutil.move(path,destination)
    elif file.lower().endswith((".bmp",".jpg",".jpeg",".webp",".gif",".svg",".tiff",".png")):
        os.makedirs(os.path.join(folder,"images"),exist_ok=True) 
        path=os.path.join(folder,file)
        if os.path.isfile(path):
            destination_dir=os.path.join(folder,"images")
            destination=os.path.join(destination_dir,file)
            shutil.move(path,destination)
    elif file.lower().endswith((".xlsx",".xlsm")):
        os.makedirs(os.path.join(folder,"excel"),exist_ok=True)#folder
        path=os.path.join(folder,file)
        if os.path.isfile(path):
           destination_dir=os.path.join(folder,"excel")#folder address
           destination=os.path.join(destination_dir,file)#address for putting file inside the folder
           shutil.move(path,destination)
    elif file.lower().endswith(".txt"):
        os.makedirs(os.path.join(folder,"text file"),exist_ok=True)
        path=os.path.join(folder,file)
        if os.path.isfile(path):
            destination_dir=os.path.join(folder,"text file")#folder
            destination=os.path.join(destination_dir,file)#file
            shutil.move(path,destination)

    elif file.lower().endswith((".mp3",".wav",".flac",".mp4",".mkv",".avi")):
        os.makedirs(os.path.join(folder,"audio and video files"),exist_ok=True)
        path=os.path.join(folder,file)
        if os.path.isfile(path):
            destination_dir=os.path.join(folder,"audio and video files")
            destination=os.path.join(destination_dir,file)
            shutil.move(path,destination)
    elif file.lower().endswith((".zip",".rar"".7z")):
        os.makedirs(os.path.join(folder,"compressed"),exist_ok=True)
        path=os.path.join(folder,file)
        if os.path.isfile(path):
            destination_dir=os.path.join(folder,"compressed")
            destination=os.path.join(destination_dir,file)
            shutil.move(path,destination)

    elif file.lower().endswith(".exe"):
        os.makedirs(os.path.join(folder,"exe files"),exist_ok=True)
        path=os.path.join(folder,file)
        if os.path.isfile(path):
            destination_dir=os.path.join(folder,"exe files")
            destination=os.path.join(destination_dir,file)
            shutil.move(path,destination)

    
    


        
    else:
        continue
    



        



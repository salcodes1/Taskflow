from Task import Task

creeazafolder = Task(["cd ~/$$LOCATION$$", "mkdir $$FOLDER_NAME$$"], default_values={"FOLDER_NAME": "Mama"})
print(creeazafolder.execute({"LOCATION": "Documents", "FOLDER_NAME": "Alex"}))

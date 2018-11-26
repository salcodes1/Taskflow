from Task import Task

crfolder = Task(["cd ~/$$LOCATION$$", "mkdir $$FOLDER_NAME$$"], default_values={"LOCATION": "Desktop"})
delfolder = Task(["cd ~/$$LOCATION$$", "rmdir $$FOLDER_NAME$$"], default_values={"LOCATION": "Desktop"})

action = "cr"
for i in range(0, 10):
    if action == "cr":
        crfolder.execute({"FOLDER_NAME": "F" + str(i)})
    elif action == "del":
        delfolder.execute({"FOLDER_NAME": "F" + str(i)})
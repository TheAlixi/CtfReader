import os
import colorama
from colorama import Fore, Back

colorama.init()

class CtfFile:
    def __init__(self, filepath):
        if os.path.isfile(filepath):
            self.filepath = filepath
            self.file = open(filepath, 'r')
            self.filedata = self.file.readlines()
            
            self.file.close()
            
    def getText(self):
        return self.filedata
    
    def getAllLines(self):
        lines = ""
        
        for line in self.filedata:
            lines += line + "\n"
        
        return lines
    
    def read(self):
        c_obj = {}
        for i in range(len(self.filedata)):
            if self.filedata[i].replace("\n", "").startswith("["):
                if self.filedata[i].replace("\n", "").endswith("]"):
                    data = self.filedata[i].replace("]", "").replace("[", "").replace("\n", "")
                    
                    if not data == ".":
                        c_obj.update({"fulldata": data, "forecolor": "none", "backcolor": "none"})
                    
                    pdata = data.replace(" ", "").split(",")
                    
                    if ":" in data:
                        for d in pdata:
                            cd = d.replace(" ", "").split(":")
                            
                            if cd[0] == "fg":
                                if cd[1] == "Green" or "Blue" or "Red" or "Cyan" or "Purple" or "Yellow" or "Black" or "White":
                                    c_obj.update({"forecolor": cd[1]})
                            elif cd[0] == "bg":
                                if cd[1] == "Green" or "Blue" or "Red" or "Cyan" or "Yellow" or "Black" or "White":
                                    c_obj.update({"backcolor": cd[1]})
                    elif data == ".":
                        c_obj = {}
                        print(Fore.WHITE)
                        print(Back.BLACK)
                    else:
                        raise TypeError("Invalid tag")
                else:
                    raise TypeError("Invalid tag")
            elif c_obj == {}:
                print(self.filedata[i].replace("\n", ""))
            else:
                if not c_obj == {}:
                    if c_obj['forecolor'] == "Green":
                        print(Fore.GREEN)
                    elif c_obj['forecolor'] == "Red":
                        print(Fore.RED)
                    elif c_obj['forecolor'] == "Blue":
                        print(Fore.BLUE)
                    elif c_obj['forecolor'] == "Cyan":
                        print(Fore.CYAN)
                    elif c_obj['forecolor'] == "Purple":
                        print(Fore.PURPLE)
                    elif c_obj['forecolor'] == "Yellow":
                        print(Fore.YELLOW)   
                    elif c_obj['forecolor'] == "Black":
                        print(Fore.BLACK)
                    elif c_obj['forecolor'] == "White":
                        print(Fore.WHITE)
                    if c_obj['backcolor'] == "Green":
                        print(Back.GREEN)
                    elif c_obj['backcolor'] == "Red":
                        print(Back.RED)
                    elif c_obj['backcolor'] == "Blue":
                        print(Back.BLUE)
                    elif c_obj['backcolor'] == "Cyan":
                        print(Back.CYAN)
                    elif c_obj['backcolor'] == "Yellow":
                        print(Back.YELLOW)   
                    elif c_obj['backcolor'] == "Black":
                        print(Back.BLACK)
                    elif c_obj['backcolor'] == "White":
                        print(Back.WHITE)
                    
                    print(self.filedata[i].replace("\n", ""))
                else:
                    print(self.filedata[i].replace("\n", ""))
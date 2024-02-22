class Phonebook():
    
    #main function
    def __init__(self):
        
        self.phone_dict = {}
        
        #dictionary of commands available for user
        commands = {
            "add": self.new_add,
            "lookup": self.lookup,
            "alias": self.alias,
            "change": self.change,
            "save": self.save,
            "load": self.load,
            "quit": self.quit_prog
        }
        
        while True:
            screen_prompt = input("phonebook> ") #the prompt in the terminal
            user_input = screen_prompt.split() #returns list of substrings
            
            try:
                #takes first string of the "split input list" and calls function from "commands" dictionary
                #the "*..." sends the other strings from "split input list" except first as separate arguments
                commands[user_input[0]](*user_input[1:])
            except SystemExit: 
                break #breaks loop, exits program
            except:
                print("command not found")
    
    #adds name and number to dictionary
    def new_add(self, name, number):
        if number in self.phone_dict.values(): #checks for duplicate number in values "phone_dict"
            print(number, "already exists")
        elif name in self.phone_dict.keys(): #checks for duplicate name in keys in "phone_dict"
            print(name, "already exists")
        else:
            self.phone_dict[name] = number
    
    #lookup number of name
    def lookup(self, name):
        if name in self.phone_dict.keys(): #checks for names' existance in "phone_dict"
            print(self.phone_dict[name])
        else:
            print(name, "not found")
    
    #add nickname/alias to name in cataloge        
    def alias(self, name, alias):
        #checks for duplicate name and existance for both inputted name and alias in keys in "phone_dict" 
        if name in self.phone_dict.keys() and alias not in self.phone_dict.keys():
            self.phone_dict[alias] = self.phone_dict[name] #adds alias with same phonenumber as name
        else:
            print("name not found or duplicate name")
    
    #change number for name and its aliases
    def change(self, name, newnumber):
        matching_keys = []

        if name in self.phone_dict.keys(): #checks for names' existance in "phone_dict"
            if newnumber in self.phone_dict.values(): #checks for duplicate number in values "phone_dict"
                print(newnumber, "already exists")
                
            else: 
                for key, value in self.phone_dict.items(): #iterates through names and numbers
                    if value == self.phone_dict[name]: #checks for what aliases share same number
                        matching_keys.append(key) #adds name and aliases to "matching_keys" list
                #changes the number for name and aliases in the dictionary
                for matches in matching_keys:
                    self.phone_dict[matches] = newnumber
       
        else:
            print(name, "not found")
            
    
    #save number and names to a textfile
    def save(self, savename):
        with open(savename, 'w') as file:
            #iterates trough all names (and aliases) with their ascossiated numbers
            for name, number in self.phone_dict.items():
                line = f"{number};{name};\n" #format name and number
                file.write(line) #writes the formatted name and number to textfile
    
    #loads texfile and gets number and names
    def load(self, loadname):
        try: 
            with open(loadname, 'r') as file: 
                self.phone_dict = {} #empties the dictionary before loading
                #iterates through the lines in the textfile
                for line in file:
                    separate = line.split(";") #removes semicolons to isolate the name and number
                    number = separate[0]
                    name = separate[1]
                    self.phone_dict[name] = number #fills dictionary with contents from textfile
        except:
            print(loadname, "does not exist")
                
    #quits program
    def quit_prog(self):
        #runs "except SystemExit:" in "__init__" function
        raise SystemExit
    
Phonebook()
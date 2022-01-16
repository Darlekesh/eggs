# Update all minecraft eggs to support arm64

# Affected directories are: game_eggs/minecraft/java, game_eggs/minecraft/proxy/java
# Affected files files are .json

import os
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def update_json(file_location):
    data=""
    

    with open(file_location) as json_file:
        data = json.load(json_file)
        # if images doesnt exist return 
        if not 'images' in data:
            print(bcolors.WARNING + "No images in " + file_location + bcolors.ENDC)
            
            return
        
        # If data includes ghcr.io/pterodactyl/yolks:java_17 then add ghcr.io/software-noob/arm64:java_17
        if "ghcr.io/pterodactyl/yolks:java_17" in data["images"]:
            # Chech if ghcr.io/software-noob/arm64:java_17 is already in data["images"] if not add it
            if "ghcr.io/software-noob/arm64:java_17" not in data["images"]:
                data["images"].append("ghcr.io/software-noob/arm64:java_17")
        # Add all java versions from 16 to 8
        # If data includes ghcr.io/pterodactyl/yolks:java_16 then add ghcr.io/software-noob/arm64:java_16
        if "ghcr.io/pterodactyl/yolks:java_16" in data["images"]:
            # Chech if ghcr.io/software-noob/arm64:java_16 is already in data["images"] if not add it
            if "ghcr.io/software-noob/arm64:java_16" not in data["images"]:
                data["images"].append("ghcr.io/software-noob/arm64:java_16")
        # If data includes ghcr.io/pterodactyl/yolks:java_15 then add ghcr.io/software-noob/arm64:java_15
        if "ghcr.io/pterodactyl/yolks:java_15" in data["images"]:
            # Chech if ghcr.io/software-noob/arm64:java_15 is already in data["images"] if not add it
            if "ghcr.io/software-noob/arm64:java_15" not in data["images"]:
                data["images"].append("ghcr.io/software-noob/arm64:java_15")
        # If data includes ghcr.io/pterodactyl/yolks:java_14 then add ghcr.io/software-noob/arm64:java_14
        if "ghcr.io/pterodactyl/yolks:java_14" in data["images"]:
            # Chech if ghcr.io/software-noob/arm64:java_14 is already in data["images"] if not add it
            if "ghcr.io/software-noob/arm64:java_14" not in data["images"]:
                data["images"].append("ghcr.io/software-noob/arm64:java_14")
        # If data includes ghcr.io/pterodactyl/yolks:java_13 then add ghcr.io/software-noob/arm64:java_13
        if "ghcr.io/pterodactyl/yolks:java_13" in data["images"]:
            # Chech if ghcr.io/software-noob/arm64:java_13 is already in data["images"] if not add it
            if "ghcr.io/software-noob/arm64:java_13" not in data["images"]:
                data["images"].append("ghcr.io/software-noob/arm64:java_13")
        # If data includes ghcr.io/pterodactyl/yolks:java_12 then add ghcr.io/software-noob/arm64:java_12
        if "ghcr.io/pterodactyl/yolks:java_12" in data["images"]:
            # Chech if ghcr.io/software-noob/arm64:java_12 is already in data["images"] if not add it
            if "ghcr.io/software-noob/arm64:java_12" not in data["images"]:
                data["images"].append("ghcr.io/software-noob/arm64:java_12")
        # If data includes ghcr.io/pterodactyl/yolks:java_11 then add ghcr.io/software-noob/arm64:java_11
        if "ghcr.io/pterodactyl/yolks:java_11" in data["images"]:
            # Chech if ghcr.io/software-noob/arm64:java_11 is already in data["images"] if not add it
            if "ghcr.io/software-noob/arm64:java_11" not in data["images"]:
                data["images"].append("ghcr.io/software-noob/arm64:java_11")
        # If data includes ghcr.io/pterodactyl/yolks:java_10 then add ghcr.io/software-noob/arm64:java_10
        if "ghcr.io/pterodactyl/yolks:java_10" in data["images"]:
            # Chech if ghcr.io/software-noob/arm64:java_10 is already in data["images"] if not add it
            if "ghcr.io/software-noob/arm64:java_10" not in data["images"]:
                data["images"].append("ghcr.io/software-noob/arm64:java_10")
        # If data includes ghcr.io/pterodactyl/yolks:java_9 then add ghcr.io/software-noob/arm64:java_9
        if "ghcr.io/pterodactyl/yolks:java_9" in data["images"]:
            # Chech if ghcr.io/software-noob/arm64:java_9 is already in data["images"] if not add it
            if "ghcr.io/software-noob/arm64:java_9" not in data["images"]:
                data["images"].append("ghcr.io/software-noob/arm64:java_9")
        # If data includes ghcr.io/pterodactyl/yolks:java_8 then add ghcr.io/software-noob/arm64:java_8
        if "ghcr.io/pterodactyl/yolks:java_8" in data["images"]:
            # Chech if ghcr.io/software-noob/arm64:java_8 is already in data["images"] if not add it
            if "ghcr.io/software-noob/arm64:java_8" not in data["images"]:
                data["images"].append("ghcr.io/software-noob/arm64:java_8")
    
    # save the data to the file_location again but json formatted
    with open(file_location, 'w') as outfile:
        json.dump(data, outfile, indent=4)
        
        
        
        
        

# for all json files in subdirectories of the game_eggs/minecraft/java and game_eggs/minecraft/proxy/java
for root, dirs, files in os.walk("game_eggs/minecraft/java"):
    for file in files:
        if file.endswith(".json"):
            # print its name
            update_json(os.path.join(root, file))
for root, dirs, files in os.walk("game_eggs/minecraft/proxy/java"):
    for file in files:
        if file.endswith(".json"):
            # print its name
            update_json(os.path.join(root, file))
print("Done!")

# create function to update json files



user_security = { "Moe": 4,     # Only for Her Majesty's eyes
                 "Larry" : 3,   # Top secret
                 "Curly": 2,    # Secret
                 "Shemp" : 1    # Public
                 }

class security:
    def __init__ (self, name, level):
        self.level = level  # Security level of user
        self.name = name
    
    def can_read(self, file):
        # High clearance can read lower clearance file
        return self.level >= file.level
    
    def can_write(self, file):
        # Low clearance can write to a higher clearance file
        return self.level >= file.level
    
class File:
    def __init__(self, name, level, content=""):
        self.name = name
        self.level = level  # Security level of the file
        self.content = content

    def __str__(self):
        return f"File: {self.name}, Level: {self.level}, Content: {self.content}"
    
def main():
    moe = security("Moe", user_security["Moe"])
    larry = security("Larry", user_security["Larry"])
    curly = security("Curly", user_security["Curly"])
    shemp = security("Shemp", user_security["Shemp"])

    # Createing files
    public_file = File("Public Information", 1, "This is public information.")
    secret_file = File("Secret Information", 2, "This is secret information.")
    top_secret_file = File("Top Secret Information", 3, "This is top secret information.")
    hme_file = File("Her Majesty's Information", 4, "This is classified information for her majesty.")

    # Moe tries to read/write
    if moe.can_read(hme_file):
        print(f"{moe.name} is reading the file: {hme_file.name}")
        print(f"Security level: {hme_file.content}")
    else:
        print(f"Warning: {moe.name} is not allowed to read {hme_file.name}.")

    if moe.can_write(hme_file):
        hme_file.content += " New content for her majesty."
        print(f"{moe.name} has written to the file: {hme_file.name}")
    else:
        print(f"Warning: {moe.name} is not allowed to write to {hme_file.name}.")

    # Larry tries to read/write
    if larry.can_read(top_secret_file):
        print(f"{larry.name} is reading the file: {top_secret_file.name}")
        print(f"Security level: {top_secret_file.content}")
    else:
        print(f"Warning: {larry.name} is not allowed to read {top_secret_file.name}.")

    if larry.can_write(secret_file):
        secret_file.content += " New content from Larry."
        print(f"{larry.name} has written to the file: {secret_file.name}")
    else:
        print(f"Warning: {larry.name} is not allowed to write to {secret_file.name}.")

    # Curly tries to read/write
    if curly.can_read(secret_file):
        print(f"{curly.name} is reading the file: {secret_file.name}")
        print(f"Security level: {secret_file.content}")
    else:
        print(f"Warning: {curly.name} is not allowed to read {secret_file.name}.")

    if curly.can_write(secret_file):
        secret_file.content += " Curly's content."
        print(f"{curly.name} has written to the file: {secret_file.name}")
    else:
        print(f"Warning: {curly.name} is not allowed to write to {secret_file.name}.")

    # Shemp tries to read/write
    if shemp.can_read(public_file):
        print(f"{shemp.name} is reading the file: {public_file.name}")
        print(f"Security level: {public_file.content}")
    else:
        print(f"Warning: {shemp.name} is not allowed to read {public_file.name}.")

    if shemp.can_write(public_file):
        public_file.content += " Shemp's content."
        print(f"{shemp.name} has written to the file: {public_file.name}")
    else:
        print(f"Warning: {shemp.name} is not allowed to write to {public_file.name}.")

    # Checks for read/write
    if shemp.can_read(top_secret_file):
        print(f"{shemp.name} is reading the file: {top_secret_file.name}")
    else:
        print(f"Warning: {shemp.name} is not allowed to read {top_secret_file.name}.")

    if larry.can_write(public_file):
        public_file.content += " Public content from Larry."
        print(f"{larry.name} has written to the file: {public_file.name}")
    else:
        print(f"Warning: {larry.name} is not allowed to write to {public_file.name}.")

if __name__ == "__main__":
    main()

"""
@brief generates directories and files for a new module.
@class Module
@param module_names: the names of the modules to be created.
@returns None

@details
usage: make_mod.py <module_name>

creates a new module with the given name and the following directory structure:
    module_name -> data | docs | assets | src | tests | scripts | tools | files
    data -> raw | processed | output
    docs -> api | design | notes | reports
    assets -> images | text
    src -> components | models | utils | include
    tests -> unit | integration | e2e
    scripts -> js | py
    tools -> build | deploy
    files -> README.md | CONTRIBUTING.md | LICENSE | package.json | .gitignore
"""
#imports
from os import path, makedirs
from datetime import datetime

#class
class Module:
    """
    Module class
    @brief generates directories and files for a new module.
    @param module_names: the name of the module to be created.

    @methods
    create_module(self, module_name:str) -> bool
    create_subdirectory(self, module_name:str, subdirectory:str) -> bool
    create_files(self) -> bool
    create_modules(self) -> None
    
    @details 
    creates a new module with the given name and the following directory structure:
        module_name -> data | docs | assets | src | tests | scripts | tools | files
        data -> raw | processed | output
        docs -> api | design | notes | reports
        assets -> images | text
        src -> components | models | utils | include
        tests -> unit | integration | e2e
        scripts -> js | py
        tools -> build | deploy
        files -> README.md | CONTRIBUTING.md | LICENSE | package.json | .gitignore
    """
    def __init__(self, module_names:list[str]) -> None:
        self.dir_structure:dict = {
            "module_names": tuple(module_names),
            "directories": {
                "data": ("raw", "processed", "output"),
                "docs": ("api", "design", "notes", "reports"),
                "assets": ("images", "text"),
                "src": ("components", "models", "utils", "include"),
                "tests": ("unit", "integration", "e2e"),
                "scripts": ("js", "py"),
                "tools": ("build", "deploy")
            },
            "files": ("README.md", "CONTRIBUTING.md", "LICENSE", "package.json", ".gitignore")
        }
    def create_module(self, module_name:str) -> bool:
        """
        @brief creates a new module
        @param module_name: name of the module to create
        @returns bool: if module is created then true, else false

        @note
        Time: O(1)
        Space: O(1)

        @details
        takes module_name and creates an empty directory
        """
        #check if module exists in path
        if not path.exists(module_name):
            makedirs(module_name, exist_ok=True)
            return True
        return False

    def create_directory(self, module_name:str, directory:str) -> bool:
        """
        @brief creates a new directory
        @param module_name: name of the module to create
        @param directory: name of the directory to create
        @returns bool: if directory is created then true, else false

        @note
        Time: O(1)
        Space: O(1)

        @details
        takes module_name and directory, creates an empty directory
        """
        #check if module exists and subdirectory does not exist
        if path.exists(module_name) and not path.exists(f'{module_name}/{directory}'):
            makedirs(f'{module_name}/{directory}', exist_ok=True)
            return True
        return False
    
    def create_subdirectories(self, module_name:str) -> bool:
        """
        @brief creates subdirectories
        @param module_name: name of the module to create
        @returns bool: if subdirectories are created then true, else false

        @note
        Time: O(n^2)
        Space: O(n)

        @details
        takes module_name, and creates subdirectories in the module
        """
        #create defined directories
        for directory in self.dir_structure.get('directories'):
            makedirs(f'{module_name}/{directory}', exist_ok=True)
            #create sub directories 
            for sub_directory in self.dir_structure.get('directories').get(directory):
                makedirs(f'{module_name}/{directory}/{sub_directory}', exist_ok=True)
        return True

    def create_files(self, module_name) -> bool:
        """
        @brief creates files
        @returns bool: if files are created then true, else false

        @note
        Time: O(n)
        Space: O(n)

        @details
        creates files in the current directory
        """
        #no files defined
        if len(self.dir_structure.get('files')) == 0:
            return False
        
        #create files
        for file in self.dir_structure.get('files'):
            #file will close after writing
            with open(f'{module_name}/{file}', 'w') as f:
                if file == self.dir_structure.get('files')[0]:
                    f.write(f'# {module_name.capitalize()}\nCreated -> {datetime.now()}\nAuthor -> \n\n## Description\n\n')
                else:
                    f.write('')
        return True
    
    def create_modules(self) -> None:
        """
        @brief creates modules from given modules
        @returns None

        @details
        takes module_names, and creates modules from the given names.
        outputs success or failure of module creation.
        """
        for module in self.dir_structure.get('module_names'):
            self.log(f"Creating module {module} has {'succeeded' if self.create_module(module) else 'failed'}")
            self.log(f"Creating subdirectories for {module} has {'succeeded' if self.create_subdirectories(module) else 'failed'}")
            self.log(f"Creating files for {module} has {'succeeded' if self.create_files(module) else 'failed'}")

    def log(self, message:str) -> None:
        """
        @brief logs a message
        @param message: the message to log
        @returns None

        @details
        logs the message to the console
        """
        with open('log.txt', 'a') as f:
            f.write(f'{datetime.now()}\t{message}\n')
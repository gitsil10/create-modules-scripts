#imports
from sys import argv, exit
from module import Module

#main
def main():
    print("Start")
    if len(argv) < 2:
        print(f"Usage: {argv[0]} <module_names>\nExiting...")
        exit(1)
    print('Creating module(s)...')
    modules = Module(argv[1:])
    modules.create_modules()
    print('Finished')  

#driver
if __name__ == '__main__':
    main()
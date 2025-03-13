from gui import gui_main
from db import conectar_bd

def main():
    conectar_bd()
    gui_main()

if __name__ == "__main__":
    main()

from gui import *
import logic

def main():
    application = QApplication([])
    window = logic.Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()
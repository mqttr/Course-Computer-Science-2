import logic
import gui

def main():
    application = gui.QApplication([])
    window = logic.Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()
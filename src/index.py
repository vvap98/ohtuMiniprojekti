from app import App 
from viittauskirjasto import Viittauskirjasto
from console_io import ConsoleIO

def main():
    kirjasto = Viittauskirjasto()
    io = ConsoleIO()
    app = App(kirjasto, io)
    app.run()


if __name__ == "__main__":
    main()

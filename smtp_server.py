from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Debugging

def main():
    print("----- Fake SMTP server -----")
    host_name = 'localhost'
    port_number = 8025

    handler = Debugging()  # Or your custom handler
    controller = Controller(handler, hostname=host_name, port=port_number)
    controller.start()
    print(f"SMTP server started on {host_name}:{port_number}. Press Enter to stop.")
    
    input()  # Keep the server running until Enter is pressed
    controller.stop()

if __name__ == "__main__":
    main()
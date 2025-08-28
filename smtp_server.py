import argparse
from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Debugging

def main():
    # Create parser
    parse = argparse.ArgumentParser(
        description="This is my parser"
    )
    # Add argument(s) to parser
    parse.add_argument("-n", dest="host_name", default="localhost", type=str)
    parse.add_argument("-p", dest="port_number", default=8025, type=int)
    # Parsing arguments
    args = parse.parse_args()
    # get values
    host_name:str = args.host_name
    port_number:int = args.port_number

    print("----- Fake SMTP server -----")
    try:
        handler = Debugging()  # Or your custom handler
        controller = Controller(handler, hostname=host_name, port=port_number)
        controller.start()
        print(f"SMTP server started on {host_name}:{port_number}. Press Enter to stop.")
        
        input()  # Keep the server running until Enter is pressed
        controller.stop()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
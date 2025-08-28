import argparse

def main():
    # Create parser
    parse = argparse.ArgumentParser(
        description="This is my parser"
    )
    # Add argument(s) to parser
    parse.add_argument("-o", dest="run_option", default=0, type=int)
    # Parsing arguments
    args = parse.parse_args()
    # get values
    run_option:int = args.run_option

    match run_option:
        case 0:
            print("Hello from fake-services! Please check how to use me by the '-h' argument.")

        case 1:
            print("Fake SMTP server test")
            import smtplib
            from email.mime.text import MIMEText

            host_name:str = 'localhost'
            port_number:int = 8025
            try:
                with smtplib.SMTP(host_name, port_number) as server:
                    server.set_debuglevel(1)  # Enable debugging output
                    server.ehlo()
                    msg = MIMEText('This is a test email.')
                    msg['Subject'] = 'Test Subject'
                    msg['From'] = 'sender@example.com'
                    msg['To'] = 'recipient@example.com'
                    server.send_message(msg)
                    print("Email sent successfully!")
            except Exception as e:
                print(f"Error sending email: {e}")

        case _:
            print(f"Error: wrong run_option({run_option})!")

if __name__ == "__main__":
    main()

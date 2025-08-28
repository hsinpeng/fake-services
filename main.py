def main():
    print("Hello from fake-services!")

    run_option = 1
    match run_option:
        case 0:
            print("Simple test")

        case 1:
            print("Fake SMTP server test")
            import smtplib
            from email.mime.text import MIMEText

            host_name = 'localhost'
            port_number = 8025
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

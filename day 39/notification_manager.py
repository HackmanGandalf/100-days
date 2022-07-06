import smtplib
import flight_search

USERNAME = "username"
PASSWORD = "password"
class NotificationManager:
    def notify (self, message, emails, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="email", password="password")
            for email in emails:
                connection.sendmail(
                    from_addr="email",
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
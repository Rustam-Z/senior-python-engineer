"""
Liskov Substitution Principle.
- A subclass must be substitutable for its super-class.  The aim of this
principle is to ascertain that a subclass can assume the place of its
super-class without errors.  If the code finds itself checking the type of class
then, it must have violated this principle.

https://www.pythontutorial.net/python-oop/python-liskov-substitution-principle/
"""


from abc import ABC, abstractmethod


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')


class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


def main_good_example():
    contact = Contact('John Doe', 'john@test.com', '(408)-888-9999')

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send('Hello John')

    notification_manager.notification = email_notification
    notification_manager.send('Hi John')


if __name__ == '__main__':
    main_good_example()

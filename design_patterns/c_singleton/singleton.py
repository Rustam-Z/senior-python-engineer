"""
Singleton restricts a class from having more than one instance and ensures a global access point to this instance.

Use case. Singleton helps
    - Manage a shared resource: i.e. a single database, file manager, or printer spooler shared by multiple parts of the application.
    - Store a global state (help filepath, user language, application path, etc.).
    - Create a simple logger.

+ Class has a single instance
- Violates the SRP (Single Responsibility Principle).
- It’s hard to unit test the code as the majority of test frameworks use inheritance when creating mock objects.
"""


class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == "__main__":
    s = Singleton()
    print("Object created:", s)

    s1 = Singleton()
    print("Object created:", s1)

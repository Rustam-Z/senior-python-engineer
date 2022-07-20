"""
Adapter pattern - making the incompatible objects adaptable to each other.
                  Converts the interface of a class into another one that a client is expecting.

For example, Adapter could help convert XML data format to JSON for further analysis.

+ Allows separating the interface from business logic.
+ Adding new adapters doesn’t break the client’s code
- Increases the code complexity

Bridge and decorator related to Adapter pattern.
"""


class Target:
    def request(self):
        return "Target: The default target's behavior."


class Adaptee:
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    def request(self):
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target"):
    print(target.request())


def main():
    print("Client: I can work just fine with the Target objects:")

    target = Target()
    client_code(target)

    adaptee = Adaptee()

    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}")

    print("Client: But I can work with it via the Adapter:")

    adapter = Adapter()
    client_code(adapter)


if __name__ == "__main__":
    main()

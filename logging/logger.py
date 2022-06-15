"""
Python Logging

- Captures and records events while app is running
- Events can be categorized for easier analysis
- Highly customizable outputs
- Debugging
"""

import logging


def main():
    # Use basicConfig to configure logging
    # this is only executed once, subsequent calls to
    # basicConfig will have no effect
    logging.basicConfig(level=logging.INFO,
                        filemode="w",
                        filename="output.log",
                        format="%(asctime)s [%(levelname)s] %(message)s",
                        )

    # Try out each of the log levels
    logging.debug("This is a debug-level log message")
    logging.info("This is an info-level log message")
    logging.warning("This is a warning-level message")
    logging.error("This is an error-level message")
    logging.critical("This is a critical-level message")

    # Output formatted string to the log
    logging.info("Here's a {} variable and an int: {}".format("string", 10))


if __name__ == "__main__":
    main()

from datetime import datetime


class ConsoleLogger:
    """Simple class for logging data to console."""

    @staticmethod
    def log(msg):
        """Adds date-time tag and prints the message."""
        date = datetime.now().strftime("%x, %X")
        print(f"[{date}] {msg}")

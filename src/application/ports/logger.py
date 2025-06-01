from typing import Protocol


class ILogger(Protocol):
    """
    Defines a logging interface for different log levels.
    Any logger implementation should adhere to this protocol to ensure consistent logging behavior.
    """

    def info(self, message: str) -> None:
        """
        Logs an informational message, typically used for general application flow tracking.

        :param message: The message to log, which may include placeholders for formatting.
        :return: None
        """

    def error(self, message: str) -> None:
        """
        Logs an error message, indicating a problem that needs attention but may not halt execution.

        :param message: The error message to log, which may include placeholders for formatting.
        :return: None
        """

    def debug(self, message: str) -> None:
        """
        Logs a debug message, useful for development and troubleshooting purposes.

        :param message: The debug message to log, typically containing detailed internal state information.
        :return: None
        """

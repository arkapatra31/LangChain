import functools
import logging
import time
from datetime import datetime
import cProfile
import pstats
import io
import sys
from logging import Logger
from io import StringIO


def logger(log_file='execution.log', log_level=logging.INFO, profile=False, nested_info=False):
    """
    @author: arkapatra@deloitte.com\n
    A decorator factory that returns a configurable decorator that logs function execution details
    with timestamp in DD-MM-YYYY HH:MM:SS:MS format, optional profiling,
    and optional nested function call tracking.
    :param log_file: Path to the log file (default: 'execution.log').
    :param log_level: Logging level (default: logging.INFO).
    :param profile: If True, profile the function execution (default: False).
    :param nested_info: If True, track nested function calls along with explicit print/log statements (default: False).
    Usage:
        - Default usage: @logger()
        - Custom log file: @logger(log_file='custom.log')
        - Change log level: @logger(log_level=logging.DEBUG)
        - Enable profiling: @logger(profile=True)
        - Enable nested function call tracking: @logger(nested_info=True)
    Important Note:
        - For deeper profiling, consider using the `profile` parameter as True along with log_level set to DEBUG.
    """

    def decorator(func):
        # Create a custom formatter with millisecond precision
        class CustomFormatter(logging.Formatter):
            def formatTime(self, record, datefmt=None):
                dt = datetime.fromtimestamp(record.created)
                return dt.strftime('%d-%m-%Y %H:%M:%S:%f')[:-3]  # Truncate to milliseconds

        # Custom stream to redirect print statements to logger when nested_info=True
        class LoggerStream:
            def __init__(self, logger, level):
                self.logger = logger
                self.level = level
                self.buffer = ""

            def write(self, message):
                if message.strip():  # Only log non-empty messages
                    self.buffer += message
                    if "\n" in message:
                        self.flush()

            def flush(self):
                if self.buffer.strip():
                    self.logger.log(self.level, self.buffer.strip())
                    self.buffer = ""

        # Create a unique logger for this function
        func_logger: Logger = logging.getLogger(f"{func.__name__}_logger")
        func_logger.setLevel(log_level)

        func_logger.handlers.clear()
        handler = logging.FileHandler(log_file)
        formatter = CustomFormatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        func_logger.addHandler(handler)

        # Trace function to capture nested calls
        def trace_calls(frame, event, arg):
            if event != 'call':
                return
            code = frame.f_code
            func_name = code.co_name
            if func_name == 'wrapper' or func_name.startswith('<'):
                return
            func_logger.debug(f"Nested call to: {func_name}")
            return trace_calls

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()

            # Set up stream to capture print statements only if nested_info is True
            original_stdout = sys.stdout
            logger_stream = None
            if nested_info:
                logger_stream = LoggerStream(func_logger, logging.INFO)
                sys.stdout = logger_stream

            func_logger.info(f"Function '{func.__name__}' called")
            func_logger.info(f"Arguments: args={args}, kwargs={kwargs}")

            try:
                if nested_info:
                    sys.settrace(trace_calls)

                if profile:
                    profiler = cProfile.Profile()
                    result = profiler.runcall(func, *args, **kwargs)

                    stream = io.StringIO()
                    stats = pstats.Stats(profiler, stream=stream)
                    stats.sort_stats('cumulative')
                    stats.print_stats()

                    func_logger.info("Profiling statistics:")
                    func_logger.info(stream.getvalue())
                else:
                    result = func(*args, **kwargs)

                execution_time = time.time() - start_time

                func_logger.info(f"Function '{func.__name__}' completed successfully")
                func_logger.info(f"Return value: {result}")
                func_logger.info(f"Execution time: {execution_time:.4f} seconds")

                return result
            except Exception as e:
                func_logger.error(f"Function '{func.__name__}' failed with error: {str(e)}")
                raise
            finally:
                # Restore stdout and flush buffer only if nested_info was enabled
                if nested_info and logger_stream:
                    logger_stream.flush()
                    sys.stdout = original_stdout
                if nested_info:
                    sys.settrace(None)

        return wrapper

    return decorator


__all__ = [
    'logger'
]


# Example usage with bare decorator
@logger()
def default_function(x, y):
    time.sleep(0.1)  # Simulate some work
    print(f"Default: Adding {x} + {y}")
    return x + y


@logger(log_file='execution.log', profile=False, nested_info=True)
def outer_function(x, y):
    time.sleep(0.1)  # Simulate some work
    print(f"Starting calculation with x={x}, y={y}")

    def inner_function(a):
        time.sleep(0.05)
        logging.info(f"Inner function processing: {a}")  # Explicit logging
        print(f"Inner function doubling: {a}")
        return a * 2

    result = inner_function(x) + y
    print(f"Final result: {result}")
    return result


@logger(log_file='custom.log', log_level=logging.DEBUG, profile=True, nested_info=False)
def simple_calc(a, b):
    time.sleep(0.2)
    print(f"Explicit print: Calculating {a} * {b}")  # Goes to console
    logging.info(f"Explicit log: Processing {a} and {b}")  # Goes to console if configured
    return a * b


# Test it
if __name__ == "__main__":
    # Configure root logger to show explicit logging in console
    logging.basicConfig(level=logging.INFO)

    result0 = default_function(3, 4)
    print(f"Default function result: {result0}")  # This goes to console

    result1 = outer_function(4, 5)
    print(f"Outer function result: {result1}")  # This goes to console

    result2 = simple_calc(2, 3)
    print(f"Simple calc result: {result2}")  # This goes to console
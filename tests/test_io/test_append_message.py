"""
Test the function "append_a_little_message_to_a_file"
"""
import os
import pytest
import pathlib
import tempfile
from simple.io import append_a_little_message_to_a_file


if os.path.exists(NON_EXISTING_FILE_NAME := 'shadkjashjkdas.txt'):
    raise SyntaxError(f'Invalid test - File {NON_EXISTING_FILE_NAME} exists')


def test_non_existing_file() -> None:
    with pytest.raises(FileNotFoundError):
        append_a_little_message_to_a_file('hello', NON_EXISTING_FILE_NAME)


def test_with_text_path() -> None:
    message = "This is a message"

    with tempfile.TemporaryDirectory() as _tempdir:
        # Make a file with a little message
        with open(filepath := pathlib.Path(_tempdir, 'file.txt'), 'w') as wrapper:
            wrapper.write("Hello\n")
            wrapper.write("I am a temporary file\n")
            wrapper.write("I will be deleted later\n")

        # Append to temporary file
        append_a_little_message_to_a_file(message, filepath)

        # Check content of temporary file
        with open(filepath, 'r') as filewrapper:
            *lines, appended_message = filewrapper.readlines()

        assert len(lines) == 3, "Unexpected number of lines in temporary file"
        assert appended_message == message

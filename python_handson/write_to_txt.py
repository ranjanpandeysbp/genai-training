"""
Write data to a text file
"""

def write_to_file(filename, data):
    """
    Write data to file (overwrites existing content)
    
    Args:
        filename: Name of the file to write to
        data: Data to write (string or list of strings)
    """
    try:
        with open(filename, 'w') as file:
            if isinstance(data, str):
                file.write(data)
            elif isinstance(data, list):
                file.writelines(data)
        print(f"Successfully wrote data to {filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")


def append_to_file(filename, data):
    """
    Append data to file (adds to existing content)
    
    Args:
        filename: Name of the file to append to
        data: Data to append (string or list of strings)
    """
    try:
        with open(filename, 'a') as file:
            if isinstance(data, str):
                file.write(data)
            elif isinstance(data, list):
                file.writelines(data)
        print(f"Successfully appended data to {filename}")
    except Exception as e:
        print(f"Error appending to file: {e}")


def write_line_by_line(filename, lines):
    """
    Write multiple lines to file
    
    Args:
        filename: Name of the file to write to
        lines: List of strings to write as separate lines
    """
    try:
        with open(filename, 'w') as file:
            for line in lines:
                # Add newline if not already present
                if not line.endswith('\n'):
                    file.write(line + '\n')
                else:
                    file.write(line)
        print(f"Successfully wrote {len(lines)} lines to {filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")


def append_line_by_line(filename, lines):
    """
    Append multiple lines to file
    
    Args:
        filename: Name of the file to append to
        lines: List of strings to append as separate lines
    """
    try:
        with open(filename, 'a') as file:
            for line in lines:
                # Add newline if not already present
                if not line.endswith('\n'):
                    file.write(line + '\n')
                else:
                    file.write(line)
        print(f"Successfully appended {len(lines)} lines to {filename}")
    except Exception as e:
        print(f"Error appending to file: {e}")


# Main execution
if __name__ == "__main__":
    filename = "data.txt"
    
    # Example 1: Write single string (overwrites)
    print("=== Writing single string ===")
    write_to_file(filename, "Hello, World!\nThis is a test file.\n")
    
    # Example 2: Append string
    print("\n=== Appending string ===")
    append_to_file(filename, "Appended line 1\nAppended line 2\n")
    
    # Example 3: Write multiple lines
    print("\n=== Writing multiple lines ===")
    lines_to_write = [
        "Line 1: This is the first line",
        "Line 2: This is the second line",
        "Line 3: This is the third line",
        "Line 4: This is the fourth line"
    ]
    write_line_by_line(filename, lines_to_write)
    
    # Example 4: Append multiple lines
    print("\n=== Appending multiple lines ===")
    lines_to_append = [
        "Appended Line 5",
        "Appended Line 6",
        "Appended Line 7"
    ]
    append_line_by_line(filename, lines_to_append)
    
    # Example 5: Write from user input
    print("\n=== Writing from user input ===")
    user_input = input("Enter text to write to file: ")
    append_to_file(filename, user_input + "\n")

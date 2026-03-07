"""
Read data from a text file
"""

def read_file_line_by_line(filename):
    """
    Read file line by line
    
    Args:
        filename: Name of the file to read
    """
    try:
        with open(filename, 'r') as file:
            print(f"Reading from {filename}:\n")
            for line_num, line in enumerate(file, 1):
                print(f"Line {line_num}: {line.rstrip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")


def read_file_as_list(filename):
    """
    Read entire file as a list of lines
    
    Args:
        filename: Name of the file to read
        
    Returns:
        List of lines from the file
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        print(f"\nFile content as list (total lines: {len(lines)}):")
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def read_file_entire(filename):
    """
    Read entire file as a single string
    
    Args:
        filename: Name of the file to read
        
    Returns:
        Entire file content as string
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"\nEntire file content:\n{content}")
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""


def read_file_specific_lines(filename, start_line, end_line):
    """
    Read specific lines from file
    
    Args:
        filename: Name of the file to read
        start_line: Starting line number (1-indexed)
        end_line: Ending line number (1-indexed)
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        print(f"\nLines {start_line} to {end_line}:")
        for i in range(start_line - 1, min(end_line, len(lines))):
            print(f"Line {i + 1}: {lines[i].rstrip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")


# Main execution
if __name__ == "__main__":
    filename = "data.txt"
    
    # Method 1: Read line by line
    read_file_line_by_line(filename)
    
    # Method 2: Read as list
    lines = read_file_as_list(filename)
    print(lines)
    
    # Method 3: Read entire file
    content = read_file_entire(filename)
    
    # Method 4: Read specific lines
    read_file_specific_lines(filename, 2, 4)

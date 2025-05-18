 def write_file(file_name, file_content):
    """
    Writes content to a .txt file
    Args:
        file_name (str): name/path of file (without extension)
        file_content (str): content to write to file
    """
    with open(f"{file_name}.txt", mode='w', encoding='utf-8') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """
    Appends content to an existing .txt file
    Args:
        file_name (str): name/path of file (without extension)
        append_content (str): content to append to file
    """
    with open(f"{file_name}.txt", mode='a', encoding='utf-8') as file:
        file.write(append_content)

def read_file(file_name):
    """
    Reads content from a .txt file
    Args:
        file_name (str): name/path of file (without extension)
    Returns:
        str: content of the file
    """
    with open(f"{file_name}.txt", encoding='utf-8') as file:
        return file.read()

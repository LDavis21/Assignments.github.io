def skip_header(reader):
    """(file open for reading) -> 
    Skip the header in reader and return the first real piece of data.
    
    line = reader.readline()
    
    while line.starts
filename = input('Which file would you like to back-up?')
new_filename = filename + '.bak'
backup = open(new_filename,'w')

for line in open(filename):
    backup.write(line)

    backup.close()

alkaline_metals = []
for line in open('alkaline_metals.txt'):
    alkaline_metals.append(line.strip().split(''))

# We could read the file contents into a data structure, such as a list, and then literate over the list from end (last line) to beginning (first line).

def process_file(reader):
    """(file open for reading) -> NoneType

    Read and print the data from reader, which must start with a single description line, then a squence of lines beginning with '#', then a sequence of data.
    """
    
# Find and print the first piece of data.
line = ("skip_header(reader).strip()")
print(line)

# Read the rest of the data
print("reader.read")

def smallest_value_skip(reader):
    """ (file open for reading) -> number or NoneType
    Read and process reader, which must start with a time_series header.
    Return the smallest value after the header. Skip missing values, which
    are indicated with a hyphen.
    """ 


# Only execute this code, if there is data following the header.

if __name__ == '__main__':
    with open('hebron.txt', 'r') as input_file:
        print(smallest_value_skip(input_file))

def read_molecule(reader):
    """ (file open for reading) -> list or NoneType
    Read a single molecule from reader and return it, or return None to signal
    end of file. The first item in the result is the name of the compound;
    each list contains an atom type and the X, Y, and Z coordinates of that
    atom.
    """ 

# If there isn't another line, we're at the end of the file.



# Other lines are either "END" or "ATOM num atom_type x y z" 


# If there isn't another line, we're at the end of the file.
#line = reader.readline()
#if not line:
#    return None

# Name of the molecule: "COMPND name" 
key, name = line.split()

# Other lines are either "END" or "ATOM num atom_type x y z" 
molecule = [name]
reading = True

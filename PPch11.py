def find_dups(L):
    """(list) -> set

    Return the number of dublicates numbers from L.
    
    find_dups([1, 1, 2, 3, 4, 2,])
    {1, 2}

    find_dups9[1, 2, 4,])
    set()
    """

elem_set = set()
dups_set = set()
for entry in 'L':
    len_initial = len(elem_set)
    elem_set.add(entry)
    len_after = len(elem_set)
    if len_initial == len_after:
        dups_set.add(entry)
    print("L")

def mating_pairs(males, females):
    """(set, set) -> set of tuple

    Return a set of tuples where each tuple contain a male from males and female from females.

    mating_pairs({'Anne', 'Beatrice', 'Cari'}, {'Ali', 'Bob', 'Chen'})
    {('Cari', 'Chen'), ('Beatrice', 'Bob'), ('Anne', 'Ali')
    """

pairs = set()
num_gerbils = len()


def get_authors(filenames):\
    """(list of str) -> set of str
    Return a list of the authors in PDB files names appear in filenames.
    """ 

authors = set()

for filename in filename:
    pdb_file = open(filename)
    for line in pdb_file:
        if line.lower().startswith('author'):
            author = line[6:].strip()
            authors.add(author)
        
def count_values(dictionary):
    """ (dict) -> int
    Return the number of unique values in dictionary.
    
    count_values({'red': 1, 'green': 2, 'blue': 2})
    2
    """ 
    return len(set(dictionary.values()))

def least_likely(particle_to_probability):
    """ (dict of {str: float}) -> str
    Return the particle from particle_to_probability with the lowest probablity.
    
    least_likely({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07})
    'meson'
    """ 


def count_duplicates(dictionary):
    """ (dic) -> int
    Return the number of duplicate values in dictionary.
    
    count_duplicates({'R': 1, 'G': 2, 'B': 2, 'Y': 1, 'P': 3})
    2
    """ 

def is_balanced(color_to_factor):
    """ (dict of {str: float}) -> bool
    Return True if and only if color_to_factor represents a balanced color.
    
    is_balanced({'R': 0.5, 'G': 0.4, 'B': 0.7})
    False
    
    is_balanced({'R': 0.3, 'G': 0.5, 'B': 0.2})
    True
    """
    values = list(color_to_factor.values())
    total = sum(values)
    return total == 1.0

def dict_interest(dict1, dict2):
    """ (dict, dict) -> dict
    Return a new dictionary that contains only the key/value pairs that occur
    in both dict1 and dict2.
    
    dict_interest({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'd': 2, 'b': 2})
    {'a': 1, 'b': 2}
    """ 
    intersection = {}
    for (key, value) in dict1.items():
        if key in dict2 and value == dict2[key]:
            intersection[key] = value
            return intersection
        
def db_headings(dict_of_dict):
    """ (dict of dict) -> set
    Return a set of the keys in the inner dictionaries in dict_of_dict.
    db_headings({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
    {1, 2, 3}
    """ 
    inner_keys = set()
    for key in dict_of_dict:
        for inner_key in dict_of_dict[key]:
            inner_keys.add(inner_key)
            return inner_keys


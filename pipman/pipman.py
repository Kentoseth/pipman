import pip
import argh
import collections
from colorama import Fore, Back, Style, init


##### START - Area for CLI options #####

# Listing all packages with subpackages
def listall():
    '''
    Show all packages and their nested dependencies.
    RED = package is a dependency in >1 other packages AND has its own dependencies
    MAGENTA/PURPLE = package has its own dependencies
    GREEN = package is a dependency in >1 other package
    '''
    
    init(autoreset=True) #for colorama to reset colours
    
    
    pip_list = pip.get_installed_distributions()
    
    for loop in reversed(range(len(pip_list))): #had to reverse input to get contents to display as abcd... instead of zyxw...
    
        print("- " + pip_list[loop].key)
        
        y = pip_list[loop].requires()
        
        if len(y) != 0:
            for sub_loop in range(len(y)):
            
                # print RED if a package is a dependency in >1 other packages AND has its own dependencies
                if has_own_subpackages(y[sub_loop].key) == True and multi_sub(y[sub_loop].key) == True:
                    print(Fore.RED + "  - " + y[sub_loop].key)
                    
                # print PURPLE if a package has its own dependencies    
                elif has_own_subpackages(y[sub_loop].key) == True:
                    print(Fore.MAGENTA + "  - " + y[sub_loop].key)
                    
                # print GREEN if a package is a dependency in >1 other package    
                elif multi_sub(y[sub_loop].key) == True:
                    print(Fore.GREEN + "  - " + y[sub_loop].key)
                    
                else:
                    print("  - " + y[sub_loop].key)
                    

# Provides the equivalent of `pip freeze` without redundant packages                    
def freeze():
    '''
    Equivalent to `pip freeze`, but removes any nested packages and
    automatically creates a requirements.txt file in the directory
    the command is issued in
    '''
    
    x = pip.get_installed_distributions()
    
    y = []
        
    for loop in reversed(range(len(x))):
    
        y.append(x[loop].key)
        
    
    #####
        
    for loop in reversed(range(len(x))):
        
        item = x[loop].key
        
        if is_sub(item) == True:
            # print(item)
            y.remove(item)
            
    
    with open('requirements.txt','w') as f:
        
        for item in y:
            
            for loop in reversed(range(len(x))):
        
                if item == x[loop].key:
                    
                    f.write(x[loop].key + "==" + x[loop].version + '\n')


'''
# test code to test colorama functionality    
def test():
    "Testing colorama features"
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')
'''    
    
##### END #####

# Regular functions below

# checks for a package that has its own subpackages
def has_own_subpackages(pkg):

    x = pip.get_installed_distributions()

    for loop in range(len(x)):
        if pkg == x[loop].key:
            if len(x[loop].requires()) != 0:
                return True
            else:
                return False
                
# checks for a subpackage that exists in >1 package
def multi_sub(pkg):

    x = pip.get_installed_distributions()
    
    counter = 0

    for loop in range(len(x)):
        y = x[loop].requires()
        
        if len(y) != 0:
            for sub_loop in range(len(y)):
                if pkg == y[sub_loop].key:
                    counter += 1
                    
    if counter > 1:
        return True
        
    else:
        return False        
     
# checks if a package is a subpackage
def is_sub(pkg):

    x = pip.get_installed_distributions()
    
    for loop in reversed(range(len(x))):
        
        y = x[loop].requires()
        
        if len(y) != 0:
            for sub_loop in range(len(y)):
                if pkg == y[sub_loop].key:
                    # print(y)
                    # print(y[sub_loop].key)
                    return True
            
'''
for loop in range(len(x)):
    if y[0].key == x[loop].key:
        print(x[loop].key)
        
    else:
        print("not found")

# x[loop].key

# y = x[8].requires()
'''

# assembling:

parser = argh.ArghParser()
parser.add_commands([listall, freeze])

# dispatching:

if __name__ == '__main__':
    parser.dispatch()



from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from random import choice, shuffle
from const import *  
from charset import CharSet

def passwd_gen( length, charsets ):
    min_length = len(charsets)
    if min_length <= 0 :
        raise ValueError("No charset used")
    if length < min_length:
        raise ValueError(f"Length must be greater than {min_length}")
    
    requirements = []
    full_set = CharSet()
    
    for charset in charsets: 
        requirements.append(choice(charset))
        full_set.extend( charset )
        
    required_length = length - len( requirements )
    requirements += [ choice( full_set ) for _ in range( required_length ) ]
    
    shuffle( requirements )
    passwd = ''.join( requirements )
    return passwd 
    
    


if __name__ == '__main__':
    parser = ArgumentParser(
        prog= PROGRAM_NAME,
        formatter_class=ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument('--length', '-L', type=int, default=DEFAULT_LENGTH, help=HELP_LENGTH)
    
    for arg_name, (charset, default, help_str) in ARGS_CHARSET_CONFIG.items():
        parser.add_argument(f'--{arg_name}', action='store_true', default=default, help=help_str)
    
    parser.add_argument('--symbols-list',type=str,default=DEFAULT_SYMBOLS_LIST,help=HELP_SYMBOLS_LIST)
    
    args = parser.parse_args()
    
    print(f"[INFO] Génération d’un mot de passe avec longueur = {args.length}")
    print(f"[INFO] Paramètres activés", end = ' : ')
    [print(value) for arg_name in ARGS_CHARSET_CONFIG if (value := getattr(args, arg_name))]

    if args.symbols:
        print(f"[INFO] Liste de symboles personnalisée utilisée : {args.symbols_list}")
    
    charsets = [ charset for arg_name, (charset, default, help_str) in ARGS_CHARSET_CONFIG.items() if getattr(args, arg_name) and charset ]
    
    if args.symbols :  charsets.append( CharSet( args.symbols_list ) )
    
    print(f"[INFO] Liste des symboles utilisés : {''.join(''.join(cs) for cs in charsets)}")    
    passwd = passwd_gen(args.length, charsets)
    print(f"[RESULT] Mot de passe généré : {passwd}")
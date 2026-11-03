# Menggunakan import nama_modul
import book_functions

book_functions.favorite_book("The Little Prince")

# Menggunakan from nama_modul import nama_fungsi
from book_functions import favorite_book

favorite_book("The Little Prince")

# Menggunakan from nama_modul import nama_fungsi as fn
from book_functions import favorite_book as fb

fb("The Little Prince")

# Menggunakan import nama_modul as mn
import book_functions as bf

bf.favorite_book("The Little Prince")

# Menggunakan from nama_modul import
from book_functions import *

favorite_book("The Little Prince")
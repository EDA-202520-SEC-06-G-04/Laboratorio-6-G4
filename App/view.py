"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones
 *
 * Dario Correal
 """

import sys
import App.logic as logic
import tracemalloc
import App.logic as logic
 
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_separate_chaining as sp
from DataStructures.List import array_list as al


"""
La vista se encarga de la interacción con el usuario.
Presenta el menú de opciones y por cada selección se hace la solicitud
al controlador para ejecutar la operación solicitada.
"""

# -------------------------------------------------------------
# Funciones para la carga de datos
# -------------------------------------------------------------

def new_logic():
    """
    Crea una instancia del controlador.
    """
    control = logic.new_logic()
    return control


# Incluir medición de tiempo y memoria
def load_data(control):
    """
    Solicita al controlador que cargue los datos y mide tiempo y memoria.
    """
    start_time = logic.getTime()
    tracemalloc.start()
    start_memory = logic.getMemory()

    books, authors, tags, book_tags = logic.load_data(control)

    stop_memory = logic.getMemory()
    end_time = logic.getTime()
    delta_t = logic.deltaTime(end_time, start_time)
    delta_m = logic.deltaMemory(start_memory, stop_memory)

    print(f"\nTiempo de carga: {delta_t:.2f} ms")
    print(f"Memoria utilizada: {delta_m:.2f} kB\n")

    return books, authors, tags, book_tags


# -------------------------------------------------------------
# Funciones para la correcta impresión de los datos
# -------------------------------------------------------------

def print_menu():
    """
    Menú de usuario.
    """
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar la información de un libro según su id")
    print("3- Consultar los libros de un autor")
    print("4- Consultar los libros según un género dado")
    print("5- Consultar los libros de un autor para un año de publicación específico")
    print("8- Salir")


def print_book_info(book):
    """
    Imprime la información de un libro.
    """
    if book:
        print('Titulo: ' + book['title'] + '  ISBN: ' +
              book['isbn'] + ' Rating: ' + book['average_rating'] +
              ' Work text reviews count : ' + book['work_text_reviews_count'])
    else:
        print('No se encontraron libros')


def print_books_by_author(author, books_by_author):
    """
    Imprime los libros de un autor.
    """
    if books_by_author:
        print(f"Para el autor {author} se encontraron los siguientes libros:")
        for book_pos in range(0, al.size(books_by_author)):
            book = al.get_element(books_by_author, book_pos)
            print('Titulo: ' + book['title'] + '  ISBN: ' +
                  book['isbn'] + ' Rating: ' + book['average_rating'] +
                  ' Work text reviews count : ' + book['work_text_reviews_count'])
    else:
        print("No se encontró el autor")


def print_books_by_tag(tag_name, books_by_tag):
    """
    Imprime los libros asociados a un tag.
    """
    if books_by_tag:
        print("Tag encontrado: " + tag_name)
        for book_pos in range(0, al.size(books_by_tag)):
            book = al.get_element(books_by_tag, book_pos)
            print('Titulo: ' + book['title'] + '  ISBN: ' +
                  book['isbn'] + ' Rating: ' + book['average_rating'] +
                  ' Work text reviews count : ' + book['work_text_reviews_count'])
    else:
        print("No se encontró el tag")


def print_books_by_auth_year(author, pub_year, books_by_author_year, tiempo_transcurrido, memoria_usada):
    """
    Imprime los libros de un autor para un año de publicación específico
    junto con las métricas de rendimiento.
    """
    if books_by_author_year:
        print(f"Para el autor {author}, se encontraron los siguientes libros publicados en el año {pub_year}:")
        for book_pos in range(0, al.size(books_by_author_year)):
            book = al.get_element(books_by_author_year, book_pos)
            print(f"Titulo: {book['title']}  ISBN: {book['isbn']}  Rating: {book['average_rating']}  "
                  f"Work text reviews count: {book['work_text_reviews_count']}")
    else:
        print("No se encontró el autor o el año especificado.")

    print(f"\nTiempo transcurrido: {tiempo_transcurrido:.2f} ms")
    print(f"Memoria utilizada: {memoria_usada:.2f} kB\n")


exit_opt_lt = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")


# -------------------------------------------------------------
# Menú principal
# -------------------------------------------------------------

def main():
    """
    Menú principal de la aplicación.
    """
    working = True
    control = new_logic()

    while working:
        print_menu()
        inputs = input("Seleccione una opción para continuar\n")

        if int(inputs[0]) == 1:
            print("Cargando información de los archivos ....")
            bk, at, tg, bktg = load_data(control)
            print('Libros cargados: ' + str(bk))
            print('Autores cargados: ' + str(at))
            print('Géneros cargados: ' + str(tg))
            print('Asociación de Géneros a Libros cargados: ' + str(bktg))

        elif int(inputs[0]) == 2:
            number = input("Ingrese el id del libro (good_read_book_id): ")
            book = logic.get_book_info_by_book_id(control, number)
            print_book_info(book)

        elif int(inputs[0]) == 3:
            authorname = input("Nombre del autor a buscar: ")
            books_by_author = logic.get_books_by_author(control, authorname)
            print_books_by_author(authorname, books_by_author)

        elif int(inputs[0]) == 4:
            label = input("Etiqueta (tag) a buscar: ")
            books_by_tag = logic.get_books_by_tag(control, label)
            print_books_by_tag(label, books_by_tag)

        elif int(inputs[0]) == 5:
            author_name = input("Ingrese el nombre del autor:\n")
            pub_year = input("Ingrese el año de publicación:\n")
            books_by_author_pub_year, tiempo, memoria = logic.get_books_by_author_pub_year(control, author_name, pub_year)
            print_books_by_auth_year(author_name, pub_year, books_by_author_pub_year, tiempo, memoria)

        elif int(inputs[0]) == 8:
            opt_usr = input("¿Desea salir del programa? (s/n): ")
            if opt_usr in exit_opt_lt:
                working = False
                print("\nGracias por utilizar el programa.")
        else:
            continue
    sys.exit(0)
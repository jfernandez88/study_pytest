import pytest
import logging

def test_parametria_A(supply_parametria):
    texto = supply_parametria
    print("INFO: ")
    print(texto)

def test_parametria_B(supply_sql):
    cursor = supply_sql.fetchone()
    print("\n LISTA: ")
    for row in cursor:
        print(" "+row)

    print("NumFondo: "+cursor[0])    
    print("Nombre: "+cursor[1]) 

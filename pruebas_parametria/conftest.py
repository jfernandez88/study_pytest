import pytest
import pyodbc


@pytest.fixture
def supply_parametria():
	aa= 10
	bb= 20
	cc= 30
	return [aa,bb,cc]

@pytest.fixture
def supply_sql():
	conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=V21SERVER21\V21SERVER21_CSAS;'
                      'Database=vfQAUI_07_00_12;'
                      'Trusted_Connection=yes;'
					  'UID=QAUserAutomation;'
					  'PWD=vesco;')

	cursor = conn.cursor()
	cursor.execute('SELECT TOP 1 CodInterfaz, Nombre FROM FONDOS')
	
	return cursor
from employee import Employee

def test_give_default_raise():
    """Menguji bahwa kenaikan gaji default menambahkan $5.000."""
    employee = Employee("Jane", "Doe", 50000)
    employee.give_raise()
    assert employee.annual_salary == 55000

def test_give_custom_raise():
    """Menguji bahwa kenaikan gaji kustom menambahkan jumlah yang ditentukan."""
    employee = Employee("John", "Smith", 60000)
    employee.give_raise(10000)
    assert employee.annual_salary == 70000
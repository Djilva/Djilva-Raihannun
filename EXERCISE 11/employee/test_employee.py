import pytest
from employee import Employee

@pytest.fixture
def general_employee():
    """Fixture untuk menyediakan sampel pegawai secara otomatis."""
    return Employee("Jane", "Doe", 50000)

def test_give_default_raise(general_employee):
    """Menguji kenaikan gaji default menggunakan fixture."""
    general_employee.give_raise()
    assert general_employee.annual_salary == 55000

def test_give_custom_raise(general_employee):
    """Menguji kenaikan gaji kustom menggunakan fixture."""
    general_employee.give_raise(10000)
    assert general_employee.annual_salary == 60000
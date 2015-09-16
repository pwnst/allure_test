import pytest
import allure
import os
import sys
from hamcrest import *
from custom import *

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

from app.calc import Calc

@pytest.allure.feature("Calculate Integers")
@pytest.allure.story('Implement Integer Calculations')
@pytest.allure.issue("https://jira.cogniance.com/browse/STP-71")
@pytest.allure.testcase("https://jira.cogniance.com/browse/STP-71")
@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
class TestCalcInt(object):
	def setup_class(self):
		self.calc  = Calc()

	@pytest.allure.step("Adding Int")
	def test_adding_int(self):
		self.calc.new_calculation(2)
		self.calc.add(2)
		assert_that(self.calc.value, equal_to(4))
	
	@pytest.allure.step("Subsraction Int")
	def test_subtract_int(self):
		self.calc.new_calculation(4)
		self.calc.subtract(2)
		assert_that(self.calc.value, equal_to(2))

	@pytest.allure.step("Multiplication Int")
	def test_multiply_int(self):
		self.calc.new_calculation(4)
		self.calc.multiply(2)
		assert_that(self.calc.value, equal_to(9))

	@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
	@pytest.allure.step("Division Int")
	def test_division_int(self):
		self.calc.new_calculation(4)
		self.calc.divide(2)
		assert_that(self.calc.value, equal_to(2))


@pytest.allure.feature("Calculate Floats")
@pytest.allure.story('Implement Float Calculations')
@pytest.allure.issue("https://jira.cogniance.com/browse/STP-71")
@pytest.allure.testcase("https://jira.cogniance.com/browse/STP-71")
class TestCalcFloat(object):
	def setup_class(self):
		self.calc  = Calc()

	@pytest.allure.step("Adding Float")
	def test_adding_float(self):
		self.calc.new_calculation(0.4)
		self.calc.add(0.4)
		assert self.calc.value == 0.8
	
	@pytest.allure.step("Subsraction Float")
	def test_subtract_float(self):
		self.calc.new_calculation(0.4)
		self.calc.subtract(0.4)
		assert self.calc.value == 0

	@pytest.allure.step("Multiplication Float")
	def test_multiply_float(self):
		self.calc.new_calculation(0.2)
		self.calc.multiply(1.2)
		assert self.calc.value == 0.24

	@pytest.allure.severity(pytest.allure.severity_level.MINOR)
	@pytest.allure.step("Division Float")
	def test_division_float(self):
		self.calc.new_calculation(0.4)
		self.calc.divide(0.2)
		assert self.calc.value == 2.0


@pytest.allure.feature("History of Calculations")
@pytest.allure.story('Add History Support')
@pytest.allure.issue("https://jira.cogniance.com/browse/STP-71")
@pytest.allure.testcase("https://jira.cogniance.com/browse/STP-71")
@pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
class TestCalcHistory(object):
	def setup_class(self):
		self.calc  = Calc()

	@pytest.allure.step("History basic flow")
	def test_adding_float(self):
		self.calc.new_calculation(4)
		self.calc.add(24)
		self.calc.subtract(12)
		self.calc.multiply(3)
		self.calc.divide(2)
		assert str(self.calc) == "4 + 24 - 12 * 3 / 2 = 24"
		assert_that(str(self.calc), has_length(24))
	
	@pytest.allure.step("Clear History")
	def test_clear_history(self):
		self.calc.new_calculation(4)
		self.calc.add(24)
		self.calc.subtract(12)
		self.calc.multiply(3)
		self.calc.divide(2)
		self.calc.clear()
		assert_that(str(self.calc), is_("0"))

	@pytest.allure.step("All Operations in History")
	def test_all_operations_in_history(self):
		self.calc.new_calculation(4)
		self.calc.add(24)
		self.calc.subtract(12)
		self.calc.multiply(3)
		self.calc.divide(2)
		assert_that(str(self.calc), is_(all_operations()))

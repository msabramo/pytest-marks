import pytest
import marks

print("*** Invoking pytest... ***")
pytest.main(args=['test_pytest_marks.py'], plugins=[marks.MarksDecorator()])
print("*** Done ***")

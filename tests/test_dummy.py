import pytest

@pytest.mark.usefixtures("init_driver")
class TestDummy():

    def test_dummy_func(self):
        self.driver.get("http://localhost:9999/testsite/")
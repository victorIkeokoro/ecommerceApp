import pytest
def pytest_configure(config):
    config._metadata['Project Name']="ecommerce app"
    config._metadata['Module Name'] = "Test cases"
    config._metadata['Tester Name'] = "Victor"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME",None)
    metadata.pop("Plugins", None)


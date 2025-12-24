import pytest

def test_with_description_doc_strings(rp_logger):
    """
    This test checks if the description in the report portal is picked from doc strings.
    """
    rp_logger.info("Starting the test to verify doc string description in report portal")
    assert True

import pytest

@pytest.mark.issue(issue_id="1", reason="Payment flow", issue_type="bug")
def test_with_issue_info(rp_logger):
    """
    This test checks if issue information is correctly associated with the test in the report portal.
    """
    rp_logger.info("Starting the test to verify issue information in report portal")
    assert False
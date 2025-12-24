import logging
import pytest

logger = logging.getLogger(__name__)

@pytest.mark.issue(issue_id="1", reason="Payment flow", issue_type="bug")
def test_with_issue_info():
    """
    This test checks the payment flow functionality.
    It logs the start of the payment process and asserts that the process completes successfully.
    :return:
    """
    logger.info("Starting payment flow")
    assert False
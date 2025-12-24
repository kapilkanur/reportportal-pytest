import logging
import pytest

logger = logging.getLogger(__name__)

@pytest.mark.custom_marker
def test_with_description():
    """
    This test checks the payment flow functionality.
    It logs the start of the payment process and asserts that the process completes successfully.
    :return:
    """
    logger.info("Starting payment flow")
    assert True

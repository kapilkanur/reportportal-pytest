import logging
import pytest

logger = logging.getLogger(__name__)


@pytest.mark.custom_marker
def test_with_log_files():
    """
    This test checks if we can attach a file in the report portal or not.
    """
    logger.info("Attaching a sample file to the report",
                attachment={
                    "name": "sample.txt",
                    "data": "Sample file content for attachment.",
                    "mime": "text/plain"
                },
                )
    assert True
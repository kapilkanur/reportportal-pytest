import pytest


def test_with_attaching_log_files(rp_logger):
    """
    This test checks if we can attach a file in the report portal or not.
    """
    rp_logger.info("Attaching a sample file to the report",
                attachment={
                    "name": "sample.txt",
                    "data": "Sample file content for attachment.",
                    "mime": "text/plain"
                },
                )
    assert True
import logging

logger = logging.getLogger(__name__)

def test_payment_success():
    logger.info("Starting payment flow")
    assert True

def test_payment_failure():
    logger.error("Payment failed due to timeout")
    assert False

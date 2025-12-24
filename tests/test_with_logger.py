def test_payment_success(rp_logger):
    rp_logger.info("Starting payment flow")
    assert True

def test_payment_failure(rp_logger):
    rp_logger.error("Payment failed due to timeout")
    assert False

from thetaqueue import enqueue


def test_run():
    assert isinstance(enqueue.run(), list)

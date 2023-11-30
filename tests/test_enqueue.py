from thetaqueue import enqueue


def test_run():
    assert enqueue.run() == ["test"]

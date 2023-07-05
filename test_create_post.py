from DZ45.preparing_for_test import response_data


def test_post_success():
    if response_data:
        assert response_data
    else:
        assert AssertionError
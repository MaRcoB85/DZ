def skip(condition, reason=''):
    def param_cond(func):
        def wrapper(*args, **kwargs):
            if condition is True:
                return reason
            else:
                return func(*args, **kwargs)
        return wrapper
    return param_cond


@skip(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
    assert 2 + 2 == 5


print(test_two_plus_two())

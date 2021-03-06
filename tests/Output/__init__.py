import pytest
from analyzer.config import LATE_MERGING, SKIP_FAILING_TESTS, SLOW_BUILD, BROKEN_RELEASE


@pytest.fixture(scope='module')
def antipattern_data_hd():
    """
    Happy day antipattern data
    :return: happy day antipattern data
    """
    return {
        LATE_MERGING: {},
        SKIP_FAILING_TESTS: {},
        SLOW_BUILD: {},
        BROKEN_RELEASE: {}
    }


@pytest.fixture(scope='module')
def late_merging_data_hd(antipattern_data_hd):
    antipattern_data_hd[LATE_MERGING] = {
        'missed activity': {
            'branch1': 0,
            'branch2': 58748,
            'branch3': -1,
            'branch4': 1,
            'branch5': -20
        },
        'branch deviation': {
            'branch1': 0,
            'branch2': 20,
            'branch3': 30,
            'branch4': 5,
            'branch5': 1000
        },
        'unsynced activity': {
            'branch1': 0,
            'branch2': 20,
            'branch3': 30,
            'branch4': 5,
            'branch5': 1000
        },
        'classification': {
            'missed activity': {
                'medium_severity': ['branch5'],
                'high_severity': ['branch2']
            },
            'branch deviation': {
                'medium_severity': ['branch5'],
                'high_severity': ['branch2']
            },
            'unsynced activity': {
                'medium_severity': ['branch5'],
                'high_severity': ['branch2']
            }
        }
    }
    return antipattern_data_hd


@pytest.fixture(scope='module')
def slow_build_hd(antipattern_data_hd):
    antipattern_data_hd[SLOW_BUILD] = {
        'wf1': {
            'data': {
                "2021-03-17T20:05:17Z": 54879.0,
                "2022-03-17T20:05:17Z": 17.0,
                None: -1
            },
            'tool': "some_tool",
            'total avg': 50
        },
        'wf2': {
            'data': {
                "2021-03-17T20:05:17Z": 54879.0,
                "2022-03-17T20:05:17Z": 17.0,
            },
            'tool': "some_other_tool",
            'total avg': 50
        }
    }
    return antipattern_data_hd


@pytest.fixture(scope='module')
def broken_release_hd(antipattern_data_hd):
    antipattern_data_hd[BROKEN_RELEASE] = {
        'wf1': {
            'data': [
                {
                    'started_at': "2021-03-17T20:05:17Z"
                },
                {
                    'started_at': "2021-03-17T20:05:45Z"
                }
            ],
            'tool': 'some_tool'
        },
        'wf2': {
            'data': [
                {
                    'started_at': "2021-03-17T20:05:17Z"
                },
                {
                    'started_at': "2021-03-17T20:05:45Z"
                }
            ],
            'tool': 'some_tool'
        },
        'wf3': {'not-correct': True}
    }
    return antipattern_data_hd


@pytest.fixture(scope='module')
def late_merging_data_some_missing(late_merging_data_hd):
    del late_merging_data_hd[LATE_MERGING]['classification']
    del late_merging_data_hd[LATE_MERGING]['branch deviation']
    return late_merging_data_hd

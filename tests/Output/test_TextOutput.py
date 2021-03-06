import pytest
import os
import shutil
from analyzer.Output.TextOutput import TextOutput
from tests.Output import antipattern_data_hd, late_merging_data_hd, late_merging_data_some_missing


_ = (antipattern_data_hd, late_merging_data_hd, late_merging_data_some_missing)


@pytest.fixture(scope='module')
def res_dir(data_dir):
    return os.path.join(data_dir, 'Output')


def test_constructor(antipattern_data_hd):
    t_out = TextOutput(
        antipattern_data_hd,
        'some/repo-path',
        out_path='./some_output'
    )
    assert t_out.data == antipattern_data_hd
    path = os.path.join('./some_output', 'some-repo-path')
    assert t_out.out_path == path

    assert os.path.exists(path)

    # Test cleanup
    os.removedirs(path)
    assert not os.path.exists(path)


def test_create_late_merging(late_merging_data_hd, res_dir):
    t_out = TextOutput(
        late_merging_data_hd,
        'some/repo-path',
        out_path='./some_output'
    )

    t_out.create_late_merging()

    assert os.path.exists(f'{t_out.out_path}/summary_late_merging.txt')

    with open(f'{t_out.out_path}/summary_late_merging.txt') as gen_f:
        with open(f'{res_dir}/summary_late_merging_ref.txt') as ref_f:
            assert gen_f.readlines() == ref_f.readlines()

    shutil.rmtree('./some_output')
    assert not os.path.exists(f'{t_out.out_path}/summary_late_merging.txt')


def test_create_late_merging_some_missing(late_merging_data_some_missing, res_dir):
    t_out = TextOutput(
        late_merging_data_some_missing,
        'some/repo-path',
        out_path='./some_output'
    )

    t_out.create_late_merging()

    assert os.path.exists(f'{t_out.out_path}/summary_late_merging.txt')

    with open(f'{t_out.out_path}/summary_late_merging.txt') as gen_f:
        with open(f'{res_dir}/summary_late_merging_ref2.txt') as ref_f:
            assert gen_f.readlines() == ref_f.readlines()

    shutil.rmtree('./some_output')
    assert not os.path.exists(f'{t_out.out_path}/summary_late_merging.txt')


def test_create_slow_build():
    t_out = TextOutput(
        {},
        'some/repo-path',
        out_path='./some_output'
    )
    t_out.create_slow_build()
    # TODO: implement function further if required


def test_create_skip_failing_tests():
    t_out = TextOutput(
        {},
        'some/repo-path',
        out_path='./some_output'
    )
    t_out.create_skip_failing_tests()
    # TODO: implement function further if required


def test_create_broken_release():
    t_out = TextOutput(
        {},
        'some/repo-path',
        out_path='./some_output'
    )
    t_out.create_broken_release()
    # TODO: implement function further if required

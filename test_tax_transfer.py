import pytest
from pandas import DataFrame
from pandas.testing import assert_frame_equal
from tax_transfer import kindergeld


# =============================================================================
# test kindergeld
# =============================================================================


def child_benefit_standard_df():
    cols = ['tu_id', 'age', 'w_hours', 'ineducation', 'm_wage']
    data = [[1, 45, 40, False, 3000],
            [1, 40, 0, False, 0],
            [1, 24, 30, True, 700],
            [1, 18, 0, True, 200],
            [1, 17, 2, True, 0],
            [1, 15, 0, True, 0]]

    df = DataFrame(columns=cols, data=data)
    return df


def child_benefit_many_children_df():
    df = DataFrame()
    df['tu_id'] = [0] * 6
    df['age'] = [1, 2, 3, 4, 5, 6]
    df['ineducation'] = [True] * 6
    df['w_hours'] = [0] * 6
    df['m_wage'] = [0] * 6
    return df


def child_benefit_eligibility_conditions():
    cols = ['tu_id', 'age', 'w_hours', 'ineducation', 'm_wage']
    data = [[0, 50, 40, False, 0],
            [0, 12, 0, False, 0],
            [0, 14, 25, True, 800],
            [0, 15, 0, True, 300]]
    df = DataFrame(columns=cols, data=data)
    return df


to_test = [(child_benefit_standard_df(), 2011, 570),
           (child_benefit_standard_df(), 2002, 570),
           (child_benefit_many_children_df(), 2011, 1227),
           (child_benefit_many_children_df(), 2001, 1227),
           (child_benefit_eligibility_conditions(), 2013, 188),
           (child_benefit_eligibility_conditions(), 2000, 188)]


@pytest.mark.parametrize('df, yr, res', to_test)
def test_kindergeld(df, yr, res):
    tb = {'kgeld1': 188, 'kgeld2': 188, 'kgeld3': 194, 'kgeld4': 219,
          'kgage': 25, 'kgfreib': 7680}

    ref = None
    actual = kindergeld(df, tb, yr, ref)
    expected = df.copy(deep=True)
    expected['kindergeld_tu'] = res
    assert_frame_equal(actual, expected)
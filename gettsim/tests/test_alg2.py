import itertools

import pandas as pd
import pytest
import yaml
from pandas.testing import assert_series_equal

from gettsim.benefits.arbeitsl_geld_2 import alg2
from gettsim.config import ROOT_DIR
from gettsim.generic_functions import get_piecewise_parameters
from gettsim.policy_for_date import get_policies_for_date
from gettsim.policy_for_date import load_regrouped_data

INPUT_COLS = [
    "p_id",
    "hh_id",
    "tu_id",
    "vorstand_tu",
    "kind",
    "alter",
    "kaltmiete_m",
    "heizkost_m",
    "wohnfläche",
    "bewohnt_eigentum",
    "alleinerziehend",
    "bruttolohn_m",
    "ges_rente_m",
    "kapital_eink_m",
    "arbeitsl_geld_m",
    "sonstig_eink_m",
    "eink_selbstst_m",
    "vermiet_eink_m",
    "eink_st_m",
    "soli_st_m",
    "sozialv_beit_m",
    "kindergeld_m_hh",
    "unterhaltsvors_m",
    "elterngeld_m",
    "jahr",
]
OUT_COLS = [
    "sum_basis_arbeitsl_geld_2_eink",
    "sum_arbeitsl_geld_2_eink",
    "arbeitsl_geld_2_brutto_eink_hh",
    "mehrbed",
    "regelbedarf_m",
    "regelsatz_m",
    "kost_unterk_m",
    "unterhaltsvors_m_hh",
    "eink_anrechn_frei",
]


YEARS = [2019]


@pytest.fixture(scope="module")
def input_data():
    file_name = "test_dfs_alg2.csv"
    out = pd.read_csv(ROOT_DIR / "tests" / "test_data" / file_name)
    return out


@pytest.mark.parametrize("year, column", itertools.product(YEARS, OUT_COLS))
def test_alg2(input_data, arbeitsl_geld_2_raw_data, year, column):
    raw_group_data = yaml.safe_load(
        (ROOT_DIR / "data" / "arbeitsl_geld_2_neu.yaml").read_text()
    )
    year_data = input_data[input_data["jahr"] == year]
    df = year_data[INPUT_COLS].copy()

    arbeitsl_geld_2_params = get_policies_for_date(
        year=year, group="arbeitsl_geld_2", raw_group_data=arbeitsl_geld_2_raw_data
    )
    arbeitsl_geld_2_params_neu = load_regrouped_data(
        arbeitsl_geld_2_params["datum"],
        group="arbeitsl_geld_2",
        raw_group_data=raw_group_data,
    )
    # get_piecewise_parameters(arbeitsl_geld_2_params_neu["e_anr_frei"], "e_anr_frei")
    import pdb

    pdb.set_trace()
    df = df.reindex(columns=df.columns.tolist() + OUT_COLS)
    df = df.groupby("hh_id", group_keys=False).apply(
        alg2, params=arbeitsl_geld_2_params
    )

    assert_series_equal(df[column], year_data[column], check_dtype=False)

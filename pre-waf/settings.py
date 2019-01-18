# -*- coding: utf-8 -*-
"""
IZAMOD SETTINGS

get_settings: Global simulation settings
ubi_settings: set alternative tax benefit parameters for UBI
hypo_graph_settings: settings for hypothetical graphs
"""
import os
import socket


def get_settings():
    """ Initialize Global Settings
    """
    # Base year
    taxyear = 2019

    # The baseline scenario is always called RS`taxyear' (RS = Rechtsstand)
    reforms = ["RS" + str(taxyear), "UBI"]

    # DATA CREATION
    # load raw SOEP data and merge them into one data set
    load_data = 0
    # Minimum year to collect data from.
    minyear = 2005
    # prepare tax-ben input
    prepare_data = 0

    # prepare descriptive statistics
    show_descr = 0

    # TAX TRANSFER CALCULATION
    taxtrans = 1

    # Run Hypo file for debugging
    run_hypo = 0

    # PATH SETTINGS
    MAIN_PATH = os.getcwd() + "/"
    # SOEP_PATH: Where is the SOEP data stored?
    # Find out whether we are on the GPU.
    if socket.gethostname() == "gpu1":
        SOEP_PATH = "/data/shares/dynamod/data/raw/soep/"
    else:
        SOEP_PATH = "V:/soep/datasets/2016/v33.1/long/"
    # The Path for self produced data
    DATA_PATH = MAIN_PATH + "data/"
    GRAPH_PATH = MAIN_PATH + "graphs/"

    return {
        "Reforms": reforms,
        "load_data": load_data,
        "minyear": minyear,
        "prepare_data": prepare_data,
        "show_descr": show_descr,
        "taxtrans": taxtrans,
        "taxyear": taxyear,
        "run_hypo": run_hypo,
        "MAIN_PATH": MAIN_PATH,
        "SOEP_PATH": SOEP_PATH,
        "DATA_PATH": DATA_PATH,
        "GRAPH_PATH": GRAPH_PATH,
    }


def ubi_settings(tb):
    """ Set alternative tax benefit parameters for UBI
    """

    tb_ubi = tb.copy()
    # UBI amount for adults
    tb_ubi["ubi_adult"] = 1000
    tb_ubi["ubi_child"] = 0.5 * tb_ubi["ubi_adult"]

    # Minijobgrenze
    tb_ubi["mini_grenzew"] = 0
    tb_ubi["mini_grenzeo"] = tb_ubi["mini_grenzew"]

    # Midijobgrenze
    tb_ubi["midi_grenze"] = 0

    # Kindergeld
    for i in range(1, 5):
        tb_ubi["kgeld" + str(i)] = 0

    # Tax Tariff

    return tb_ubi


def hypo_graph_settings():
    """ Set various settings for Hypo Graphs
    """
    # Create labels for each graph type
    xlabels = {
        "lego": "Gross monthly household income (€)",
        "emtr": "Gross monthly household income (€)",
        "bruttonetto": "Gross monthly household income (€)",
    }

    ylabels = {
        "lego": "Disp. monthly household income (€)",
        "emtr": "Effective Marginal Tax Rate",
        "bruttonetto": "Disp. monthly household income (€)",
    }
    # depending on the plottype, which reform-specific variables to plot?
    yvars = {"emtr": "emtr", "bruttonetto": "dpi"}

    # max yearly income to plot
    maxinc = 60000

    return xlabels, ylabels, yvars, maxinc

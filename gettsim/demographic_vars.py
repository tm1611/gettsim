"""This module provides functions to compute demographic variables."""
from gettsim.typing import BoolSeries
from gettsim.typing import IntSeries


def alleinerziehend_tu(tu_id: IntSeries, alleinerziehend: BoolSeries) -> BoolSeries:
    """

    Parameters
    ----------
    tu_id
    alleinerziehend

    Returns
    -------

    """
    return alleinerziehend.groupby(tu_id).any()


def alleinerziehend_hh(hh_id, alleinerziehend):
    """

    Parameters
    ----------
    hh_id
        See :ref:`hh_id`
    alleinerziehend

    Returns
    -------

    """
    return alleinerziehend.groupby(hh_id).any()


def _anz_kinder_in_tu(tu_id, kind):
    """

    Parameters
    ----------
    tu_id
    kind

    Returns
    -------

    """
    return (kind.astype(int)).groupby(tu_id).sum()


def _anz_erwachsene_tu(tu_id, kind):
    """

    Parameters
    ----------
    tu_id
    kind

    Returns
    -------

    """
    return (~kind).astype(int).groupby(tu_id).sum()


def gemeinsam_veranlagt(tu_id, _anz_erwachsene_tu):
    """

    Parameters
    ----------
    tu_id
    _anz_erwachsene_tu

    Returns
    -------

    """
    return tu_id.replace(_anz_erwachsene_tu) == 2


def gemeinsam_veranlagte_tu(gemeinsam_veranlagt, tu_id):
    """

    Parameters
    ----------
    gemeinsam_veranlagt
    tu_id

    Returns
    -------

    """
    return gemeinsam_veranlagt.groupby(tu_id).any()


def bruttolohn_m_tu(bruttolohn_m, tu_id):
    """

    Parameters
    ----------
    bruttolohn_m
    tu_id

    Returns
    -------

    """
    return bruttolohn_m.groupby(tu_id).sum()


def anz_kind_zwischen_0_6_hh(hh_id, kind, alter):
    """

    Parameters
    ----------
    hh_id
    kind
    alter

    Returns
    -------

    """
    kind_0_bis_6 = kind & (0 <= alter) & (alter <= 6)
    return kind_0_bis_6.astype(int).groupby(hh_id).sum()


def anz_kind_zwischen_0_15_hh(hh_id, kind, alter):
    """

    Parameters
    ----------
    hh_id
    kind
    alter

    Returns
    -------

    """
    kind_0_bis_15 = kind & (0 <= alter) & (alter <= 15)
    return kind_0_bis_15.astype(int).groupby(hh_id).sum()


def anz_kind_zwischen_7_13_hh(hh_id, kind, alter):
    """

    Parameters
    ----------
    hh_id
    kind
    alter

    Returns
    -------

    """
    kind_7_bis_13 = kind & (7 <= alter) & (alter <= 13)
    return kind_7_bis_13.astype(int).groupby(hh_id).sum()


def anz_kind_zwischen_14_24_hh(hh_id, kind, alter):
    """

    Parameters
    ----------
    hh_id
    kind
    alter

    Returns
    -------

    """
    kind_14_bis_24 = kind & (14 <= alter) & (alter <= 24)
    return kind_14_bis_24.astype(int).groupby(hh_id).sum()


def anz_kinder_hh(hh_id, kind):
    """

    Parameters
    ----------
    hh_id
    kind

    Returns
    -------

    """
    return kind.astype(int).groupby(hh_id).sum()


def anz_kinder_tu(tu_id, kind):
    """

    Parameters
    ----------
    tu_id
    kind

    Returns
    -------

    """
    return (kind.astype(int)).groupby(tu_id).sum()


def anz_erwachsene_hh(hh_id, kind):
    """

    Parameters
    ----------
    hh_id
    kind

    Returns
    -------

    """
    return (~kind).groupby(hh_id).sum()


def kinder_in_hh(kind, hh_id):
    """

    Parameters
    ----------
    kind
    hh_id

    Returns
    -------

    """
    return kind.groupby(hh_id).any()


def haushaltsgröße(hh_id):
    """

    Parameters
    ----------
    hh_id

    Returns
    -------

    """
    return hh_id.groupby(hh_id).transform("size")


def haushaltsgröße_hh(hh_id):
    """

    Parameters
    ----------
    hh_id

    Returns
    -------

    """
    return hh_id.groupby(hh_id).size()


def rentner_in_hh(hh_id, rentner):
    """

    Parameters
    ----------
    hh_id
    rentner

    Returns
    -------

    """
    return rentner.groupby(hh_id).any()

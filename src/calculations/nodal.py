from shapely.geometry import LineString


def calc_nodal(vlp: dict, ipr: dict):
    """
    Расчёт точки пересечения VLP vs IPR

    Parameters
    ----------
    vlp : dict
        Словарь, содержащий VLP
    ipr : dict
        Словарь, содержащий IPR
    """
    # Можно использовать numpy или библиотеку Shapely, LineString intersection
    vlp_line = LineString(
        [(x, y) for x, y in zip(vlp["q_liq"], vlp["p_wf"])]
    )

    ipr_line = LineString(
        [(x, y) for x, y in zip(ipr["q_liq"], ipr["p_wf"])]
    )

    intersection = vlp_line.intersection(ipr_line)
    return dict(q_liq=intersection.x, p_wf=intersection.y)



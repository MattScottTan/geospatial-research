from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parents[1]
OUT_T = ROOT / 'outputs' / 'tables'
OUT_F = ROOT / 'outputs' / 'figures'
DOCS = ROOT / 'docs'
for p in [OUT_T, OUT_F, DOCS]:
    p.mkdir(parents=True, exist_ok=True)

RAW_JSON: Dict[str, str] = {
    'Singapore': '''{"meta": {"count": 2210, "db_response_time_ms": 91, "page": 1, "per_page": 200, "groups_count": 26, "cost_usd": 0.0001}, "group_by": [{"key": "2008", "key_display_name": "2008", "count": 141}, {"key": "2007", "key_display_name": "2007", "count": 126}, {"key": "2006", "key_display_name": "2006", "count": 125}, {"key": "2010", "key_display_name": "2010", "count": 123}, {"key": "2005", "key_display_name": "2005", "count": 119}, {"key": "2009", "key_display_name": "2009", "count": 117}, {"key": "2004", "key_display_name": "2004", "count": 113}, {"key": "2014", "key_display_name": "2014", "count": 103}, {"key": "2016", "key_display_name": "2016", "count": 96}, {"key": "2013", "key_display_name": "2013", "count": 90}, {"key": "2011", "key_display_name": "2011", "count": 89}, {"key": "2017", "key_display_name": "2017", "count": 88}, {"key": "2012", "key_display_name": "2012", "count": 85}, {"key": "2015", "key_display_name": "2015", "count": 84}, {"key": "2025", "key_display_name": "2025", "count": 81}, {"key": "2018", "key_display_name": "2018", "count": 80}, {"key": "2019", "key_display_name": "2019", "count": 79}, {"key": "2003", "key_display_name": "2003", "count": 74}, {"key": "2002", "key_display_name": "2002", "count": 63}, {"key": "2023", "key_display_name": "2023", "count": 62}, {"key": "2020", "key_display_name": "2020", "count": 59}, {"key": "2024", "key_display_name": "2024", "count": 57}, {"key": "2022", "key_display_name": "2022", "count": 56}, {"key": "2021", "key_display_name": "2021", "count": 49}, {"key": "2001", "key_display_name": "2001", "count": 33}, {"key": "2000", "key_display_name": "2000", "count": 18}]}''',
    'Tokyo': '''{"meta": {"count": 6491, "db_response_time_ms": 90, "page": 1, "per_page": 200, "groups_count": 26, "cost_usd": 0.0001}, "group_by": [{"key": "2002", "key_display_name": "2002", "count": 422}, {"key": "2010", "key_display_name": "2010", "count": 327}, {"key": "2015", "key_display_name": "2015", "count": 320}, {"key": "2011", "key_display_name": "2011", "count": 305}, {"key": "2017", "key_display_name": "2017", "count": 301}, {"key": "2008", "key_display_name": "2008", "count": 292}, {"key": "2009", "key_display_name": "2009", "count": 289}, {"key": "2023", "key_display_name": "2023", "count": 289}, {"key": "2012", "key_display_name": "2012", "count": 285}, {"key": "2014", "key_display_name": "2014", "count": 285}, {"key": "2018", "key_display_name": "2018", "count": 285}, {"key": "2016", "key_display_name": "2016", "count": 274}, {"key": "2006", "key_display_name": "2006", "count": 259}, {"key": "2005", "key_display_name": "2005", "count": 256}, {"key": "2013", "key_display_name": "2013", "count": 251}, {"key": "2019", "key_display_name": "2019", "count": 243}, {"key": "2003", "key_display_name": "2003", "count": 237}, {"key": "2007", "key_display_name": "2007", "count": 223}, {"key": "2020", "key_display_name": "2020", "count": 222}, {"key": "2024", "key_display_name": "2024", "count": 202}, {"key": "2025", "key_display_name": "2025", "count": 198}, {"key": "2022", "key_display_name": "2022", "count": 186}, {"key": "2004", "key_display_name": "2004", "count": 183}, {"key": "2021", "key_display_name": "2021", "count": 170}, {"key": "2001", "key_display_name": "2001", "count": 98}, {"key": "2000", "key_display_name": "2000", "count": 89}]}''',
    'Seoul': '''{"meta": {"count": 82, "db_response_time_ms": 6, "page": 1, "per_page": 200, "groups_count": 22, "cost_usd": 0.0001}, "group_by": [{"key": "2002", "key_display_name": "2002", "count": 8}, {"key": "2004", "key_display_name": "2004", "count": 7}, {"key": "2005", "key_display_name": "2005", "count": 6}, {"key": "2007", "key_display_name": "2007", "count": 6}, {"key": "2021", "key_display_name": "2021", "count": 6}, {"key": "2003", "key_display_name": "2003", "count": 5}, {"key": "2018", "key_display_name": "2018", "count": 5}, {"key": "2009", "key_display_name": "2009", "count": 4}, {"key": "2015", "key_display_name": "2015", "count": 4}, {"key": "2016", "key_display_name": "2016", "count": 4}, {"key": "2019", "key_display_name": "2019", "count": 4}, {"key": "2006", "key_display_name": "2006", "count": 3}, {"key": "2008", "key_display_name": "2008", "count": 3}, {"key": "2017", "key_display_name": "2017", "count": 3}, {"key": "2022", "key_display_name": "2022", "count": 3}, {"key": "2001", "key_display_name": "2001", "count": 2}, {"key": "2010", "key_display_name": "2010", "count": 2}, {"key": "2011", "key_display_name": "2011", "count": 2}, {"key": "2020", "key_display_name": "2020", "count": 2}, {"key": "2012", "key_display_name": "2012", "count": 1}, {"key": "2014", "key_display_name": "2014", "count": 1}, {"key": "2025", "key_display_name": "2025", "count": 1}]}''',
    'Kyoto': '''{"meta": {"count": 95, "db_response_time_ms": 65, "page": 1, "per_page": 200, "groups_count": 25, "cost_usd": 0.0001}, "group_by": [{"key": "2022", "key_display_name": "2022", "count": 10}, {"key": "2021", "key_display_name": "2021", "count": 8}, {"key": "2025", "key_display_name": "2025", "count": 8}, {"key": "2002", "key_display_name": "2002", "count": 6}, {"key": "2019", "key_display_name": "2019", "count": 6}, {"key": "2006", "key_display_name": "2006", "count": 5}, {"key": "2007", "key_display_name": "2007", "count": 5}, {"key": "2017", "key_display_name": "2017", "count": 5}, {"key": "2005", "key_display_name": "2005", "count": 4}, {"key": "2010", "key_display_name": "2010", "count": 4}, {"key": "2013", "key_display_name": "2013", "count": 4}, {"key": "2018", "key_display_name": "2018", "count": 4}, {"key": "2023", "key_display_name": "2023", "count": 4}, {"key": "2011", "key_display_name": "2011", "count": 3}, {"key": "2012", "key_display_name": "2012", "count": 3}, {"key": "2015", "key_display_name": "2015", "count": 3}, {"key": "2020", "key_display_name": "2020", "count": 3}, {"key": "2016", "key_display_name": "2016", "count": 2}, {"key": "2024", "key_display_name": "2024", "count": 2}, {"key": "2000", "key_display_name": "2000", "count": 1}, {"key": "2003", "key_display_name": "2003", "count": 1}, {"key": "2004", "key_display_name": "2004", "count": 1}, {"key": "2008", "key_display_name": "2008", "count": 1}, {"key": "2009", "key_display_name": "2009", "count": 1}, {"key": "2014", "key_display_name": "2014", "count": 1}]}''',
    'Hong Kong': '''{"meta": {"count": 788, "db_response_time_ms": 89, "page": 1, "per_page": 200, "groups_count": 26, "cost_usd": 0.0001}, "group_by": [{"key": "2021", "key_display_name": "2021", "count": 62}, {"key": "2024", "key_display_name": "2024", "count": 57}, {"key": "2022", "key_display_name": "2022", "count": 46}, {"key": "2025", "key_display_name": "2025", "count": 45}, {"key": "2020", "key_display_name": "2020", "count": 43}, {"key": "2019", "key_display_name": "2019", "count": 39}, {"key": "2018", "key_display_name": "2018", "count": 38}, {"key": "2002", "key_display_name": "2002", "count": 37}, {"key": "2017", "key_display_name": "2017", "count": 36}, {"key": "2023", "key_display_name": "2023", "count": 33}, {"key": "2016", "key_display_name": "2016", "count": 32}, {"key": "2012", "key_display_name": "2012", "count": 28}, {"key": "2013", "key_display_name": "2013", "count": 28}, {"key": "2006", "key_display_name": "2006", "count": 25}, {"key": "2008", "key_display_name": "2008", "count": 25}, {"key": "2009", "key_display_name": "2009", "count": 25}, {"key": "2011", "key_display_name": "2011", "count": 25}, {"key": "2003", "key_display_name": "2003", "count": 22}, {"key": "2004", "key_display_name": "2004", "count": 22}, {"key": "2010", "key_display_name": "2010", "count": 21}, {"key": "2015", "key_display_name": "2015", "count": 21}, {"key": "2014", "key_display_name": "2014", "count": 20}, {"key": "2000", "key_display_name": "2000", "count": 17}, {"key": "2005", "key_display_name": "2005", "count": 16}, {"key": "2001", "key_display_name": "2001", "count": 15}, {"key": "2007", "key_display_name": "2007", "count": 10}]}''',
    'Milan': '''{"meta": {"count": 0, "db_response_time_ms": 59, "page": 1, "per_page": 200, "groups_count": 0, "cost_usd": 0.0001}, "group_by": []}''',
    'Zurich': '''{"meta": {"count": 36, "db_response_time_ms": 43, "page": 1, "per_page": 200, "groups_count": 17, "cost_usd": 0.0001}, "group_by": [{"key": "2025", "key_display_name": "2025", "count": 6}, {"key": "2015", "key_display_name": "2015", "count": 4}, {"key": "2021", "key_display_name": "2021", "count": 3}, {"key": "2022", "key_display_name": "2022", "count": 3}, {"key": "2024", "key_display_name": "2024", "count": 3}, {"key": "2008", "key_display_name": "2008", "count": 2}, {"key": "2012", "key_display_name": "2012", "count": 2}, {"key": "2014", "key_display_name": "2014", "count": 2}, {"key": "2020", "key_display_name": "2020", "count": 2}, {"key": "2023", "key_display_name": "2023", "count": 2}, {"key": "2006", "key_display_name": "2006", "count": 1}, {"key": "2010", "key_display_name": "2010", "count": 1}, {"key": "2011", "key_display_name": "2011", "count": 1}, {"key": "2013", "key_display_name": "2013", "count": 1}, {"key": "2017", "key_display_name": "2017", "count": 1}, {"key": "2018", "key_display_name": "2018", "count": 1}, {"key": "2019", "key_display_name": "2019", "count": 1}]}''',
    'Hyderabad': '''{"meta": {"count": 38, "db_response_time_ms": 6, "page": 1, "per_page": 200, "groups_count": 14, "cost_usd": 0.0001}, "group_by": [{"key": "2023", "key_display_name": "2023", "count": 7}, {"key": "2019", "key_display_name": "2019", "count": 5}, {"key": "2022", "key_display_name": "2022", "count": 4}, {"key": "2025", "key_display_name": "2025", "count": 4}, {"key": "2010", "key_display_name": "2010", "count": 3}, {"key": "2021", "key_display_name": "2021", "count": 3}, {"key": "2015", "key_display_name": "2015", "count": 2}, {"key": "2017", "key_display_name": "2017", "count": 2}, {"key": "2018", "key_display_name": "2018", "count": 2}, {"key": "2020", "key_display_name": "2020", "count": 2}, {"key": "2011", "key_display_name": "2011", "count": 1}, {"key": "2012", "key_display_name": "2012", "count": 1}, {"key": "2013", "key_display_name": "2013", "count": 1}, {"key": "2016", "key_display_name": "2016", "count": 1}]}''',
    'Abu Dhabi': '''{"meta": {"count": 96, "db_response_time_ms": 7, "page": 1, "per_page": 200, "groups_count": 16, "cost_usd": 0.0001}, "group_by": [{"key": "2024", "key_display_name": "2024", "count": 20}, {"key": "2022", "key_display_name": "2022", "count": 10}, {"key": "2011", "key_display_name": "2011", "count": 9}, {"key": "2023", "key_display_name": "2023", "count": 9}, {"key": "2025", "key_display_name": "2025", "count": 8}, {"key": "2012", "key_display_name": "2012", "count": 7}, {"key": "2021", "key_display_name": "2021", "count": 7}, {"key": "2015", "key_display_name": "2015", "count": 6}, {"key": "2018", "key_display_name": "2018", "count": 5}, {"key": "2016", "key_display_name": "2016", "count": 4}, {"key": "2013", "key_display_name": "2013", "count": 3}, {"key": "2020", "key_display_name": "2020", "count": 3}, {"key": "2019", "key_display_name": "2019", "count": 2}, {"key": "2008", "key_display_name": "2008", "count": 1}, {"key": "2010", "key_display_name": "2010", "count": 1}, {"key": "2017", "key_display_name": "2017", "count": 1}]}''',
    'Beijing': '''{"meta": {"count": 1053, "db_response_time_ms": 36, "page": 1, "per_page": 200, "groups_count": 26, "cost_usd": 0.0001}, "group_by": [{"key": "2025", "key_display_name": "2025", "count": 123}, {"key": "2023", "key_display_name": "2023", "count": 117}, {"key": "2024", "key_display_name": "2024", "count": 117}, {"key": "2022", "key_display_name": "2022", "count": 82}, {"key": "2021", "key_display_name": "2021", "count": 77}, {"key": "2020", "key_display_name": "2020", "count": 70}, {"key": "2019", "key_display_name": "2019", "count": 66}, {"key": "2018", "key_display_name": "2018", "count": 55}, {"key": "2016", "key_display_name": "2016", "count": 37}, {"key": "2015", "key_display_name": "2015", "count": 31}, {"key": "2017", "key_display_name": "2017", "count": 29}, {"key": "2013", "key_display_name": "2013", "count": 28}, {"key": "2014", "key_display_name": "2014", "count": 26}, {"key": "2007", "key_display_name": "2007", "count": 25}, {"key": "2011", "key_display_name": "2011", "count": 23}, {"key": "2010", "key_display_name": "2010", "count": 22}, {"key": "2006", "key_display_name": "2006", "count": 17}, {"key": "2012", "key_display_name": "2012", "count": 17}, {"key": "2004", "key_display_name": "2004", "count": 16}, {"key": "2005", "key_display_name": "2005", "count": 14}, {"key": "2009", "key_display_name": "2009", "count": 14}, {"key": "2003", "key_display_name": "2003", "count": 12}, {"key": "2000", "key_display_name": "2000", "count": 11}, {"key": "2002", "key_display_name": "2002", "count": 11}, {"key": "2008", "key_display_name": "2008", "count": 9}, {"key": "2001", "key_display_name": "2001", "count": 4}]}''',
    'Barcelona': '''{"meta": {"count": 1455, "db_response_time_ms": 26, "page": 1, "per_page": 200, "groups_count": 26, "cost_usd": 0.0001}, "group_by": [{"key": "2011", "key_display_name": "2011", "count": 99}, {"key": "2012", "key_display_name": "2012", "count": 89}, {"key": "2014", "key_display_name": "2014", "count": 89}, {"key": "2010", "key_display_name": "2010", "count": 86}, {"key": "2009", "key_display_name": "2009", "count": 78}, {"key": "2015", "key_display_name": "2015", "count": 78}, {"key": "2018", "key_display_name": "2018", "count": 72}, {"key": "2013", "key_display_name": "2013", "count": 71}, {"key": "2017", "key_display_name": "2017", "count": 70}, {"key": "2016", "key_display_name": "2016", "count": 66}, {"key": "2006", "key_display_name": "2006", "count": 63}, {"key": "2008", "key_display_name": "2008", "count": 63}, {"key": "2020", "key_display_name": "2020", "count": 63}, {"key": "2007", "key_display_name": "2007", "count": 60}, {"key": "2023", "key_display_name": "2023", "count": 58}, {"key": "2019", "key_display_name": "2019", "count": 53}, {"key": "2005", "key_display_name": "2005", "count": 50}, {"key": "2021", "key_display_name": "2021", "count": 48}, {"key": "2024", "key_display_name": "2024", "count": 42}, {"key": "2022", "key_display_name": "2022", "count": 37}, {"key": "2025", "key_display_name": "2025", "count": 37}, {"key": "2004", "key_display_name": "2004", "count": 32}, {"key": "2002", "key_display_name": "2002", "count": 23}, {"key": "2003", "key_display_name": "2003", "count": 20}, {"key": "2000", "key_display_name": "2000", "count": 4}, {"key": "2001", "key_display_name": "2001", "count": 4}]}''',
    'Valencia': '''{"meta": {"count": 994, "db_response_time_ms": 9, "page": 1, "per_page": 200, "groups_count": 26, "cost_usd": 0.0001}, "group_by": [{"key": "2011", "key_display_name": "2011", "count": 68}, {"key": "2012", "key_display_name": "2012", "count": 59}, {"key": "2010", "key_display_name": "2010", "count": 58}, {"key": "2005", "key_display_name": "2005", "count": 53}, {"key": "2009", "key_display_name": "2009", "count": 52}, {"key": "2017", "key_display_name": "2017", "count": 50}, {"key": "2018", "key_display_name": "2018", "count": 50}, {"key": "2007", "key_display_name": "2007", "count": 48}, {"key": "2019", "key_display_name": "2019", "count": 47}, {"key": "2020", "key_display_name": "2020", "count": 44}, {"key": "2006", "key_display_name": "2006", "count": 43}, {"key": "2016", "key_display_name": "2016", "count": 43}, {"key": "2008", "key_display_name": "2008", "count": 42}, {"key": "2015", "key_display_name": "2015", "count": 39}, {"key": "2013", "key_display_name": "2013", "count": 38}, {"key": "2024", "key_display_name": "2024", "count": 36}, {"key": "2021", "key_display_name": "2021", "count": 34}, {"key": "2014", "key_display_name": "2014", "count": 32}, {"key": "2002", "key_display_name": "2002", "count": 29}, {"key": "2003", "key_display_name": "2003", "count": 26}, {"key": "2023", "key_display_name": "2023", "count": 25}, {"key": "2025", "key_display_name": "2025", "count": 21}, {"key": "2004", "key_display_name": "2004", "count": 18}, {"key": "2022", "key_display_name": "2022", "count": 17}, {"key": "2000", "key_display_name": "2000", "count": 11}, {"key": "2001", "key_display_name": "2001", "count": 11}]}''',
    'Daejeon': '''{"meta": {"count": 52, "db_response_time_ms": 17, "page": 1, "per_page": 200, "groups_count": 21, "cost_usd": 0.0001}, "group_by": [{"key": "2008", "key_display_name": "2008", "count": 5}, {"key": "2014", "key_display_name": "2014", "count": 5}, {"key": "2022", "key_display_name": "2022", "count": 5}, {"key": "2006", "key_display_name": "2006", "count": 3}, {"key": "2009", "key_display_name": "2009", "count": 3}, {"key": "2010", "key_display_name": "2010", "count": 3}, {"key": "2013", "key_display_name": "2013", "count": 3}, {"key": "2020", "key_display_name": "2020", "count": 3}, {"key": "2002", "key_display_name": "2002", "count": 2}, {"key": "2003", "key_display_name": "2003", "count": 2}, {"key": "2004", "key_display_name": "2004", "count": 2}, {"key": "2005", "key_display_name": "2005", "count": 2}, {"key": "2011", "key_display_name": "2011", "count": 2}, {"key": "2012", "key_display_name": "2012", "count": 2}, {"key": "2018", "key_display_name": "2018", "count": 2}, {"key": "2019", "key_display_name": "2019", "count": 2}, {"key": "2025", "key_display_name": "2025", "count": 2}, {"key": "2007", "key_display_name": "2007", "count": 1}, {"key": "2021", "key_display_name": "2021", "count": 1}, {"key": "2023", "key_display_name": "2023", "count": 1}, {"key": "2024", "key_display_name": "2024", "count": 1}]}''',
    'Delhi': '''{"meta": {"count": 223, "db_response_time_ms": 21, "page": 1, "per_page": 200, "groups_count": 18, "cost_usd": 0.0001}, "group_by": [{"key": "2023", "key_display_name": "2023", "count": 38}, {"key": "2019", "key_display_name": "2019", "count": 26}, {"key": "2021", "key_display_name": "2021", "count": 25}, {"key": "2022", "key_display_name": "2022", "count": 25}, {"key": "2025", "key_display_name": "2025", "count": 24}, {"key": "2024", "key_display_name": "2024", "count": 21}, {"key": "2020", "key_display_name": "2020", "count": 18}, {"key": "2018", "key_display_name": "2018", "count": 15}, {"key": "2017", "key_display_name": "2017", "count": 10}, {"key": "2014", "key_display_name": "2014", "count": 5}, {"key": "2015", "key_display_name": "2015", "count": 5}, {"key": "2016", "key_display_name": "2016", "count": 4}, {"key": "2011", "key_display_name": "2011", "count": 2}, {"key": "2008", "key_display_name": "2008", "count": 1}, {"key": "2009", "key_display_name": "2009", "count": 1}, {"key": "2010", "key_display_name": "2010", "count": 1}, {"key": "2012", "key_display_name": "2012", "count": 1}, {"key": "2013", "key_display_name": "2013", "count": 1}]}''',
    'Bengaluru': '''{"meta": {"count": 122, "db_response_time_ms": 10, "page": 1, "per_page": 200, "groups_count": 17, "cost_usd": 0.0001}, "group_by": [{"key": "2024", "key_display_name": "2024", "count": 21}, {"key": "2023", "key_display_name": "2023", "count": 18}, {"key": "2025", "key_display_name": "2025", "count": 18}, {"key": "2022", "key_display_name": "2022", "count": 15}, {"key": "2021", "key_display_name": "2021", "count": 8}, {"key": "2016", "key_display_name": "2016", "count": 7}, {"key": "2015", "key_display_name": "2015", "count": 5}, {"key": "2020", "key_display_name": "2020", "count": 5}, {"key": "2014", "key_display_name": "2014", "count": 4}, {"key": "2018", "key_display_name": "2018", "count": 4}, {"key": "2019", "key_display_name": "2019", "count": 4}, {"key": "2012", "key_display_name": "2012", "count": 3}, {"key": "2017", "key_display_name": "2017", "count": 3}, {"key": "2009", "key_display_name": "2009", "count": 2}, {"key": "2011", "key_display_name": "2011", "count": 2}, {"key": "2013", "key_display_name": "2013", "count": 2}, {"key": "2010", "key_display_name": "2010", "count": 1}]}''',
    'Lausanne': '''{"meta": {"count": 5, "db_response_time_ms": 6, "page": 1, "per_page": 200, "groups_count": 4, "cost_usd": 0.0001}, "group_by": [{"key": "2019", "key_display_name": "2019", "count": 2}, {"key": "2012", "key_display_name": "2012", "count": 1}, {"key": "2024", "key_display_name": "2024", "count": 1}, {"key": "2025", "key_display_name": "2025", "count": 1}]}''',
    'Genoa': '''{"meta": {"count": 142, "db_response_time_ms": 22, "page": 1, "per_page": 200, "groups_count": 26, "cost_usd": 0.0001}, "group_by": [{"key": "2009", "key_display_name": "2009", "count": 10}, {"key": "2016", "key_display_name": "2016", "count": 10}, {"key": "2024", "key_display_name": "2024", "count": 10}, {"key": "2021", "key_display_name": "2021", "count": 9}, {"key": "2022", "key_display_name": "2022", "count": 9}, {"key": "2017", "key_display_name": "2017", "count": 8}, {"key": "2015", "key_display_name": "2015", "count": 7}, {"key": "2020", "key_display_name": "2020", "count": 7}, {"key": "2002", "key_display_name": "2002", "count": 6}, {"key": "2012", "key_display_name": "2012", "count": 6}, {"key": "2014", "key_display_name": "2014", "count": 6}, {"key": "2023", "key_display_name": "2023", "count": 6}, {"key": "2025", "key_display_name": "2025", "count": 6}, {"key": "2003", "key_display_name": "2003", "count": 5}, {"key": "2011", "key_display_name": "2011", "count": 5}, {"key": "2018", "key_display_name": "2018", "count": 5}, {"key": "2013", "key_display_name": "2013", "count": 4}, {"key": "2019", "key_display_name": "2019", "count": 4}, {"key": "2004", "key_display_name": "2004", "count": 3}, {"key": "2006", "key_display_name": "2006", "count": 3}, {"key": "2008", "key_display_name": "2008", "count": 3}, {"key": "2000", "key_display_name": "2000", "count": 2}, {"key": "2001", "key_display_name": "2001", "count": 2}, {"key": "2005", "key_display_name": "2005", "count": 2}, {"key": "2007", "key_display_name": "2007", "count": 2}, {"key": "2010", "key_display_name": "2010", "count": 2}]}''',
    'Hiroshima': '''{"meta": {"count": 56, "db_response_time_ms": 22, "page": 1, "per_page": 200, "groups_count": 21, "cost_usd": 0.0001}, "group_by": [{"key": "2016", "key_display_name": "2016", "count": 7}, {"key": "2018", "key_display_name": "2018", "count": 7}, {"key": "2006", "key_display_name": "2006", "count": 5}, {"key": "2015", "key_display_name": "2015", "count": 5}, {"key": "2019", "key_display_name": "2019", "count": 4}, {"key": "2002", "key_display_name": "2002", "count": 3}, {"key": "2005", "key_display_name": "2005", "count": 3}, {"key": "2013", "key_display_name": "2013", "count": 3}, {"key": "2011", "key_display_name": "2011", "count": 2}, {"key": "2012", "key_display_name": "2012", "count": 2}, {"key": "2014", "key_display_name": "2014", "count": 2}, {"key": "2020", "key_display_name": "2020", "count": 2}, {"key": "2021", "key_display_name": "2021", "count": 2}, {"key": "2025", "key_display_name": "2025", "count": 2}, {"key": "2003", "key_display_name": "2003", "count": 1}, {"key": "2004", "key_display_name": "2004", "count": 1}, {"key": "2007", "key_display_name": "2007", "count": 1}, {"key": "2008", "key_display_name": "2008", "count": 1}, {"key": "2010", "key_display_name": "2010", "count": 1}, {"key": "2017", "key_display_name": "2017", "count": 1}, {"key": "2022", "key_display_name": "2022", "count": 1}]}''',
}

CITY_META: Dict[str, Dict[str, Any]] = {
    'Singapore': {'country': 'SG', 'treated': 1, 'event_year': 2010},
    'Tokyo': {'country': 'JP', 'treated': 1, 'event_year': 2011},
    'Seoul': {'country': 'KR', 'treated': 1, 'event_year': 2016},
    'Kyoto': {'country': 'JP', 'treated': 1, 'event_year': 2018},
    'Hong Kong': {'country': 'HK', 'treated': 1, 'event_year': 2019},
    'Milan': {'country': 'IT', 'treated': 1, 'event_year': 2020},
    'Zurich': {'country': 'CH', 'treated': 1, 'event_year': 2022},
    'Hyderabad': {'country': 'IN', 'treated': 1, 'event_year': 2022},
    'Abu Dhabi': {'country': 'AE', 'treated': 1, 'event_year': 2022},
    'Beijing': {'country': 'CN', 'treated': 0, 'event_year': None},
    'Barcelona': {'country': 'ES', 'treated': 0, 'event_year': None},
    'Valencia': {'country': 'ES', 'treated': 0, 'event_year': None},
    'Daejeon': {'country': 'KR', 'treated': 0, 'event_year': None},
    'Delhi': {'country': 'IN', 'treated': 0, 'event_year': None},
    'Bengaluru': {'country': 'IN', 'treated': 0, 'event_year': None},
    'Lausanne': {'country': 'CH', 'treated': 0, 'event_year': None},
    'Genoa': {'country': 'IT', 'treated': 0, 'event_year': None},
    'Hiroshima': {'country': 'JP', 'treated': 0, 'event_year': None},
}


def parse_city_payload(raw: str) -> Dict[int, int]:
    obj = json.loads(raw)
    return {int(d['key']): int(d['count']) for d in obj['group_by']}


def build_panel() -> pd.DataFrame:
    years = list(range(2000, 2026))
    rows = []
    for city, raw in RAW_JSON.items():
        counts = parse_city_payload(raw)
        meta = CITY_META[city]
        for yr in years:
            event_year = meta['event_year']
            post_full = int(meta['treated'] == 1 and event_year is not None and yr >= event_year + 1)
            rel_year = None if event_year is None else yr - event_year
            rows.append(
                {
                    'city': city,
                    'country': meta['country'],
                    'year': yr,
                    'ai_works_city_topinst': counts.get(yr, 0),
                    'treated_city': meta['treated'],
                    'event_year': event_year,
                    'post_full': post_full,
                    'rel_year': rel_year,
                }
            )
    df = pd.DataFrame(rows)
    df['log1p_ai'] = np.log1p(df['ai_works_city_topinst'])
    df['year_c'] = df['year'] - df['year'].min()
    return df


def run_twfe(df: pd.DataFrame, subset: str = 'all') -> pd.DataFrame:
    d = df.copy()
    if subset == 'multi_country':
        d = d[d['country'].isin(['JP', 'IN', 'KR', 'CH'])].copy()
    models = []
    m1 = smf.ols('log1p_ai ~ post_full + C(city) + C(year)', data=d).fit(cov_type='cluster', cov_kwds={'groups': d['city']})
    models.append(('TWFE baseline', subset, m1))
    m2 = smf.ols('log1p_ai ~ post_full + C(city) + C(year) + C(city):year_c', data=d).fit(cov_type='cluster', cov_kwds={'groups': d['city']})
    models.append(('TWFE + city trends', subset, m2))
    if subset == 'multi_country':
        m3 = smf.ols('log1p_ai ~ post_full + C(city) + C(country):C(year)', data=d).fit(cov_type='cluster', cov_kwds={'groups': d['city']})
        models.append(('City FE + country-year FE', subset, m3))
    rows = []
    for name, sub, mod in models:
        rows.append({
            'model': name,
            'subset': sub,
            'n_obs': int(mod.nobs),
            'coef_post_full': float(mod.params.get('post_full', np.nan)),
            'se_post_full': float(mod.bse.get('post_full', np.nan)),
            'p_post_full': float(mod.pvalues.get('post_full', np.nan)),
            'ci_low': float(mod.params.get('post_full', np.nan) - 1.96 * mod.bse.get('post_full', np.nan)),
            'ci_high': float(mod.params.get('post_full', np.nan) + 1.96 * mod.bse.get('post_full', np.nan)),
            'r2': float(mod.rsquared),
        })
    return pd.DataFrame(rows)


def add_event_bins(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()
    def bin_rel(x):
        if pd.isna(x):
            return 'never'
        x = int(x)
        if x <= -5:
            return 'lead_le5'
        if x == -4:
            return 'lead_4'
        if x == -3:
            return 'lead_3'
        if x == -2:
            return 'lead_2'
        if x == -1:
            return 'lead_1'
        if x == 0:
            return 'event_0'
        if x == 1:
            return 'lag_1'
        if x == 2:
            return 'lag_2'
        if x == 3:
            return 'lag_3'
        if x == 4:
            return 'lag_4'
        return 'lag_ge5'
    d['event_bin'] = d['rel_year'].apply(bin_rel)
    return d


def run_event_study(df: pd.DataFrame, subset: str = 'all') -> pd.DataFrame:
    d = add_event_bins(df)
    if subset == 'multi_country':
        d = d[d['country'].isin(['JP', 'IN', 'KR', 'CH'])].copy()
    # only treated cities contribute event dummies; never-treated cities just provide FE baseline
    for col in ['lead_le5','lead_4','lead_3','lead_2','event_0','lag_1','lag_2','lag_3','lag_4','lag_ge5']:
        d[col] = ((d['event_bin'] == col) & (d['treated_city'] == 1)).astype(int)
    formula = 'log1p_ai ~ lead_le5 + lead_4 + lead_3 + lead_2 + event_0 + lag_1 + lag_2 + lag_3 + lag_4 + lag_ge5 + C(city) + C(year)'
    mod = smf.ols(formula, data=d).fit(cov_type='cluster', cov_kwds={'groups': d['city']})
    rows = []
    mapping = {
        'lead_le5': -5,
        'lead_4': -4,
        'lead_3': -3,
        'lead_2': -2,
        'event_0': 0,
        'lag_1': 1,
        'lag_2': 2,
        'lag_3': 3,
        'lag_4': 4,
        'lag_ge5': 5,
    }
    for term, ev in mapping.items():
        rows.append({
            'subset': subset,
            'term': term,
            'event_time': ev,
            'coef': float(mod.params.get(term, np.nan)),
            'se': float(mod.bse.get(term, np.nan)),
            'p': float(mod.pvalues.get(term, np.nan)),
            'ci_low': float(mod.params.get(term, np.nan) - 1.96 * mod.bse.get(term, np.nan)),
            'ci_high': float(mod.params.get(term, np.nan) + 1.96 * mod.bse.get(term, np.nan)),
        })
    out = pd.DataFrame(rows)
    # pretrend joint heuristic
    pre = ['lead_le5','lead_4','lead_3','lead_2']
    try:
        test = mod.f_test('lead_le5 = 0, lead_4 = 0, lead_3 = 0, lead_2 = 0')
        pre_p = float(test.pvalue)
    except Exception:
        pre_p = np.nan
    out.attrs['pretrend_p'] = pre_p
    return out


def make_event_plot(es_all: pd.DataFrame, es_multi: pd.DataFrame, fp: Path) -> None:
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for data, label, marker in [(es_all, 'Pilot sample', 'o'), (es_multi, 'Within-country subset', 's')]:
        ax.errorbar(data['event_time'], data['coef'], yerr=1.96 * data['se'], fmt=marker+'-', capsize=4, label=label)
    ax.axhline(0, color='0.4', ls='--', lw=1)
    ax.axvline(-1, color='0.7', ls=':', lw=1)
    ax.set_xlabel('Years relative to AWS local-region launch (event year = 0)')
    ax.set_ylabel('Event-study coefficient on log(1 + AI works)')
    ax.set_title('Stage 5 pilot event study')
    ax.grid(alpha=0.2)
    ax.legend()
    fig.tight_layout()
    fig.savefig(fp, dpi=220, bbox_inches='tight')
    plt.close(fig)


def make_avg_trends(df: pd.DataFrame, fp: Path) -> None:
    d = df.copy()
    avg = d.groupby(['year','treated_city'], as_index=False)['ai_works_city_topinst'].mean()
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for treated, label in [(1, 'Eventually treated cities'), (0, 'Never-treated controls')]:
        tmp = avg[avg['treated_city']==treated]
        ax.plot(tmp['year'], tmp['ai_works_city_topinst'], marker='o', label=label)
    ax.set_xlabel('Year')
    ax.set_ylabel('Average AI works in city-year panel')
    ax.set_title('Raw pilot-panel trends (unadjusted)')
    ax.grid(alpha=0.2)
    ax.legend()
    fig.tight_layout()
    fig.savefig(fp, dpi=220, bbox_inches='tight')
    plt.close(fig)


def write_summary(df: pd.DataFrame, twfe_all: pd.DataFrame, twfe_multi: pd.DataFrame, es_all: pd.DataFrame, es_multi: pd.DataFrame) -> None:
    pre_all = es_all.attrs.get('pretrend_p', np.nan)
    pre_multi = es_multi.attrs.get('pretrend_p', np.nan)
    lines = [
        '# Stage 5 pilot city-year panel and event-study',
        '',
        '## Design actually implemented',
        '- Outcome: annual AI-related works by city, but only from institution IDs present in the project\'s top-institution file. This is a pilot panel, not a full-city census.',
        '- Treatment: first local AWS region opening for cities within 75 km of a launch location; never-treated controls are cities farther than 75 km from any AWS launch city in the sample window.',
        '- Post indicator uses the first full publication year after launch to avoid partial-year contamination.',
        '',
        '## Coverage',
        f'- Cities in pilot panel: {df.city.nunique()}',
        f'- Years: {df.year.min()}-{df.year.max()}',
        f'- Treated cities: {df[df.treated_city==1].city.nunique()}',
        f'- Never-treated controls: {df[df.treated_city==0].city.nunique()}',
        '',
        '## Average treatment effect estimates',
        twfe_all.to_markdown(index=False),
        '',
        twfe_multi.to_markdown(index=False),
        '',
        '## Event-study pretrend checks',
        f'- Pilot sample pretrend joint p-value: {pre_all:.3f}' if pd.notna(pre_all) else '- Pilot sample pretrend joint p-value: NA',
        f'- Within-country subset pretrend joint p-value: {pre_multi:.3f}' if pd.notna(pre_multi) else '- Within-country subset pretrend joint p-value: NA',
        '',
        '## Interpretation',
        '- This pilot can show whether the sign is directionally consistent in a dynamic panel, but it cannot settle causality because the outcome is a top-institution subset and the treatment is still plausibly endogenous.',
        '- The strongest version here is the within-country subset with country-year comparison logic, which strips out many broad national shocks but still leaves city-specific selection into region openings unresolved.',
    ]
    (DOCS / 'stage5_pilot_summary.md').write_text('\n'.join(lines), encoding='utf-8')


def main() -> None:
    df = build_panel()
    df.to_csv(OUT_T / 'stage5_city_year_panel.csv', index=False)

    twfe_all = run_twfe(df, subset='all')
    twfe_multi = run_twfe(df, subset='multi_country')
    twfe = pd.concat([twfe_all, twfe_multi], ignore_index=True)
    twfe.to_csv(OUT_T / 'stage5_twfe_summary.csv', index=False)

    es_all = run_event_study(df, subset='all')
    es_multi = run_event_study(df, subset='multi_country')
    es = pd.concat([es_all, es_multi], ignore_index=True)
    es.to_csv(OUT_T / 'stage5_event_study_summary.csv', index=False)

    make_event_plot(es_all, es_multi, OUT_F / 'fig_stage5_event_study.png')
    make_avg_trends(df, OUT_F / 'fig_stage5_raw_trends.png')
    write_summary(df, twfe_all, twfe_multi, es_all, es_multi)

    print('Wrote panel and summaries.')


if __name__ == '__main__':
    main()

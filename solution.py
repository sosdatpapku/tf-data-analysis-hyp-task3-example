import pandas as pd
import numpy as np
from scipy.stats import shapiro, ttest_ind


chat_id = 1188007817 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    control_group = x
    experimental_group = y
    p_value_control = shapiro(control_group)
    p_value_experimental = shapiro(experimental_group)
    t_statistic, p_value = ttest_ind(control_group, experimental_group)
    alpha = 0.06
    if p_value < alpha:
        return True
    else:
        return False

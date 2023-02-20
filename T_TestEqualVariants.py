import math
from scipy.stats import t

def t_test_equal_variances(data1, data2, alpha=0.05):
    # Calculate the means and standard deviations of the two datasets
    n1 = len(data1)
    n2 = len(data2)
    mean1 = sum(data1) / n1
    mean2 = sum(data2) / n2
    var1 = sum([(x - mean1) ** 2 for x in data1]) / (n1 - 1)
    var2 = sum([(x - mean2) ** 2 for x in data2]) / (n2 - 1)
    s = math.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))

    # Calculate the t-statistic and p-value
    t_stat = (mean1 - mean2) / (s * math.sqrt(1 / n1 + 1 / n2))
    df = n1 + n2 - 2
    p_value = 2 * t.cdf(-abs(t_stat), df)

    # Determine whether the null hypothesis can be rejected
    if p_value < alpha:
        reject_null = True
    else:
        reject_null = False

    # Return the results
    return {'t_stat': t_stat, 'p_value': p_value, 'reject_null': reject_null}
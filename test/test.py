default_speaker_calibration = (
    118.97129592, 118.85342742, 118.1560025, 117.35310275, 116.41419258, 115.62182308, 115.20886492, 114.95345658,
    114.77811592, 114.84784333,
    114.98569725, 115.37972533, 116.2442175, 117.38331708, 118.87947008, 120.68096842, 122.10399808, 122.25416308,
    120.79821658, 118.21325358,
    115.36788542, 112.74273308, 110.61898283, 108.71922217, 107.14874533, 105.73730825, 104.46745983, 103.27669458,
    102.26681263071428, 101.25693068142857,
    100.24704873214286, 99.23716678285714, 98.22728483357143, 97.21740288428572, 96.20752093499999, 95.19763898571428,
    94.18775703642856, 93.17787508714285, 92.16799313785714, 91.15811118857143,
    90.14822923928571, 89.13834729, 88.12846534071429, 87.11858339142857, 86.10870144214286, 85.09881949285713,
    84.08893754357143, 83.0790555942857, 82.06917364499999, 81.05929169571428,
    80.04940974642857, 79.03952779714285, 78.02964584785714, 77.01976389857143, 76.00988194928571, 75.0
)

print(default_speaker_calibration)


def func(array):
    text = ""
    for val in array:
        text += str(val) + ", "
    return text[:-2]


print(func(default_speaker_calibration))
from functools import reduce

print(reduce(lambda x, y: str(x) + ", " + str(y), default_speaker_calibration))

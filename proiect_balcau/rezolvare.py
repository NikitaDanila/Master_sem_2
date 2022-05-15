from numpy import AxisError


x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
     47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
     76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100
     ]
lxM = [
    100000, 99930, 99860, 99760, 99654, 99543, 99425, 99302, 99173, 99032, 98880, 98716, 98540, 98353, 98144, 97914,
    97664, 97392, 97100, 96754, 96356, 95905, 95402, 94849, 94231, 93548, 92804, 91998, 91133, 90209, 89228, 88191,
    87101, 85960, 84731, 83417, 82024, 80556, 79017, 77374, 75633, 73803, 71891, 69907, 67814, 65625, 63353, 61011,
    58614, 56111, 53524, 50875, 48183, 45471, 42371, 38981, 35399, 31727, 28059, 24483, 21072, 17886, 14970, 12352,
    10045, 8050, 6356, 4942, 3785, 2854, 2118, 1546, 1111, 785, 545, 372, 250, 165, 107, 68, 42, 26, 15
]

lxF = [
    100000, 99960, 99920, 99880, 99838, 99794, 99748, 99700, 99651, 99597, 99539, 99477, 99412, 99342, 99261, 99167,
    99062, 98945, 98817, 98670, 98507, 98325, 98127, 97911, 97670, 97404, 97114, 96799, 96461, 96088, 95683, 95245,
    94774, 94272, 93717, 93112, 92456, 91752, 91000, 90182, 89302, 88361, 87361, 86304, 85125, 83829, 82423, 80911,
    79301, 77493, 75501, 73342, 71032, 68588, 65336, 61387, 56877, 51959, 46789, 41524, 36311, 31280, 26538, 22170,
    18232, 14757, 11751, 9205, 7091, 5370, 3996, 2922, 2099, 1480, 1024, 696, 463, 303, 194, 122, 75, 45, 26
]

DxM, DxF, NxM, NxF, axM, axF = [], [], [], [], [], []
p = 8
i = 0.08
v = (1 / (1 + i))


def calc_DxM():
    for i, j in zip(x, lxM):
        DxM.append(round(pow(v, i) * j, 3))
    # print(f'DxM =\n{DxM}\n')


def calc_DxF():
    for i, j in zip(x, lxF):
        DxF.append(round(pow(v, i)*j, 3))
    # print(f'DxF =\n{DxF}\n')


def calc_NxM():
    for i in range(len(DxM)):
        sum = 0
        for j in range(i, len(DxM)):
            sum = sum + DxM[j]
        NxM.append(round(sum, 3))

    # print(f'NxM =\n{NxM}\n')


def calc_NxF():
    for i in range(len(DxF)):
        sum = 0
        for j in range(i, len(DxF)):
            sum = sum + DxF[j]
        NxF.append(round(sum, 3))

    # print(f'NxF =\n{NxF}\n')


def calc_axM():
    for i in range(0, len(NxM), 1):
        value = 0
        if i == len(NxM) - 1:
            value = 0
        else:
            value = NxM[i + 1] / DxM[i]
        axM.append(round(value, 3))

    # print(f'axM =\n{axM}\n')


def calc_axF():
    for i in range(0, len(NxF), 1):
        value = 0
        if i == len(NxF) - 1:
            value = 0
        else:
            value = NxF[i + 1] / DxF[i]
        axF.append(round(value, 3))

    # print(f'axF =\n{axF}\n')


def P_771():
    """Calculate the single premium payable by a 30 years old
person for a single claim of 10000$ over 35 years if the person survives. The
annual interest percent is 6%."""

    age = 30
    T = 10000
    n = 35

    nExF = round(DxF[abs(age-18+n)]/DxF[abs(age - 18)],7)
    nExM = round(DxM[abs(age-18+n)]/DxM[age -18],7)

    rez_M = round(T * nExM,6)
    rez_F = round(T * nExF,6)
    rez_Banca_M = round(rez_M * (1 + i)**n,3)
    rez_Banca_F = round(rez_F * (1 + i)**n,3)
    print('p_771:')
    print(f'rez_M = {rez_M} rez_F = {rez_F}')
    print(f'rez_Banca_M = {rez_Banca_M} rez_Banca_F = {rez_Banca_F}\n')

def P_772():
    """Calculate the single premium payable by a 30 years old
person for a whole life annuity-immediate of 12000RON per year. The annual
interest percent is 8%"""
    age = 30
    T = 12000
    n = 35
    rez_M = round(axM[age - 18] * T, 4)
    rez_F = round(axF[age - 18] * T, 4)
    rez_Banca_M = round(rez_M * (1 + i)**n,3)
    rez_Banca_F = round(rez_F * (1 + i)**n,3)
    print('p_772:')
    print(f'rez_M = {rez_M} rez_F = {rez_F}')
    # print(f'rez_Banca_M = {rez_Banca_M} rez_Banca_F = {rez_Banca_F}\n')


def P_773():
    """Calculate the single premium payable by a 30 years old
person for a 35-year deferred whole life annuity-immediate of 12000RON per
year. The annual interest percent is 8%."""
    age = 30
    T = 12000
    r = 35
    raxF = round(NxF[abs(age-18+r)]/DxF[abs(age - 18)],7)
    raxM = round(NxM[abs(age-18+r)]/DxM[abs(age -18)],7)
    rez_M = round(T*raxM, 4)
    rez_F = round(T*raxF, 4)
    rez_Banca_M = round(rez_M * (1 + i)**r,3)
    rez_Banca_F = round(rez_F * (1 + i)**r,3)
    print('p_773:')
    print(f'rez_M = {rez_M} rez_F = {rez_F}')
    # print(f'rez_Banca_M = {rez_Banca_M} rez_Banca_F = {rez_Banca_F}\n')

def P_774():
    """Calculate the single premium payable by a 30 years old
person for a 35-year temporary life annuity-immediate of 12000RON per
year. The annual interest percent is 8%."""
    age = 30
    T = 12000
    r = 35
    raxF = round((NxF[abs(age - 18)] - NxF[abs(age-18+r)]) / DxF[abs(age-18)],7)
    raxM = round((NxM[abs(age - 18)] - NxM[abs(age-18+r)]) / DxM[abs(age-18)],7)
    rez_M = round(T*raxM, 4)
    rez_F = round(T*raxF, 4)
    rez_Banca_M = round(rez_M * (1 + i)**r,3)
    rez_Banca_F = round(rez_F * (1 + i)**r,3)
    print('p_774:')
    print(f'rez_M = {rez_M} rez_F = {rez_F}')
    # print(f'rez_Banca_M = {rez_Banca_M} rez_Banca_F = {rez_Banca_F}\n')

calc_DxM()
calc_DxF()
calc_NxM()
calc_NxF()
calc_axM()
calc_axF()
P_771()
P_772()
P_773()
P_774()
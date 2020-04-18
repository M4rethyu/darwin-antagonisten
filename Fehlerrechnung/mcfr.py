'''Copyright (c) 2020 Moritz Siebert
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

""" Dieses Package wurde von Moritz Siebert kreiert,
    um die Fehlerrechnung nach den Leitlinien des physikalischen Grundpraktikums der JMU-Wuerzburg zu automatisieren."""

import math as m
import statistics as st


def round_to_n(value, n):
    return (value / abs(value)) * int(value * 10 ** n + 0.5) / 10 ** n


'''Das n (also die negative Größenordnung auf die gerundet werden muss) wird anhand des Fehlers bestimmt.'''


def n_from_error(error):
    import math
    from numpy import sign
    return int((-sign(math.log(abs(error), 10)) * int(abs(math.log(abs(error), 10)))) + 2)


'''In dieser Funktion ermittle ich die gerundeten Werte und die Größenordnung des Messwertes in einer Liste.'''


def rou_val_n_err(value, error):
    from math import log
    ne = n_from_error(error)
    roundval = round_to_n(value, ne)
    rounderr = round_to_n(error, ne)
    dimen = int(log(abs(value), 10))
    return [round(roundval, ne), round(rounderr, ne), dimen, ne]


'''Hier kann mit der vorigen Funktion aus zwei Listen mit je ungerundeten Werten und Fehlern die zugehöirgen
gerundeten Werte,sowie die Größenordnung und die Nachkommastelle, auf die gerundet wurde ermittelt werden.'''


def vall_errl(vallist, errlist):
    try:
        joinl = [rou_val_n_err(vallist[i], errlist[i]) for i in range(len(vallist))]
        return joinl
    except:
        if len(vallist) != len(errlist):
            print('Die Listen sind nicht gleich lang!\n')
        else:
            print('Es ist ein anderer Fehler auftgetreten...\n')
        return


def mean(list):
    return sum(list) / len(list)


def stand_dev(list):
    return st.stdev(list)


def std_err(list):
    return st.stdev(list)/m.sqrt(len(list))


def stats_to_list(list):
    return mean(list), stand_dev(list), std_err(list)


def r_mean_err(list):
    return rou_val_n_err(mean(list), std_err(list))[:2]


def r_pois_mean_err(list):
    x = mean(list)
    stddev = m.sqrt(x)
    n = len(list)
    stdf = stddev/m.sqrt(n)
    return rou_val_n_err(x, stdf)[:2]

def poisv(list, x):
    mue = mean(list)
    p = (mue**x)/((m.e**mue)*m.factorial(x))
    return p


if __name__ == '__main__':
    tlist = [1.1, 1.2, 1.42, 1.33, 1.4]
    print(r_mean_err(tlist))
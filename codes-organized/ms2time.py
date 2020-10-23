def ms2time(ms1,ms2):
    time1 = round(ms1/7.8125)+1;
    time2 = round(ms2/7.8125)+1;
    return list(range(time1, time2))
def slices(series, length):
    if len(series) < 1 or length < 1 or length > len(series):
        raise ValueError('series must not be empty and lenght must be less than or equal to the size of series and positive')
    else:
        first = 0
        l_series = []
        while length != len(series)+1:
            l_series.append(series[first:length])
            first += 1
            length += 1
    return l_series

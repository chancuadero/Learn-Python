
mapping = {"Date": str, "Symbol": str, "Open": float, "High": float, "Low": float, "Close": float, "Volume": int}

def cleanData(read_stocks):
    cleaned_list = []
    for rs in read_stocks:
        result = {key:mapping.get(key)(value) for key, value in rs.items()}
        cleaned_list.append(result)
    return cleaned_list

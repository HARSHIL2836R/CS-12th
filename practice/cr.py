import csv
with open('me.csv', 'r') as f:
    reader = csv.reader(f)
    data = []
    try:
        data.append(reader.readrow())
    except EOFError:
        pass
    print('No. of records: ', len(data))
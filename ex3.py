import csv


def read_from_csv():
    with open('tz_opendata_z01012020_po01122020.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=';')
        result = []
        for row in csv_reader:
            in_row = False
            if row['BRAND'] == ['TOYOTA']:
                in_row = True
            if row['MAKE_YEAR'] == ['2012']:
                in_row = True
            if in_row:
                result.append(row)
    return write_in_csv(result)

def write_in_csv(res):
    filename = 'TOYOTA.csv'
    with open(filename, 'w') as csvresult:
        headers = ['D_REG', 'BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR', 'FUEL', 'N_REG_NEW']
        csv_writer = csv.DictWriter(csvresult, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(res)
    print(f'Write into {filename}')



import csv


def student_counts(file_in: str = 'student_counts.csv',
                   file_out: str = 'sorted_student_counts2.csv') -> None:

    with open(file_in, 'r', encoding='utf-8') as fi:
        reader = csv.DictReader(fi)
        columns = ['year'] + sorted(reader.fieldnames[1:],
                                    key=lambda x: (x[-1:], int(x[:-2])))
        rows = list(reader)

    with open(file_out, 'w', encoding='utf-8') as fo:
        writer = csv.DictWriter(fo, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


student_counts()
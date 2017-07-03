import csv

def export(url1, url2, url3):
    with open('url.csv', 'w') as csvfile:
        fieldnames = ['base_url', 'csv_url', 'web_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()


        writer.writerow({'base_url': url1, 'csv_url': url2, 'web_url': url3})


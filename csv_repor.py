import csv

def write_csv_report(page_data, filename="report.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ['page_url','h1','first_paragraph','outgoing_link_urls', 'image_urls']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        i = next(iter(page_data))
        writer.writerow({'page_url': page_data[i]["url"],'h1': page_data[i]["h1"],'first_paragraph': page_data[i]["first_paragraph"],'outgoing_link_urls': page_data[i]["outgoing_links"], 'image_urls': page_data[i]["image_urls"]})
import csv

def save_csv(file_path: str, dict_list: list) -> None:
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=dict_list[0].keys())
        writer.writeheader()
        for data in dict_list:
            data: dict
            writer.writerow(data)
    print(f'{file_path} 파일이 생성 되었습니다.')
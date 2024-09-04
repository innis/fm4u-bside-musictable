import os
import re
from datetime import datetime

def convert_to_markdown(input_text):
    lines = input_text.strip().split('\n')
    date_line = lines[0].strip()
    table_lines = lines[1:]

    # Parse date
    #date_obj = datetime.strptime(date_line, '%Y년 %m월 %d일 %A')
    #formatted_date = date_obj.strftime('%Y년 %m월 %d일 %A')

    # Start building markdown
    markdown = f"# {date_line} 플레이리스트\n\n"
    markdown += "| 번호 | 곡명 | 가수 | 설명 |\n"
    markdown += "|------|------|------|------|\n"

    for line in table_lines:
        parts = line.split('\t')
        if len(parts) >= 4:
            number, title, artist = parts[1:4]
            description = parts[4] if len(parts) > 4 else ""
            markdown += f"| {number.strip()} | {title.strip()} | {artist.strip()} | {description.strip()} |\n"

    return markdown

def process_files(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(".lst"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.md")

            with open(input_path, 'r', encoding='utf-8') as file:
                input_text = file.read()

            markdown_content = convert_to_markdown(input_text)

            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(markdown_content)

            print(f"Converted {filename} to Markdown.")

# 사용 예:
input_directory = "./lst"
output_directory = "./markdown"
process_files(input_directory, output_directory)

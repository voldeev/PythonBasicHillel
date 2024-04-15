import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    cleaned_text = re.sub(r'<[^>]+>', '', html)

    cleaned_text = '\n'.join(line for line in cleaned_text.split('\n') if line.strip())

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)


delete_html_tags('draft.html')

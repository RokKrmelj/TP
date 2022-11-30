import requests

def get_html(url):
    html = requests.get(url)
    if html.status_code == 200:
        return html.text
    else:
        return "false"

page = get_html("https://example.com/")
print(page)
page = get_html("http://example.com/neobstaja")
print(page)
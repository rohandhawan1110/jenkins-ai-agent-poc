from bs4 import BeautifulSoup

def clean_confluence_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator="\n")
    return text


html = """
<p>
Jenkins Job: CustomerPortal_Build<br />
Environment: UAT<br />
Branch: main
</p>
"""

clean_text = clean_confluence_html(html)

print("Input HTML: ", html)
print("Clean Output: ", clean_text)

# print("CLEAN OUTPUT:\n")
# print(clean_text)
# Replacing String with another string
def test_strreplace():
    string = "Hello, World!"
    assert string.replace("world", "Sohail") == "Hello, World!"

# String Split - Splits a string to two substrings


def test_strsplit():
    string = "Welcome to New Year"
    assert string.split(" ") == ["Welcome", "to", "New", "Year"]

# String Strip


def test_strStrip():
    string = "    Hello, World!    "
    assert string.strip() == "Hello, World!"
# String Concatenate


def test_strconcat():
    string1 = "Sohail"
    string2 = "Badeghar"
    assert string1 + string2 == "SohailBadeghar"


def pytest_html_report_title(report):
    report.title = "My very own title!"

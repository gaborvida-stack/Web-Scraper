try:
    import requests
    from bs4 import BeautifulSoup
except ImportError as err:
    print("Error occurred: {}".format(err))

def get_response(url, status=False):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print("Request failed: {}".format(err))
        return None

    if status:
        print("Response received: code={}".format(response.status_code))

    return response

def get_data(response, tag, class_name=None, id_name=None, attrs=None):
    if not response:
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    if class_name:
        content = soup.find_all(tag, class_=class_name)
    elif id_name:
        content = soup.find_all(tag, id=id_name)
    elif attrs:
        content = soup.find_all(tag, attrs=attrs)
    else:
        content = soup.find_all(tag)

    return [tag.get_text(strip=True) for tag in content]


def main():
    url = input("Enter URL: ").strip()
    tag = input("Enter HTML tag to search for: ").strip()
    attr_choice = input("Search by (c)lass, (i)d, or (a)ttributes? (leave empty for none): ").strip().lower()

    class_name = id_name = attrs = None

    if attr_choice == 'c':
        class_name = input("Enter class name: ").strip()
    elif attr_choice == 'i':
        id_name = input("Enter id name: ").strip()
    elif attr_choice == 'a':
        attr_key = input("Enter attribute name: ").strip()
        attr_value = input("Enter attribute value: ").strip()
        attrs = {attr_key: attr_value}

    response = get_response(url, status=True)
    content = get_data(response, tag, class_name, id_name, attrs)

    if content:
        print("Found content:")
        for index, item in enumerate(content, start=1):
            print(f"{index}. {item}")
    else:
        print("No content found.")

if __name__ == "__main__":
    main()
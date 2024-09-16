try:
    import requests
    from bs4 import BeautifulSoup
except ImportError as err:
    print(f"Error occurred: {err}")

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.response = None

    def get_response(self, status=False):
        try:
            self.response = requests.get(self.url)
            self.response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(f"Request failed: {err}")
            self.response = None
        if status and self.response:
            print(f"Response received: code={self.response.status_code}")
        return self.response

    def get_data(self, tag, class_name=None, id_name=None, attrs=None):
        if not self.response:
            return []

        soup = BeautifulSoup(self.response.content, "html.parser")

        if class_name:
            content = soup.find_all(tag, class_=class_name)
        elif id_name:
            content = soup.find_all(tag, id=id_name)
        elif attrs:
            content = soup.find_all(tag, attrs=attrs)
        else:
            content = soup.find_all(tag)

        return [item.get_text(strip=True) for item in content]

class Main:
    @staticmethod
    def run():
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

        scraper = WebScraper(url)
        scraper.get_response(status=True)
        content = scraper.get_data(tag, class_name, id_name, attrs)

        if content:
            print("Found content:")
            for index, item in enumerate(content, start=1):
                print(f"{index}. {item}")
        else:
            print("No content found.")

if __name__ == "__main__":
    Main.run()

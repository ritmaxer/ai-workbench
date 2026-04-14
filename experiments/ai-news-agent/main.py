import requests

def get_hn_ai():
    url = "https://hn.algolia.com/api/v1/search?query=AI"
    data = requests.get(url).json()
    hits = data.get("hits", [])[:5]

    lines = []

    for i, item in enumerate(hits, 1):
        title = item.get("title")
        link = item.get("url")

        print(f"{i}. {title}")
        print(link)
        print()

        lines.append(f"{i}. {title}\n{link}\n")

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    get_hn_ai()
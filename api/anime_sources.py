import re

from utils.utils import get_feed


class Ani:
    @staticmethod
    def get_ann_entires():
        all_entries = get_feed("https://www.animenewsnetwork.com/all/rss.xml?ann-edition=w")

        results = []
        for entries in all_entries:
            for entry in entries:
                url = entry.link
                title = entry.title

                description = entry.description
                description = re.sub(r"<.*?>", "", description)
                # remove new lines from post content
                description = re.sub(r"\n", " ", description)
                # remove extra spaces from post content
                description = re.sub(r"\s{2,}", " ", description)

                results.append({
                    "title": title,
                    "description": description,
                    "url": url,
                })
        return results

    @staticmethod
    def get_mal_entires():
        all_entries = get_feed("https://myanimelist.net/rss/news.xml")

        results = []
        for entries in all_entries:
            for entry in entries:
                description = entry.summary
                description = re.sub(r"<.*?>", "", description)
                # remove new lines from post content
                description = re.sub(r"\n", " ", description)
                # remove extra spaces from post content
                description = re.sub(r"\s{2,}", " ", description)

                results.append({
                    "title": entry.title,
                    "url": entry.link.split("?")[0],
                    "summary": description,
                    "thumbnail": entry.media_thumbnail,
                    "date": entry.published,
                })
        return results

    @staticmethod
    def get_crunchy_entires():
        all_entries = get_feed("http://feeds.feedburner.com/crunchyroll/animenews")

        results = []
        for entries in all_entries:
            for entry in entries:
                results.append({
                    "title": entry.title,
                    "url": entry.link.split("?")[0],
                    "summary": entry.summary,
                    "thumbnail": entry.media_thumbnail,
                    "date": entry.published,
                })
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Ani.get_crunchy_entires())

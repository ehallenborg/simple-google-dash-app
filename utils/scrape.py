import requests
import bs4

_URL = "https://myanimelist.net/anime/39617/Yakusoku_no_Neverland_2nd_Season"

class Scrape:

    def __init__(self):
        self.url = _URL

    def get_current_score(self, url=None):
        """Gets the current score and the number of users who have scored the show
           User can input their own url though it has to contain "myanimelist"

        Returns:
            [list]: [score, users]
        """
        score, users = [], []

        if url:
            if url.find("myanimelist.net/anime") == -1:
                return Warning("This URL is currently not supported")
            else:
                resp = requests.get(url)
        else:
            resp = requests.get(self.url)

        try:
            if resp.status_code == 200:
                soup = bs4.BeautifulSoup(resp.text, 'lxml')

                title = soup.select('title')[0].getText()
                score = soup.findAll("div", {"class": "score-label"})[0].getText()
                users = soup.findAll("div", {"class": "fl-l score"})[0].attrs['data-user'].split(" ")[0]
            else:
                return "Error processing request"
            
        except Exception as e:
            print(e)
            return e

        return [score, users]

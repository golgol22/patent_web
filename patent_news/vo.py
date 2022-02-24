class News:
    def __init__(self, news_img_url, news_title, news_content, news_reporter, news_date, news_url):
        self.news_img_url = news_img_url
        self.news_title = news_title
        self.news_content = news_content
        self.news_reporter = news_reporter
        self.news_date = news_date
        self.news_url = news_url
        
    def __str__(self):
        s = ''
        s += self.news_img_url + '|'
        s += self.news_title + '|'
        s += self.news_content + '|'
        s += self.news_reporter + '|'
        s += self.news_date + '|'
        s += self.news_url 
        return s
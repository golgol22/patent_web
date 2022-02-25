from member.vo import db

class NewsDB(db.Model):
    num = db.Column(db.Integer, primary_key=True)  
    user = db.Column(db.String(50), db.ForeignKey('member.id', ondelete='CASCADE'))
    news_img_url = db.Column(db.String(100), nullable=False)
    news_title = db.Column(db.String(100), nullable=False)
    news_content = db.Column(db.String(100), nullable=False)
    news_reporter = db.Column(db.String(50), nullable=False)
    news_date = db.Column(db.String(50), nullable=False)
    news_url = db.Column(db.String(100), nullable=False)
    
class News():
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
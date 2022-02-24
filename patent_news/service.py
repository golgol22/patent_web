from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from patent_news.vo import News

class Service:
    
    def getPatentNews(self, section='특허', section2=None):       
        res = []
        for page in range(1, 11):
            url = 'https://www.e-patentnews.com/sub.html?'
            url += 'page=' + str(page) + '&'
            
            if section == '특허':
                section = 'sc1'
            if section == '상표':
                section = 'sc9'
            if section == '디자인':
                section = 'sc7'
            if section == '사이언스':
                section = 'sc5'
            if section == '종합':
                section = 'sc6'
            if section == '특허&CEO':
                section = 'sc3'
            if section == 'TV 특허뉴스':
                section = 'sc20'
            if section == '특허Q&A':
                section = 'sc27'
            if section == '이슈':
                section = 'sc29'
            if section == '스페셜 기획':
                section = 'sc35'
            url += 'section=' + section + '&'
            
            if section2 != None:
                url += 'section2=' + section2
            
            try: 
                headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
                request = Request(url, headers=headers)
                response = urlopen(request)
                html = response.read()
                soup = BeautifulSoup(html, 'html.parser')
                news = soup.find_all('div', attrs={'class':'sub_read_list_box'})
                base_url = 'https://www.e-patentnews.com'

                for n in news:
                    img = n.find('img')
                    news_img_url = img.get('src')
                    news_title = n.select_one('dl > dt > a').text
                    news_content = n.select_one('dl > dd > a').text
                    news_reporter = n.select_one('dl > dd.etc > span').text
                    news_date = n.select_one('dl > dd.etc').text
                    news_url = n.find('a').get('href')
                    
                    news_img_url = base_url + news_img_url.lstrip('.').strip() 
                    news_title = news_title.strip()
                    news_content = news_content.strip()
                    news_reporter = news_reporter.strip()
                    news_date = news_date.split('|')[1].strip()
                    news_url = base_url + news_url.strip() 
                    
                    # print(news_img_url, news_title, news_content, news_reporter, news_date, news_url)
                    if news_img_url != None and news_title != None and news_content != None and news_reporter != None and news_date != None and news_url != None:
                        res.append(News(news_img_url=news_img_url, news_title=news_title, news_content=news_content, news_reporter=news_reporter, news_date=news_date, news_url=news_url))
        
            except Exception as e:
                break
            
        return res
        
if __name__ == "__main__": 
    s = Service()
    print(s.getPatentNews(section='특허'))
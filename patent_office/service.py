from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from vo import Office

class Service:
        
    def getPatentOffice(self, selected_sectors='전체'):       
        res = []
        page = 1
        while True:
            url = 'https://blsn.co.kr/companies/firm/list/?'
            if selected_sectors != '전체': 
                if selected_sectors == '생활(A)':
                    selected_sectors = 'pt_a'
                if selected_sectors == '운송(B)':
                    selected_sectors = 'pt_b'
                if selected_sectors == '화학(C)':
                    selected_sectors = 'pt_c'
                if selected_sectors == '섬유(D)':
                    selected_sectors = 'pt_d'
                if selected_sectors == '구조(E)':
                    selected_sectors = 'pt_e'
                if selected_sectors == '기계(F)':
                    selected_sectors = 'pt_f'
                if selected_sectors == '물리(G)':
                    selected_sectors = 'pt_g'
                if selected_sectors == '전기(H)':
                    selected_sectors = 'pt_h'
                if selected_sectors == '상표':
                    selected_sectors = 'dn%2Ctm'
                if selected_sectors == '디자인':
                    selected_sectors = 'dn'
                url += 'selected_sectors' + selected_sectors + '&'
            url += 'page=' + str(page)
            
            try: 
                headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
                request = Request(url, headers=headers)
                response = urlopen(request)
                html = response.read()
                soup = BeautifulSoup(html, 'html.parser')
                offices = soup.find_all('a', attrs={'class':'flex flex-row flex-wrap w-full cursor-pointer'})
                
                for office in offices:
                    office_name = office.find('span', attrs={'class':'text_content text_ellipsis'}).text
                    office_apply = office.select_one('div:nth-child(2) > span:nth-child(1)').text
                    office_referee = office.select_one('div:nth-child(2) > span:nth-child(3)').text
                    office_score = office.select_one('div:nth-child(2) > span:nth-child(5)').text
                    
                    office_name = office_name.strip()
                    office_apply = office_apply.strip()
                    office_referee = office_referee.strip()
                    office_score = ''.join(office_score.strip().replace('\n', '').split())
                    
                    print(office_name, office_apply, office_referee, office_score)
                    if office_name != None and office_apply != None and office_referee != None and office_score != None:
                        res.append(Office(office_name=office_name, office_apply=office_apply, office_referee=office_referee, office_score=office_score))
        
                page += 1
            except Exception as e:
                break
            
        return res
        
if __name__ == "__main__": 
    s = Service()
    print(s.getPatentOffice('전체'))
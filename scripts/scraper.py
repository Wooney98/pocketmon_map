import requests
from bs4 import BeautifulSoup
from pbook.models import Pocket

pocket = 20
#print(items)
def run():
    for i in range(1,pocket):
        url = f"https://pokemonkorea.co.kr/pokedex/view/{i}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")
        items = soup.find("div",class_= "book-ct").find_all('div',class_='bx-content')
        #print(items)
        for item in items:
            try:
                img_url = item.select("div>img")[0].get('src').strip()
                #name = item.select("h3>p.font-lato")
                name = item.select("div.col-lg-6")[1].text
                name_sp = name.split(" ")
                name = name_sp[2]
                name = "".join(name)
                character = item.select("p",class_="para descript")[2].text.strip()
                height = item.select("div.col-4>p")[0].text.strip()
                weight = item.select("div.col-4>p")[-2].text.strip()
                classify = item.select("div.col-4>p")[1].text.strip()
                link = url
                #type = item.select(".d-flex>span>p")[0].text
                #type2 = item.select(".d-flex>span>p")[1].text
                # type1 = type[0].text
                # type2 = type[1].text
                # if type2 is None:
                #     type = type1
                # else:
                #     type = type1+","+type2
                
                print(name)
                #if(Pocket.objects.filter(link__iexact=link).count()==0):
                Pocket(img_url=img_url,name=name,link=link,height=height,weight=weight,classify=classify,character=character).save()
                print(type(img_url),
                type(name),
                type(link),
                type(height),
                type(weight),
                type(classify),
                type(character))
            except Exception as e:
                    continue  

import codecs

from phone import Phone

def get_info2():

def get_info(phones):
    p = Phone()
    #phones = [18575670303,18588201231,15626585681]
    #print(phones)
 
    for phone in phones:
        try:
            city = p.find(phone)['city']
            province =p.find(phone)['province']
            print("%s %s %s"%(phone,province,city))
        except:
            pass
if __name__ == '__main__':          
    f = open('nihao.txt') 
    phones = [line.strip() for line in f.readlines()]  
    f.close()  
    #print(phones) 
    get_info(phones)




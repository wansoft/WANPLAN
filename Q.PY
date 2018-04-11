import codecs

from phone import Phone
 
def get_info(phones):
    p = Phone()
    #phones = [18575670303,18588201231,15626585681]
    #print(phones)
 
    for phone in phones:
        try:
            city = p.find(phone)['city']
            province = p.find(phone)['province']
            print("%s %s %s" % (phone, province, city))
        except:
            pass
if __name__ == '__main__':
    for line in open('nihao.txt','r'):
        if line.strip():
            line=line.strip('\n')
            phones=[line]
            #print(phones)
            get_info(phones)
    
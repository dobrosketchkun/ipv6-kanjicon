import pickle
import random
import ipaddress

def dec2hex(dec):
	return hex(dec).split('x')[-1]

jap_kanji = pickle.load( open( "kanji.p", "rb" ))
j_len = len(jap_kanji)

def rand_ipv6():
	return str(ipaddress.IPv6Address(random.randint(0, 2**128-1)))

ipv6 = rand_ipv6()
#print(ipv6)
ip6_p = ipv6.split(':')

kanji1 = divmod((int(ip6_p[0],16) + int(ip6_p[1],16) + int(ip6_p[2],16) + int(ip6_p[6],16) + int(ip6_p[7],16)),j_len)[1] 
kanji2 = divmod((int(ip6_p[1],16) + int(ip6_p[2],16) + int(ip6_p[3],16) + int(ip6_p[6],16) + int(ip6_p[7],16)),j_len)[1]  
kanji3 = divmod((int(ip6_p[2],16) + int(ip6_p[3],16) + int(ip6_p[4],16) + int(ip6_p[6],16) + int(ip6_p[7],16)),j_len)[1]  
kanji4 = divmod((int(ip6_p[3],16) + int(ip6_p[4],16) + int(ip6_p[5],16) + int(ip6_p[6],16) + int(ip6_p[7],16)),j_len)[1]  
#print (kanji1, kanji2, kanji3, kanji4)


kanji1_color = divmod(((int(ip6_p[0],16) + int(ip6_p[1],16) + int(ip6_p[2],16)) * (int(ip6_p[6],16) + int(ip6_p[7],16))),int('ffffff',16))[1] 
kanji2_color = divmod(((int(ip6_p[1],16) + int(ip6_p[2],16) + int(ip6_p[3],16)) * (int(ip6_p[6],16) + int(ip6_p[7],16))),int('ffffff',16))[1] 
kanji3_color = divmod(((int(ip6_p[2],16) + int(ip6_p[3],16) + int(ip6_p[4],16)) * (int(ip6_p[6],16) + int(ip6_p[7],16))),int('ffffff',16))[1] 
kanji4_color = divmod(((int(ip6_p[3],16) + int(ip6_p[4],16) + int(ip6_p[5],16)) * (int(ip6_p[6],16) + int(ip6_p[7],16))),int('ffffff',16))[1] 
#print (kanji1_color, kanji2_color, kanji3_color, kanji4_color)


text = '''
<style type="text/css">
p {
  margin-bottom: -22px; /* between paragraphs */
  }
w1 {
  font-size: 160px;
  color: #''' + dec2hex(kanji1_color) + dec2hex(kanji2_color)[0:2] + ';' + '''
  background-color:#''' + dec2hex(kanji2_color)[0:2]  +  dec2hex(kanji1_color)[6::-1] + ';' +'''
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: white;
  font-weight: 900;
}
''' + '''
w2 {
  font-size: 160px;
  color: #''' + dec2hex(kanji2_color) + dec2hex(kanji3_color)[0:2] + ';' + '''
  background-color:#''' + dec2hex(kanji3_color)[0:2] + dec2hex(kanji2_color) + ';' + '''
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: white;
  font-weight: 900;
}
''' + '''
w3 {
  font-size: 160px;
  color: #''' + dec2hex(kanji3_color) + dec2hex(kanji4_color)[0:2] + ';' + '''
  background-color:#'''+ dec2hex(kanji4_color)[0:2] + dec2hex(kanji3_color) + ';' +'''
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: white;
  font-weight: 900;
}
''' + '''
w4 {
  font-size: 160px;
  color: #''' + dec2hex(kanji4_color) + dec2hex(kanji1_color)[0:2] + ';' + '''
  background-color:#'''+ dec2hex(kanji1_color)[0:2] + dec2hex(kanji4_color) + ';' +'''
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: white;
  font-weight: 900;
}
</style>
''' + '''
<p>''' + '<w1>' + jap_kanji[kanji1]+ '</w1>' + ' ' +\
 '<w2>' + jap_kanji[kanji2] + '</w2>' +'''</p>
<p>''' + '<w3>' + jap_kanji[kanji3]+ '</w3>' + ' ' +\
 '<w4>' + jap_kanji[kanji4] + '</w4>' + '</p>'

with open('kanjicon.html', 'w', encoding='utf-8') as f:
    for item in text:
        f.write("%s" % item)

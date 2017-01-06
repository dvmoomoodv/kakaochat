#-*- coding: utf-8 -*-
import codecs, re
readFile = codecs.open( "KakaoTalkChats.txt", "r", "utf-8")
line = readFile.read()
# print(line)
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
print(urls)

#Kakao File Link
writeFile = codecs.open( "KakaoFileLink.txt", "w", "utf-8")
for data in urls:
    writeFile.writelines(data+'\n')

writeFile.close()
readFile.close()

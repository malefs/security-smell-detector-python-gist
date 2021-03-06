"""
The basic idea is that I loop through all characters and count the number of 
pixels and make <Hashtable number of pixels as a key and character as value>

The table will not have 255 value so to cover this I had to calculate the 
slope of change as a base step for the colors.
example, 	if we have 50 value and we need 255 value, then each 255/50 = 5.1
			Then with each gray color we will devied by 5 so we have index to
			be fetched from the keys of the pixels table

Looping through the photo pixels and converting it to Gray scale and devide
using the base step, now you will have a character
"""

from PIL import Image, ImageDraw
import sys

def pix_in_char(c):
    size = (10,10)
    im = Image.new('RGB', size)
    draw = ImageDraw.Draw(im)
    white = (255,255,255)
    text_pos = (0,0)
    draw.text(text_pos, c+c, fill=white)
    
    del draw
    pix = im.load()
    cid = 0
    for x in range(10):
        for y in range(10):
            cid = cid if pix[x,y][0]==0 else cid + y
    return cid

pix_in_char_table = {}

for i in range(255):
    character = chr(i)
    pix_count = pix_in_char(character)
    pix_in_char_table[pix_count] = character

pix_in_char_table[pix_count] = " "

keys = sorted(list(pix_in_char_table.keys()))
base = int(255/len(pix_in_char_table))

if len(sys.argv)!=2:
    print("Need image name only.")
    exit()

image_name = sys.argv[1]
output_name = image_name.split(".")[0] + "__image_2_ascii__.txt"
im = Image.open(image_name)
pix = im.load()
image_text = ""
for y in range(im.size[1]):
    for x in range(im.size[0]):
        clr = int(sum(pix[x,y])/4)
        image_text += pix_in_char_table[keys[int(clr/base)]]*2
    image_text += "\n"


open(output_name, "w").write(image_text)

"""
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnnnnnnnnnnnnnnnnnnnnnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnnnnnqqllffffffllqqqqqqyynnnnnnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnyyffZZppppppQQppllqqllllllllqqyynnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnnnllppQQQQQQppppQQppllqqllllllllllllqqnnnnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnyyZZppQQppppppppppQQppllllllllllllllllllqqyynnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnyyZZQQppppppppppppppQQppllqqllllllllllllllllllyynnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnyyZZQQppppppppppppppppQQppllqqllllllllllllllllllllyynnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnnnZZQQppppppppppppppppppQQppllqqllllllllllllllllllllqqnnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnffQQppppppppppppppppppppQQppllqqllllllllllllllllllllllqqnnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnllppQQppppppppppppppppppppQQppllqqllllllllllllllllllllllqqyynnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnyyZZQQppppppppppppppppppppppQQppllqqllllllllllllllllllllllllqqnnnnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnffQQppppppppppppppppppppppppQQppllqqllllllllllllllllllllllllllyyxxyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnqqppQQppppppppppppppppppppppppQQppllqqllllllllllllllllllllllllllllnnxxyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnZZQQppppppppppppppppppppppppppQQppllqqllllllllllllllllllllllllllllqqssnnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyynnllppQQppppppppppppppppppppppppppQQppllqqllllllllllllllllllllllllllllllyyssnnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyynnnnZZQQppppppppppppppppppppppppppppQQppllqqllllllllllllllllllllllllllllllqqxxxxnnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyynnllppppppppppppppppppppppppppppppppQQppllqqllllllllllllllllllllllllllllllllyyssnnnnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyynnnnZZQQppppppppppppppppppppppppppppppppppllqqllllllllllllllllllllllllllllllllqqxxxxnnnnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyynnllppppppppppppppppppppppppppQQQQQQQQQQQQffffffllllllllllllllllllllllllllllllllyyssxxxxnnyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyynnZZQQppppppppppppppppppQQQQQQddddddddddddZZZZZZffffffffllllllllllllllllllllllllqqxxxxnnnnnnyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyynnllppQQppppppppppppQQQQQQddddddddddddddddddZZZZZZZZffffffffffffllllllllllllllllllllnnssxxnnnnnnyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyynnZZQQppppppppppppQQddddddddddddddddddddddddZZZZZZZZZZffffffffffffffllllllllllllllllqqssxxxxnnnnnnyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyynnllppQQppppppQQQQQQddddddddddddddddddddddddddZZZZZZZZZZZZffffffffffffffffllllllllllllllnnssxxnnnnnnnnyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyynnZZQQppppppQQppppddddddddddddddddddddddddddddZZZZZZZZZZZZZZZZffffffffffffffllllllllllllyyssxxxxnnnnnnnnyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyynnqqppQQppppQQppqqZZddddddddddddddddddddddddddddZZZZZZZZZZZZZZZZZZffffffffffffffllllllllllqqnnssxxxxnnnnnnnnyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyynnffQQppppQQppyyyyZZddddddddddddddddddddddddddddZZZZZZZZZZZZZZZZZZZZZZffffffffffyyqqllllllllyyssxxxxnnnnnnnnnnyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyynnyyppQQppppQQqq??yyZZddddddddddddddddddddddddddddZZZZZZZZZZZZZZZZZZZZZZZZZZffffllwwxxllllllllqqxxxxxxxxnnnnnnnnyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyynnllppppppQQZZcc??xxZZddddddddddddddddddddddddddddZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZqqccvvyyllllllllyyssxxxxnnnnnnnnnnyyyyyyyyyyyy
yyyyyyyyyyyyyynnnnZZQQppppQQqq????ccffddddddddddddddddddddddddddddZZZZZZZZZZZZZZZZZZZZZZZZZZZZffnnxxssnnllllllllqqssxxxxxxnnnnnnnnnnyyyyyyyyyy
yyyyyyyyyyyyyynnqqppQQppQQppss??wwxxllQQddddddddddddddddddddddddddZZZZZZZZZZZZZZZZZZZZZZZZZZZZllxxxxxxxxqqllllllllnnssxxxxnnnnnnnnnnnnyyyyyyyy
yyyyyyyyyyyyyynnffQQppppQQZZvvssqqqqqqppddddddddddddddddddddddddddZZZZZZZZZZZZZZZZZZZZZZZZZZZZnnssssccccyyllllllllyyssxxxxnnnnnnnnnnnnyyyyyyyy
yyyyyyyyyyyynnyyppQQppppQQffssyynnxxccffddddddddddddddddddQQppppZZqqqqllffZZZZZZZZZZZZZZZZZZllssxxxxcc??nnllllllllqqxxxxxxxxnnnnnnnnnnnnyyyyyy
yyyyyyyyyyyynnllppppppppQQllvvcc??????qqddddddddddddddddppffffffllxxssxxxxqqZZZZZZZZZZZZZZZZnnvvssxxjj??nnllllllllllyyssxxxxnnnnnnnnnnnnnnyyyy
yyyyyyyyyyyynnZZQQppppppQQqq??????cc??xxQQddddddddddddppffffffffllxxssssssssqqZZZZZZZZZZZZffww??vvvvcc??xxllllllllllqqssxxxxxxnnnnnnnnnnnnyyyy
yyyyyyyyyynnqqppQQppppppQQqq??vvcc??wwyyZZddddddddddQQffffffZZZZZZyynnnnxxssxxffZZZZZZZZZZyy??vvvv??vv??xxllllllllllqqnnssxxxxnnnnnnnnnnnnnnyy
yyyyyyyyyynnffQQppppppppQQqq??vv??ccyyqqqqppddddddddppffffppddddQQZZffZZllxxssyyZZZZZZZZlljj??vvvvvvvv??nnllllllllllllyyssxxxxxxnnnnnnnnnnnnyy
yyyyyyyyyynnZZQQppppppppQQll????wwnnyywwjjffppQQQQppffffZZQQppppZZqqyyqqffyyssxxllffffqqxxcc??vvvvvvvv??nnllllllllllllqqxxxxxxxxnnnnnnnnnnnnnn
yyyyyyyyyynnZZQQppppppppQQff????jjjj??vvxxllffffffffffffZZffllffllxxjjjjnnyyxxxxxxnnxxssjjvv??vv??vv????yyllllllllllllqqssxxxxxxnnnnnnnnnnnnnn
yyyyyyyyyynnllppppppppppQQZZjj??vv??ccssssxxffffffffffffffffffffffnnxxxxssssxxxxxxssxxxxww??vvvv??vv??ccqqllllllllllllyyssxxxxxxxxnnnnnnnnnnnn
yyyyyyyyyynnyyppQQppppppQQppnn??vvvvvvvv????qqffffffffffffffffffffnnssxxxxxxxxxxxxxxxxss????vvvv??vv??ssllllllllllllqqxxssxxxxxxxxnnnnnnnnnnnn
yyyyyyyyyyyynnffQQppppppppQQll??vvvv????vv??jjllffffffffffffffffffnnssxxxxxxxxxxxxxxxxcc??vv??vvvvvv??nnllllllllllllyyssxxxxxxxxxxxxnnnnnnnnnn
yyyyyyyyyyyynnqqppQQppppppQQZZww??vvvvvvvvvv??nnffffffffffffffffffnnssxxxxxxxxxxxxxxjj??vvvvvv??vv??ccqqllllllllllqqnnssxxxxxxxxxxxxnnnnnnnnnn
yyyyyyyyyyyyyynnZZQQppppppQQppnn??vvvv????vv????yyffffffffffffffffnnssxxxxxxxxxxxxjj????vv??vv??vv??ssqqllllllllllqqssxxxxxxxxxxxxxxnnnnnnnnnn
yyyyyyyyyyyyyynnqqppQQppppppQQll??vvvvvvvv??vv????qqffffffffffffffnnssxxxxxxxxxxssvv??vv??vvvvvvvv??nnllllllllllllnnssxxxxxxxxxxxxxxnnnnnnnnnn
yyyyyyyyyyyyyyyynnZZQQppppppQQZZ????vvvvvvvv??vv??vvyyffffffffffffnnssxxxxxxxxssvv??vv??vvvv??vv????yyllllllllllqqssxxxxxxxxxxxxxxxxnnnnnnnnnn
yyyyyyyyyyyyyyyynnqqppQQppppQQppss??vv??vvvvvv??vv????nnffffffffllnnssxxxxxxjj????vv??vvvvvv??vv??wwqqllllllllllnnssxxxxxxxxxxxxxxxxnnnnnnnnnn
yyyyyyyyyyyyyyyyyynnffQQppppQQppnn??cc??vvvvvvvv??vv????ssqqffZZffnnxxxxssww????vv??vvvvvvvvvvvv??ssllllllllllyyssxxxxxxxxxxxxxxxxnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyynnyyppQQppppQQll??ccvvvvvvvvvvvv??vvvv????ssqqllxxjjww????vvvv??vvvvvvvv??vvvv??nnllllllllqqxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyynnllppQQppQQff????vvvvvvvvvvvvvv??vvvv??????wwcc??????vvvv??vvvvvvvvvv??vv????yyllllllllnnssxxxxxxxxxxxxxxxxnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyynnffQQppQQZZww??vv??vvvvvvvvvvvv????vvvv????????vvvvvvvvvvvvvvvvvvvv??vv??ccqqllllllyyssxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyynnnnZZQQQQppss??cc??vvvvvvvvvvvvvvvv????vvvvvvvvvv??vvvvvvvvvvvvvvvv??vv??wwqqllllqqxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyynnyyZZQQppnn??cc??vvvvvvvvvvvvvvvvvvvv????vvvvvvvvvvvvvvvvvvvvvvvvvvvv??jjqqllqqxxssxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyynnqqppQQyy??cc??vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv??ssllqqnnssxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyynnllppqq??cc??vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv??vvvv??xxllnnssxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnllqq??vvvv??vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv??vv????xxnnssxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnnnjj????vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv????wwssssxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnss????vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv??vvjjxxxxxxxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyxxcc????vvvvvv??vvvvvvvvvvvvvvvvvvvvvvvvvvvv????wwssxxxxxxxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyxxjjcc????vvvvvvvv????vvvv????vvvvvvvv????ccjjxxxxxxxxxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnssjjcc??????vvvvvvvvvvvvvvvv??????ccjjssxxxxxxxxxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnxxssjjcc????????????????????ccjjssxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnxxxxxxssjjccvv????vvccjjssxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnxxxxxxxxxxssssssssxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyynnnnnnxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn

"""
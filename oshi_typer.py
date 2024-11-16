import keyboard



oshi_dict_index=['ayumu','kasumi','shizuku','karin','ai','kanata','setsuna','emma','rina','shioriko','mia','lanzhu','yu',#Nijigasaki
                 'kanon','keke','chisato','sumire','ren','kinako','mei','shiki','natsumi','wien','tomari',#Liella
                 'kaho','kozue','tsuzuri','sayaka','rurino','megumi','ginko','kosuzu','hime',#Hasunosora
                 'chika','riko','kanan','dia','you','youshiko','hanamaru','mari','ruby','xdnhx']#Aqours

oshi_dict_word={
    'ayumu':'🎀',
    'kasumi':'👑',
    'shizuku':'💧',
    'karin':'👠',
    'ai':'🙏',
    'kanata':'🐏',
    'setsuna':'🎙️',
    'emma':'🍞',
    'rina':'📶',
    'shioriko':'🔖',
    'mia':'🐇',
    'lanzhu':'🪽',
    'yu':'𝄞⨾𓍢ִ໋',#Nijigasaki
    'kanon':'🎧',
    'keke':'🍦',
    'chisato':'🍡',
    'sumire':'🪐',
    'ren':'☕',
    'kinako':'🦊',
    'mei':'🐾',
    'shiki':'🧪',
    'natsumi':'🥤',
    'wien':'🦋',
    'tomari':'🪼',#Liella
    'kaho':'🐰',
    'sayaka':'⏰',
    'kozue':'💽',
    'tsuzuri':'🐧',
    'rurino':'🔋',
    'megumi':'🎤',
    'ginko':'🦢',
    'kosuzu':'🏏',
    'hime':'🏆',#Hasunorora
    'chika':'🍊',
    'riko':'🎹',
    'kanan':'🐬',
    'dia':'🌸',
    'you':'⛵',
    'yoshiko':'🦇',
    'hanamaru':'💮',
    'mari':'✨',
    'ruby':'🍭',#Aqours
    'xdnhx':'😊🖕️'
}

koi = '''言いたいことがあるんだよ！
やっぱ{}ちゃんはかわいいよ！
好き好き大好きやっぱ好き！
やっと見つけたお姫様！
俺が生まれてきた理由！
それはお前に出会うため！
俺と一緒に人生歩もう！
世界で一番愛してる！
ア・イ・シ・テ・ルーーー！
'''


print("Type something and press Space. Type end to exit.")
print('本程序基于英语输入法使用，请在键入角色emoji时切换至英语输入法。本程序纯属娱乐，请勿在可能造成损失的生产环境下使用。输入end以退出程序。使用案例：输入ayumu+空格，输出🎀。ayumukoi对应ayumu恋口上。')
print('Reference:https://www.reddit.com/r/LoveLive/comments/186avrq/does_yu_takasaki_not_have_a_symbol/')
print('https://www.lovelive-anime.jp/nijigasaki/worldwide/member.php')
print('https://www.paradisearmy.com/doujin/pasok_gachikoikoujyou.htm')



i=True
while i==True:
    typed_string=keyboard.get_typed_strings(keyboard.record(until='space'))
    for typed_string in typed_string:
         text=typed_string
    text=str(text)
    true_length=len(text)
    text=text[0:(len(text)-1)]
    print(text)
    if text == 'end':
        i=False
        keyboard.write('程序已中止')
        break
    for j in range(0,len(oshi_dict_index)):
        if text == str(oshi_dict_index[j]):#check if the input is a name in list
            for h in range(0,true_length):
                keyboard.send('backspace')
            keyboard.write(oshi_dict_word[text])
    for k in range(0,len(oshi_dict_index)):
        if text == str(oshi_dict_index[k]+'koi'):#gachikoi program
            for r in range(0,true_length):
                keyboard.send('backspace')
            keyboard.write(koi.format(oshi_dict_word[oshi_dict_index[k]]*3))

print('Program ended')







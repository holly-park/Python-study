colours = {'red':'apple', 'green':'kiwi', 'yellow':'mango','orange':'orangefruits','pink':'peach' }
print(colours)

print(colours['red'])
print(colours['green'])
print(colours['yellow'])

#새로운 키 추가
#존재하면 덮어쓰고 존재하지 않으면 새로 만듬
colours['brown']='jackfruits'
colours['red']='strawberry'
print(colours)

personinfo=dict()
#처음에 데이터없이 객체만 만든다
personinfo['name']='lydia'
personinfo['nickname']='starfish'
personinfo['school']='brdsch'

print(personinfo)
print(personinfo.get('name'))
#print(personinfo.['name'])도 똑같다


print(colours.keys())#키 리스만만
print(colours.values())#값 리스트만
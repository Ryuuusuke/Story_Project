# Madlibs Game
# This is my Practice python


Name = input('お名前は誰ですか？ :')

# Story
print ((f'こんにちは！ {Name}'))
age = input('何歳ですか？ : ')
print (f'わあ、わかいねえ{age}なんて')
mono = input('それ、なに？： ')
print (f'あ、{mono}か')
henji1 = input('重そうに見えるんだけど、半分私がもちましょうか？ (はい / いいえ)： ')
if henji1 == 'はい':
    print('任せて！')
elif henji1 == 'いいえ':
    print('ばか')
else:
    print('よくわからないけど、頑張って！')

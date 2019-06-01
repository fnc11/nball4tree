def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def find_unknown_words():
    with open('catCodes.txt','r') as catCodef, open('/home/fnc11/HindiTest/wordEmbs.txt', 'r') as word_embsf:
        words = []

        for line in catCodef.readlines():
            wlst = line.split()
            words.append(wlst[0])
        # words.remove("/*root/*")

        word_embs_cont = word_embsf.read()
        word_embs = word_embs_cont.split('$')

        unknownWords = list(set(word_embs[:-1]).difference(set(words[:-1])))

        eng_words = []
        for word in unknownWords:
            if isEnglish(word):
                eng_words.append(word)

        for eword in eng_words:
            unknownWords.remove(eword)


        with open('unknownWords.txt', 'w') as unknownf, open('wordList.txt', 'w') as wordlistf:
            unknownf.write('\n'.join(unknownWords) + '\n')
            wordlistf.write('\n'.join(words[:-1])+'\n')
import pickle

# Loading input dictionaries
word2synsets = pickle.load(open("WordSynsetDict.pk", 'rb'))
#synset2words = pickle.load(open("SynsetWords.pk", 'rb'))
synset2hypes = pickle.load(open("SynsetHypernym.pk", 'rb'))

# All the paths from the leaf/word to root will be printed in tree_struct.txt
tree_struct = open("tree_struct.txt", 'w+')

"""
This function assigns one special char to each word type in the wordnet. 
	1: n (noun), 2: j (Adjective), 3: v (verb), 4: a (Adverb)
"""


def assign_alpha(num):
    if num == "1":
        return "n"
    elif num == "2":
        return "j"
    elif num == "3":
        return "v"
    else:
        return "r"


""" 
Compares the words from the Hindi Wordnet and the Hindi Word-embeddings, and keeps track of the synsets which 
contains the words which are not in the word-embeddings so that they can be removed later from the Hindi Wordnet.
"""

# Synsets of the words which are not in the word-embeddings file.
to_remove = set()

# Synsets of the commen words between the both files.
to_keep = set()

# embwords.txt contains all the words which are present in the Hindi Word embeddings file
# sets2remove.txt contains all the synsets which needs to be removed from the Hindi Wordnet
with open("/home/lab-mueller/Documents/AILab/wordEmbs.txt", 'r') as emb_word_f, open("sets2remove.txt", 'w') as inspectf:
    embedding_content = emb_word_f.read()
    bwords = embedding_content.split("$")
    print(len(bwords))
    # count = 0
    # first creating two sets one set for all the sets which are going to be removed.
    # second mapping for the sets which definitely have some words in the ball embeddings
    wordsto_remove = []
    for word, value in word2synsets.items():
        normword = word.strip(" ")
        # print(normword)
        # check if the words from wordnet are present in the embedding words
        if normword in bwords:
            print("prs")
            # count += 1
            for typ, lis in value.items():
                for i in range(0, len(lis)):
                    # why not save type
                    to_keep.add(lis[i])
        else:
            wordsto_remove.append(word)
            print("abs")
            for typ, lis in value.items():
                for i in range(0, len(lis)):
                    to_remove.add(lis[i])

    # removing the words from word2synsets Dictionary
    # this ensure we don't persue paths for such words
    for i in range(0, len(wordsto_remove)):
        del word2synsets[wordsto_remove[i]]

    # Ensuring sets that need not to be removed
    amgsset = set()
    for set in to_remove:
        if set in to_keep:
            amgsset.add(set)
    # removing these amg sets from to_remove
    # print(amgsset)
    for set in amgsset:
        to_remove.remove(set)

    # if some set in to_keep by some word
    inspectf.write(" ".join(to_remove))


def printUptoRoot(sen, key, wordtype):
    key_exp = {}
    # path length
    count = 0
    tlen = 0
    while (True):
        if key not in key_exp:
            key_exp[key] = True
            sen += "<-" + str(key)
            tlen += 1
            # reminder take len1 words
            if key in synset2hypes:
                # check here wordtype not used
                if int(wordtype) in synset2hypes[key].keys():
                    lis = synset2hypes[key][int(wordtype)]
                    key = lis[0]
                    for i in range(0, len(lis)):
                        # we could do the to_remove check here for better results
                        if lis[i] not in to_remove:
                            key = lis[i]
                            break
                else:
                    print("Rare case!")
                    # reminder why not add them directly to the root
                    for typ, lis in synset2hypes[key].items():
                        lis = synset2hypes[key][int(typ)]
                        key = lis[0]
                        to_break = False
                        for i in range(0, len(lis)):
                            # we could do the to_remove check here for better results
                            if lis[i] not in to_remove:
                                to_break = True
                                key = lis[i]
                                break
                        if to_break:
                            break
            else:
                # Analyze this path and remove the sets which belongs to to_remove set
                tokens = sen.split("<-")
                newsen = tokens[0]
                for i in range(1, len(tokens)):
                    if tokens[i] not in to_remove:
                        newsen += "<-" + str(tokens[i])
                    else:
                        count += 1
                if (tlen > 1):
                    tree_struct.write(newsen + "$")
                break
        else:
            break
    return count


wordList = []
sentence = ""
num = 0
modernSyn2Words = {}
count = 0
for word, value in word2synsets.items():
    # num += 1
    for typ, lis in value.items():
        alpha = assign_alpha(typ)
        for i in range(0, len(lis)):
            # print(word)
            wordversion = word + "." + alpha + "." + "{:02d}".format(i+1)

            # if the set already exist in the modernSyn2Words just add this word also
            # otherwise add new list with this word
            if lis[i] in modernSyn2Words.keys():
                modernSyn2Words[lis[i]].append(wordversion)
            else:
                modernSyn2Words[lis[i]] = [wordversion]

            count += printUptoRoot(wordversion, lis[i], typ)
            # printHch(sentence, lis[i], 0)
            # wordList.append((key+alpha+str(i+1), lis[i]))
    # if num == 1000:
    #     break
print("Total sets removed:{}".format(count))
tree_struct.write("root")

with open("set2WordV.txt", 'w') as s2w:
    for set, values in modernSyn2Words.items():
        s2w.write(str(set) + ":" + values[0] + "$")
    s2w.write("root:root")

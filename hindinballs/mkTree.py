import random
from util import Tree

root = Tree("root")
allNodes = {"root": root}

set2Word = {}
word2Set = {}

with open("set2WordV.txt","r") as s2w:
    cont = s2w.read()
    sets = cont.split("$")
    for set in sets:
        pairs = set.split(":")
        num = pairs[0]
        word = pairs[1]
        set2Word[num] = word
        word2Set[word] = num

# final cleansing of the paths
paths = []
clean_paths = []
with open("tree_struct.txt", 'r') as tree_struct:
    struct_cont = tree_struct.read()
    paths = struct_cont.split("$")
    # count = 0
    for path in paths:
        tokens = path.split("<-")
        num_of_tokens = len(tokens)
        new_path = tokens[0]
        for i in range(1, num_of_tokens):
            if tokens[i] in set2Word.keys():
                new_path += "<-" + tokens[i]
        clean_paths.append(new_path)

    for path in clean_paths:
        tokens = path.split("<-")
        # print(tokens)
        num_tokens = len(tokens)
        # saving prev_token to save it's child if they don't exist already
        prev_token = tokens[num_tokens - 1]
        # remember to leave last set, need to replace it with actual word
        for i in range(0, num_tokens - 2):
            name = str(tokens[num_tokens - 1 - i])
            # to avoid index out of bound error
            if i > 0:
                prev_token = tokens[num_tokens - i]
            if name in allNodes.keys():
                continue
            else:
                # create new node and save it's mapping in the allNodes dict
                temp = Tree(name)
                allNodes[name] = temp
                if i == 0:
                    # if it's the node that goes below root
                    allNodes["root"].add_child(temp)
                else:
                    # if it is some other node's child, other than root(prev_token's)
                    allNodes[prev_token].add_child(temp)
        # now for the last node, as word
        name = str(tokens[0])
        # if the word is not directly attached to the root
        if num_tokens >= 3:
#            child_found = False
#            child_nodes = allNodes[tokens[2]].children
#            for child in child_nodes:
#                if child.name == name:
#                    child.add_child(temp)
#                    child_found = True
#                    break;
#            if not child_found:
#                allNodes[tokens[2]].add_child(temp)
            if name in word2Set.keys():
                name = word2Set[name]
            if name not in allNodes.keys():
                temp = Tree(name)
                allNodes[name] = temp
                allNodes[tokens[2]].add_child(temp)
        else:
            if name in word2Set.keys():
                name = word2Set[name]
            if name not in allNodes.keys():
                temp = Tree(name)
                allNodes[name] = temp
                allNodes["root"].add_child(temp)

# levelDict = root.printLevelOrder()
# print(levelDict)


"""No needed for now
# print(wordAndOrderDict)
# Now replace set in the levelDict with word and sort them, and replace the -1 in the wordAndOrderDict
# with correct place
setOrderNum = {'root': 1 }
with open("sameLevelWords.txt", "w") as slw:
    stck =[root]
    while(True):
        if len(stck) != 0:
            temp = stck.pop(0)
            if len(temp.children) > 0:
                o_list = temp.children
                c_list  = []
                for child in o_list:
                    word_name = child.name
                    if child.name in set2Word.keys():    
                        word_name = set2Word[child.name]
                    c_list.append(word_name)
                    stck.append(child)
                c_list.sort()
                k=0
                for i in c_list:
                    k=k+1
                    if i in word2Set.keys():
                        setOrderNum[word2Set[i]] = k
                    else:
                        setOrderNum[i] = k
        else:
            break
        slw.write("\n\n")




# printing cat codes of all the words in a file
with open("catCodes.txt", "w") as ctcd:
    # count = 0
    # A dictionary to hold all the words whose cat_codes are already generated
    cat_printed = {}
    for path in clean_paths:
        tokens = path.split("<-")
        num_of_tokens = len(tokens)
#        for i in range(0, num_of_tokens):   
#            if i==1:
#                continue
#            word = tokens[i]
#            if word in set2Word.key():
#                word = set2Word[word]
#            sen = ""
#            if word not in cat_printed:
#                if word in word2Set.keys():
#                    sen = str(setOrderNum[word2Set[tokens[i]]])+" "+sen
#                # discussion need to be done here
#                elif word in setOrderNum.keys():
#                    # count += 1
#                    sen = str(setOrderNum[tokens[i]])+" "+sen
#                else:
#                    print("Evil case")
#                    continue

        for j in range(0, num_of_tokens):
            leaf = tokens[j]
            if leaf in set2Word.keys():
                leaf = set2Word[leaf]
            if leaf not in cat_printed:
                cat_printed[leaf]=True
                sen = ""
                slen = 0
                for i in range(j, num_of_tokens):
                    if j==0 and i==1:
                        slen = 1
                        continue
                    word = tokens[i]
                    if word in set2Word.keys():
                        word = set2Word[word]
                    if word in word2Set.keys():
                        sen = str(setOrderNum[word2Set[word]])+" "+sen
                    # discussion need to be done here
                    elif word in setOrderNum.keys():
                        # count += 1
                        sen = str(setOrderNum[word])+" "+sen
                    else:
                        print("Evil case")
                        continue
                # root order for every word
                # need to add special case for root*
                sen = "1 "+sen.strip()
                for k in range(0, 13-(num_of_tokens-j-slen)):
                    sen += " 0"
                ctcd.write(leaf+" "+sen+"\n")
    # print(count)




# root.printTree()
# printing word sense children file as English
with open("wordSenseChildren.txt","w") as wsc:
    stck = [root]
    while (True):
        if len(stck) != 0:
            temp = stck.pop(0)

            if temp.name in set2Word.keys():
                wsc.write(set2Word[temp.name])
            else:
                wsc.write(temp.name)

            if len(temp.children) > 0:
                for child in temp.children:
                    stck.insert(0, child)
                    if child.name in set2Word.keys():
                        wsc.write(" "+set2Word[child.name])
                    else:
                        wsc.write(" "+child.name)

            wsc.write("\n")
        else:
            break

"""


def print_node_children(fixnum):
    # read the 900 nodes file
    with open("prs.txt",'r') as alf, open("nodechildren.txt",'w') as nodechildf:
        cont = alf.read()
        lines = cont.split('\n')
        num = len(lines)
        count = 0
        for i in range(0, num):
            count += 1
            tect = lines[i].split(':')
            fin = tect[1].strip()
            node_children_set = allNodes[fin].node_and_children()
            node_children_list = []
            for st in node_children_set:
                try:
                    node_children_list.append(set2Word[st])
                except KeyError:
                    node_children_list.append(st)
            nodechildf.write(' '.join(node_children_list) + '\n')
            if count >= fixnum:
                break


# Making a random selection out of dictionary and checking if it has childrens more than 10
def find_node_with_children(fixnum, sz):
    count = 0
    selected = {}
    with open("selected_new.txt", 'w') as examf:
        while True:
            picked, node = random.choice(list(allNodes.items()))

            if picked not in selected.keys() and allNodes[picked].child_size(sz) > sz:
                count += 1
                print("Found "+str(count)+": "+picked)
                selected[picked] = True
                examf.write(":"+picked+"\n")

            if count == fixnum:
                break

    # print(allNodes)
    print(selected)


def convert_st_to_word_paths():
    with open("paths_with_sets.txt",'r') as filest, open("paths_with_words.txt", 'w') as filepths:
        cont = filest.read()
        lines = cont.split('\n')
        for line in lines[:-1]:
            # print(line)
            sts = line.strip().split()
            sts[-1] = "*root*"
            num = len(sts)
            for i in range(0, num-1):
                try:
                    sts[i] = set2Word[sts[i]]
                except KeyError:
                    continue
            filepths.write(' '.join(sts) + '\n')

# with open("paths_with_sets.txt",'w') as filest:
#     root.print_all_paths("", filest)

convert_st_to_word_paths()




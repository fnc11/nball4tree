class Tree(object):
    # "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def printTree(self):
        assert isinstance(self, Tree)
        stck = [self]
        while(True):
            if len(stck) != 0:
                temp = stck.pop(0)
                print(temp.name)
                if len(temp.children) > 0:
                    for child in temp.children:
                        stck.insert(0, child)
            else:
                break

    def printLevelOrder(self):
        assert isinstance(self, Tree)
        que = [self]
        nums_at_level = 1
        levelNum = 0
        # maxLevel = -1
        levelDict = {0:[]}
        for i in range(1,15):
            levelDict[i]=[]
        count = 0
        while(True):
            if nums_at_level == 0:
                # print("level: "+str(levelNum))
                # if levelNum > maxLevel:
                #     maxLevel = levelNum
                levelNum += 1
                nums_at_level = count
                count = 0

            if len(que) != 0:
                nums_at_level -= 1
                temp = que.pop(0)
                # print(temp.name)
                levelDict[levelNum].append(temp.name)
                if len(temp.children) > 0:
                    for child in temp.children:
                        que.append(child)
                        count += 1
            else:
                break
        return levelDict
        # print(maxLevel)

    def child_size(self, sz):
        assert isinstance(self, Tree)
        clist = len(self.children)
        count = 0
        for i in range(0, clist):
            if count > sz:
                return count
            count += self.children[i].size(sz)
        return count+1

    def node_and_children(self):
        assert isinstance(self, Tree)
        stck = [self]
        child_list = []
        while len(stck) != 0:
            node = stck.pop()
            child_list.append(node.name)
            for child in node.children:
                stck.append(child)
        return child_list

    def print_all_paths(self, path, filest):
        assert isinstance(self, Tree)
        new_path = self.name+" "+path
        # print(new_path)
        filest.write(new_path+"\n")
        if len(self.children)!= 0:
            for child in self.children:
                child.print_all_paths(new_path, filest)


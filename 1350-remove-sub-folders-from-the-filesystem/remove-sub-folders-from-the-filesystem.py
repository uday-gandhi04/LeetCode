class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort(key=lambda x:len(x))
        folders=set()
        out=[]
        for f in folder:
            names=list(f.split('/'))
            temp=[]
            flag=True
            for name in names:
                temp.append(name)
                if '/'.join(temp) in folders:
                    flag=False
                    break
            
            if flag:
                folders.add('/'.join(temp))
                out.append('/'.join(temp))
        return out


        
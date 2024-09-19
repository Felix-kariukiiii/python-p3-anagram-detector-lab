# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word=word
    def match(self,list=None):
        matching_list=[]
        if list is None:
            return matching_list
        for list in list:
            if (sorted(self.word)==sorted(list)):
                matching_list.append(list)
        return matching_list
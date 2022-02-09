def formSentence(inList,searchChr):
    """
    Checking all words rowwise in list and creating a str contains the first letter of word is same with searched character
    
    Parameters:
    inList(list): the input list
    searchChr(str): the value going to check 
    
    
    returns:
    String : return rev
    
    """
    res = ""
    for i in inList:
        for j in i:
            if j[0].lower() == searchChr.lower():
                res += j+' '
    return res 
        
inList = [['This','is','lab','Script'],['We','should','finish','it'],['we','solve','some','questions']]
print(f'Sentence: {formSentence(inList,"s")}')

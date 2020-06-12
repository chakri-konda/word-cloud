import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    d = {}
    
    def generate_from_frequencies():
        
        string = file_contents.lower()
        
        #Removing the punctuations
        for x in string:
            if x in punctuations:
                string = string.replace(x, '')
                
        word_list = string.split(' ')
        
        #Removing the Uninteresting words
        for word in word_list:
            if word in uninteresting_words:
                word_list.remove(word)
        
        #counting the word frequecies
        for word in word_list:
            if word in d.keys():
                d[word] += 1
            else:
                d[word] = 1
        
        return d
        #print(frequencies)
        
    #wordcloud
    d = generate_from_frequencies()
    
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(d)
    return cloud.to_array()
    


file_contents = ''#add the text data
# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

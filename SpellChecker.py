import sys
import fileinput
# filename = sys.argv

def surround_with(surrounding):
    """Return a function that takes a single argument and."""
    def surround_with_value(word):
        return '{}{}{}'.format(surrounding, word, surrounding)
    return surround_with_value

def file2string():

    content = ""
    for line in fileinput.input():
        content+=line.strip()

    fileinput.close()
    # print content
    return content
	# with open (filename, "r") as myfile:
	# 	data=myfile.read().replace('\n', '')
 #   	print type(data)
def words2list():
    word_list=[]
    try: #attempts to open the file
        with open("words.txt","r") as fin:
            for lines in fin:
                word_list.extend(lines.split())
            return word_list
        
    except: #prints out if file name doesn't exist
        print "Problem loading file"
    
    
    



def transform_words(content, targets, transform):
    """Return a string based on *content* but with each occurrence 
    of words in *targets* replaced with
    the result of applying *transform* to it."""
    result = ''
    for word in content.split():
        if word in targets:
            result += ' {}'.format(word.lower())
        else:
            result += ' {}'.format(transform(word.lower()))
    return result

markdown_string = 'My name is Jeff Knupp and I like Python but I do not own a Python'


markdown_string_italicized = transform_words(file2string(), words2list(),surround_with('$'))
print(markdown_string_italicized)
# except:
#     print "something went wrong"


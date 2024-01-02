
class Node():
  letter = ''
  counter = 0
  children : dict

  def __init__(self):
    self.children = dict()

  def insert(self, data): 
    if len(data) == 0:
      self.counter += 1
    else:
      firstLetter = data[0] 
    
      if firstLetter not in self.children:
        self.children[firstLetter] = Node()
        self.children[firstLetter].letter = firstLetter

      self.children[firstLetter].insert(data[1:])
    
root = Node()

indents = 0

#Prints the nodes as a tree
def printChildren(node):
  global indents
  print( (' ' * indents*2) + f"NODE: {node.letter} - {node.counter}")
  for _,c in node.children.items():
    indents += 1
    printChildren(c)
    indents -= 1

currentPath = ''

#Prints the words with frequency and probability
def printWords(node):
  global currentPath
  global wordCount
  currentPath +=  node.letter
  if (node.counter > 0):
    print(f'{currentPath} ({node.counter}) ({(node.counter/wordCount)*100}%)')

  for _,c in node.children.items():
    printWords(c)
    currentPath = currentPath[:-1]

#Open a file, read the text to allwords and then close the file
file = open('input.txt')
allwords = file.read()
file.close()

#Replacements
allwords = allwords.replace(',', ' ')
allwords = allwords.replace('.', ' ')

wordCount = 0

for word in allwords.split():
  root.insert(word)
  wordCount += 1

printChildren(root)
printWords(root)









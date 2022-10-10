
from math import inf
def prefix_match(dictionary, query):
  #"""Returns the range of words in dictionary which have a prefix matching query"""
  def search(dictionary, query, left, right):
    if(left>right): return[inf, -inf]
    if(right == 1):
      mid = 1
    else:
      mid = (left+right)//2
    length = len(query)
    if(dictionary[mid][0:length]==query):
      result=[mid,mid]
      left_most = min(result[0], search(dictionary, query, left, mid-1)[0])
      right_most = max(result[1], search(dictionary, query, mid+1, right)[1])
      return [left_most, right_most]
    elif (dictionary[mid][0:length] < query):
      return search(dictionary,query, (mid+1), right)
    else:
      return search(dictionary, query, left, mid-1)

  result = search(dictionary, query, 0, (len(dictionary)-1))
  if result[0] == inf: result[0] = -1
  if result[1] == -inf: result[1] = -1
  if result==[-1,-1]: return None
  x = result[0]
  y = result[1] + 1
  return (x,y)

#test
#dictionary = ['beq', 'beqt','beqtie','bes','best', 'better', 'hello']
#query = 'bes'
#print(prefix_match(dictionary, query))



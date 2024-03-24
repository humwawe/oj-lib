class Trie:

  def __init__(self):
    self.sons = {}
    # 记录出现次数，根据要求记录信息
    self.val = 0

  def insert(self, word):
    rt = self
    for c in word:
      if c not in rt.sons:
        rt.sons[c] = Trie()
      rt = rt.sons[c]

    rt.val += 1

  def search(self, word):
    rt = self
    for c in word:
      if c not in rt.sons:
        break
      rt = rt.sons[c]

    return rt.val

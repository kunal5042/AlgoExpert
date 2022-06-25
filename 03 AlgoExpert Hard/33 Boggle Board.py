# O(NM8^S + WS) time and O(NM + WS) space
def boggleBoard(board, words):
    # Write your code here.
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for letter in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())


def explore(i, j, board, trieNode, visited, finalWords):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trieNode:
        return
    visited[i][j] = True
    trieNode = trieNode[letter]
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True
    neighbors = getNeighbors(i, j, board)
    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)
    visited[i][j] = False


def getNeighbors(i, j, board):
    neighbors = []
    if i > 0 and j > 0:
        neighbors.append([i-1, j-1])
    if i > 0 and j < len(board[0]) - 1:
        neighbors.append([i-1, j+1])
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbors.append([i+1, j+1])
    if i < len(board) - 1 and j > 0:
        neighbors.append([i+1, j-1])
    if i > 0:
        neighbors.append([i-1, j])
    if i < len(board) - 1:
        neighbors.append([i+1, j])
    if j > 0:
        neighbors.append([i, j-1])
    if j < len(board[0]) - 1:
        neighbors.append([i, j+1])
    return neighbors


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        board = [
            ["t", "h", "i", "s", "i", "s", "a"],
            ["s", "i", "m", "p", "l", "e", "x"],
            ["b", "x", "x", "x", "x", "e", "b"],
            ["x", "o", "g", "g", "l", "x", "o"],
            ["x", "x", "x", "D", "T", "r", "a"],
            ["R", "E", "P", "E", "A", "d", "x"],
            ["x", "x", "x", "x", "x", "x", "x"],
            ["N", "O", "T", "R", "E", "-", "P"],
            ["x", "x", "D", "E", "T", "A", "E"],
        ]
        words = ["this", "is", "not", "a", "simple", "boggle",
            "board", "test", "REPEATED", "NOTRE-PEATED"]
        expected = ["this", "is", "a", "simple",
            "boggle", "board", "NOTRE-PEATED"]
        actual = boggleBoard(board, words)
        self.assertEqual(len(actual), len(expected))
        for word in actual:
            self.assertTrue(word in expected)
        print("Test Case: Passed")


if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa

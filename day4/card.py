import json

def get_correct_numbers(my_numbers: list, conclusion: list):
    correct_numbers = [x for x in my_numbers if x in conclusion]
    return correct_numbers

def get_score(correct_numbers: list):
    if len(correct_numbers) == 0:
        return 0
    if len(correct_numbers) == 1:
        return 1
    if len(correct_numbers) == 2:
        return 2

    count = 2
    n = len(correct_numbers) -1
    score = 2
    while count <= n:
        score = score * 2
        count += 1

    return score


def get_scratchcards_id(id, card):
    return [id + i + 1 for i in range(len(card))]

def lol(cards, curr, id=1):
    if len(list(curr.values())) == 0:
        return cards, curr

    for key, val in curr.items():
        print(key, val)
        cards[key] = [ lol(cards, {x: cards[x]}) for x in val]

    return cards



class TreeNode():
    def __init__(self, data):
        self.child = []
        self.id = data
        self.parent = None

    def add_child(self,child):
        self.child = child
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p :
            p = p.parent
            level += 1
        return level

    def print_tree(self):
        print('  '*self.get_level() + '|--', end = '')
        print(self.data)
        if self.children:
            for each in self.children:
                each.print_tree()

# # Part 1
# with open("./input.txt") as f:
#     lines = f.read().splitlines()
#     points = []
#     for line in lines:
#         card, game = line.split(":")
#         my_numbers, conclusion = game.split("|")
#         my_numbers = list(filter(lambda x: x, my_numbers.split(" ")))
#         conclusion = list(filter(lambda x: x, conclusion.split(" ")))
#         correct_numbers = [x for x in my_numbers if x in conclusion]
#         points.append(get_score(correct_numbers))
#     print(points)
#     print(sum(points))

# Part 2
# with open("./input2.txt") as f:
#     lines = f.read().splitlines()
#     points = []
#     my_cards = {}
#     for line in lines:
#         card, game = line.split(":")
#         card_id = int(card.split(" ")[1])
#         my_numbers, conclusion = game.split("|")
#         my_numbers = list(filter(lambda x: x, my_numbers.split(" ")))
#         conclusion = list(filter(lambda x: x, conclusion.split(" ")))

#         my_cards[card_id] = get_scratchcards_id(card_id, get_correct_numbers(my_numbers, conclusion))

    # print(lol(my_cards, my_cards))
    # node = TreeNode(s)
    # def recursive(my_cards, node):
    #     for key, val in my_cards.items():
    #         node = TreeNode(key)
    #         card = my_cards[key]
    #         for child in card:
    #             child = node.add_child(TreeNode(child))


    # recursive(my_cards)

cards = open("./input2.txt").readlines()

count = 0
multiplier = [1 for _ in cards]

for i, card in enumerate(cards):
    card = card.split(":")[1].split("|")

    # Parse the winning and have sets
    winning = set([int(x) for x in card[0].strip().split()])
    have = set(int(x) for x in card[1].strip().split())

    # Find the intersection of the two sets
    wins = set(x for x in have if x in winning)

    # Get the multiplier for this card
    cmultiplier = multiplier[i]

    # Set the multiplier for the next cards
    for j in range(i + 1, min(i + len(wins) + 1, len(cards))):
        multiplier[j] += cmultiplier
    count += cmultiplier

print(count)






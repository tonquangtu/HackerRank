
# generate all permutation of input string
# Using Recursive algorithm

s1 = "i love shoppe"
# for (index, c) in enumerate(s):
#     print(index, c)
#
# r_s = []
# r_w = []
#
# for c in s:
#     if c != ' ':
#         r_w.append(c)
#     else:
#         r_w.reverse()
#         r_s.append(r_w)
#         r_s.append(c)
#         r_w = []
#
# print(r_s)
#
#
# a = "I love Shopee"
# r = ''
# for c in a.split():
#     r += ' ' + c[::-1]
# print(r)


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


def create_linked_list2(s):
    ll_nodes = []
    header = None
    pre_node = None

    len_s = len(s)
    node = Node(s[len_s - 1], None)
    pre_node = node
    header = pre_node

    # Create a linked list for store string
    for c in s[len_s - 2:: -1]:
        node = Node(c, pre_node)
        pre_node = node

    # Loop linked list for display string
    while node != None:
        print(node.value)
        node = node.next_node


def create_linked_list(s):
    header = tail = None
    if len(s) < 1:
        return header, tail

    header = node = Node(s[0], None)
    for index in range(1, len(s)):
        post = Node(s[index], None)
        node.next_node = post
        node = post

    tail = node
    return header, tail


def show_ll(header, tail):
    node = header
    s = ''
    while node is not None:
        s += node.value
        node = node.next_node

    print(s)




# lens = len(s1)
# print(lens)
# s2 = s1[11::-1]
# print(s2)
# create_linked_list2("I love Shopee")
#  Create a linked list to store a input string
h, t = create_linked_list("I love Shopee")
show_ll(h, t)




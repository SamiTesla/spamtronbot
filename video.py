import random
import os
import discord

import discord as command


class TrieNode:

    def __init__(self, char):
        self.char = char

        self.is_end = False

        self.children = {}


class Trie(object):

    def __init__(self):

        self.root = TrieNode("")

    def insert(self, word):

        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:

                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True

    def dfs(self, node, pre):

        if node.is_end:
            self.output.append((pre + node.char))

        for child in node.children.values():
            self.dfs(child, pre + node.char)

    def search(self, x):

        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:

                return []

        self.output = []
        self.dfs(node, x[:-1])

        return self.output


client = discord.Client()
trie = Trie()
table = {
    "\"": None,
    "'": None,
    "-": None,
    "`": None,
    "~": None,
    ",": None,
    ".": None,
    ":": None,
    ";": None,
    "_": None
}


def trie1():
    file = open("words.txt.docx", 'r')

    for line in file:
        x = line.strip()
        trie.insert(x)


def punish_user(user_id):
    user_id = '<@' + str(user_id) + '>'
    responses = [

        "Come on now, {}. Did you really need to say that?",
        "{} - LANGUAGE!",
        "Hey now {}, watch your mouth.",
        "We don't use that kind of language here, {}."
    ]

    choice = random.choice(responses)
    choice = choice.format(user_id)

    return choice


@client.event
async def on_ready():
    trie1()
    print("Trie is built. ready to read messages.")


@client.event
async def on_message(message):
    text = message.content
    text = text.translate(str.maketrans(table))
    author_id = message.author.id

    if author_id != 756276859225768057:
        isclean = True
        message_word_list = text.split()
        for word in message_word_list:
            if trie.search(word):
                isclean = False
                break
        if not isclean:
            await message.channel.send(punish_user(author_id))


client.run('token')



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
    # list of possible sayings
    choice = random.choice(responses)
    choice = choice.format(user_id)

    return choice


@client.event
async def on_ready():
    trie1()
    print("Trie is built. ready to read messages.")


# notifys me that the bot is online on discord

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


# checks if the user says something that is on the list of banned words

client.run('token')
# runs on discord


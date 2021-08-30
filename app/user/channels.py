from channels import Group

def conectando(message):
    Group('users').add(message.reply_channel)

def desconectando(message):
    Group('users').discard(message.reply_channel)
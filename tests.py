import unittest
from asyncirc.ircbot import user_re

class IRCBotTest(unittest.TestCase):
    def test_nick_recognition(self):
        nicks = ["abc", "b-s[", "ChanServ", "C_C", "CC[m]", "C-K", "LXI123", "J_", "k4cg2", "n|m", "n[m]"]
        for nick in nicks:
            input = ":%(username)s!Name@host COMMAND <ARGS>" % {"username": nick} #:User!Name@host COMMAND <ARGS>nick!username@host" 
            userhost = user_re.search(input)
            newNick, user, host = userhost.groups()
            self.assertEqual(nick, newNick, 'incorrect username recognition: ' + nick + " was " + newNick)

if __name__ == '__main__':
    unittest.main()

from random import choice
class Word():
    def wortmachen(self):
        zahlen = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
        grossb = ("Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ü", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä", "Y", "X", "C", "V", "B", "N", "M")
        kleinb = ("q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "ü", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "y", "x", "c", "v", "b", "n", "m")
        sonderz = ("^", "!", "\"", "§", "$", "%", "&", "/", "(", ")", "=", "?", "ß", "\\", "+", "*", "<", ">", "|", "'", "#", ",", ";", ":", "-", "_", "{", "}", "[", "]", "~")
        wörter = ("ab ", "etwas ", "Holz ", "neun ", "stellen ", "Abend ", "fahren ", "hören ", "nicht ", "Straße ")
        sub = ("Mehmet ", "Felix ", "Pascal ", "Jan ", "Ling Ling ", "Florian ", "Kevin ")
        pre = ("fragt ", "haut ", "spielt mit ", "diskutiert", "lernt mit ", "fährt mit")
        obj = ("Mehmet ", "Felix ", "Pascal ", "Jan ", "Ling Ling ", "Florian ", "Kevin ")

        wort = ""
        zusammensetzung = (sub, pre, obj, ".")
        for teil in zusammensetzung:
            zeichen = choice(teil)
            wort += zeichen


        return(wort)
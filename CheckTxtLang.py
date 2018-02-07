# -*- coding: utf-8 -*-
# Share a function or covert any function you Done Before in Other Programming Lang
def CheckTextIsArabic(string):
    lang = 0
    byte = []
    for char in string :
        u = ord(char)
        byte.append(u)
    print byte
    uni_len = len(byte)
    i= 0
    while i < uni_len:
        if byte[i] == 216 :#0x06** is arabic code page
            lang = 1
            break
        elif byte[i] == 195 : #NONE ACSII lang
            #print byte[i]
            lang = 3
            break
        else:
            lang = 2 #English
        i += 1
    return lang

#print CheckTextLang("English") # should print 2
print CheckTextIsArabic("z")
#[122] lang 2
print CheckTextIsArabic("ب")
#[216, 168] lang 1
print CheckTextIsArabic("ÿ")
#[195, 191] lang 3

'''
# C# Method to Check text if Contains arabic AsciiCharacter or not
public static int CheckText(string s)
{
    bool ar = false;
    //int returns with 1 for arabic 2 for english and ascii 3 for non AsciiCharacter
    int n = 0;
    byte[] bytes = Encoding.Unicode.GetBytes(s);
    for (int i = 1; i < bytes.Length; i += 2)
        if (bytes[i] == 6) //0x06** is arabic code page
        {
            n = 1; // Arabic

        }
        else if (bytes[i] > 0)
        {
            n = 3; // NONE ACSII = Arabic

        }
        else
        {
            n = 2; // English
        }
    return n;
}
'''

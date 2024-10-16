# Annalise Gade
# UWYO COSC 1010
# Submission Date: 10/16/24
# Lab 06
# Lab Section: 15
# Sources, people worked with, help given to: N/A
# No further comments


random_string = """
jppamiqxegokaizvkyawwurhewtcxohryzptznyuedhhmawpic
pkzwuiorngdfcsgqnlyifzyaivehpiyszykqprbcsobygzhadd
yfddbulxmcnyvqhesmnybyuhxjqqmhdxwhcselasiayqhctnlw
hakethjahqnvjdowhlyzosemxkbenestxgvgncmffkcxldcmkl
itclmqdhrbdgzwtvdxwedcknbyaecvttjphtxubvhwvcvjqayy
almxuxjbcmznnzekptfzbldsjwpvringlmalwufvlppeiendur
dyophftqjkghhncwxoksqaqnpueudpygiytqgpcgjqsjbtbpzi
vaeczmyicnednjjoxkpnjmpfbgyjnbfjlweqqppodfxfzzwkuf
rldgryyhceuikimoavosuzuozthmatcgxcmkxnaxmsevkcumby
spiajlbycvrluxdkfavxidzalxuixqkxiybhfuqhcvmrhzbzse
idjwgwdwgfkyreozkyoxdvhixfejxjfgkkgobescboyfshiovu
fxdyvfsnmjzsphgmtldlaoehofcspzujghcdcxzggvunpbtglr
topplmkviuewwpoaplmbpgejmymxbyzzwbnujrlysszmxkjerb
zpiewqvgopvhmmcgwcyvxvwhdvfgsrybcozhdtwujhdbxzznkc
ergcqbetpgwrejuluqfxchlihunzbcdwboysjqenjxzbgqbycx
dybxpyztjyxpkqfvxullzkedpkjjobhymfinpvprxejktyrpai
ehjgwahpquzcmvclatdfcmattavoehnhnzveoxwnmnptxbvxto
gpcobgzdhsjevhcohkltftmrqkosknkxeylhqxkkctbnusijgr
uvecpbqmylqdaohkfaqbgeokyyipumjuaaayikdzyxfrpaieyo
uxiosjwioebsjtslblfurgcodtyaggzovzfnnyjngawiwbbtqi
kqqhnkwheolpqzasmsmbxqkeiqvogquobphewznfsnlkkizhca
cbiyvxpmjxywqvzqtshfvnfbusphggexfqzepsrduvtovdsknl
ztyuwugprkhbmktfvrenbmqgdjwnkeugtojrpqfmjhtrlcqcpq
pwsguedzgvktpwbqkhkueymjtxbvzmdfjopzkygujrjdtogssg
cxczryuqhhgjlpultkoffescpzyjrfqqabnhkfdnhkylpjamxk
uxidjkqdrkxqjqjtflebvwhcvqjciykzhrvppvxhvpedgznwty
kujglixooczrhxziasjxddfcghzlwrqcyiilpruhdfvitewxzg
dzcvmvnoskchscgoqfsojfvahlwkrslzeirlblseplcmpmbmum
ibrdamvqfstydtjopdkdcbnnmpifxckozyxzluhcqbqtpismog
ulufaajxvuizvdzioxfvypxovptkibcrjvfidomejknuggfrtp
kptwffersvqjknemkejsgspckwqisdcliuezhbeqpwgrjcqajl
huobykkbujmyuuinbwdklqfhvakyozzsxghfyownjjwqtkxgkf
ipdbjzxfogozstfsektujsvklrvecditiectuvtfibohmxxzna
cpqzeoburtquuizhypugnkvuwbdxnraareqkofhfjobrpcsuxq
nbafxlkuafbfsiuyrxdusqyasqyrwhdjrukgxdackumvairlgn
fjhenwbrdghbevgqbybpwncclolgqyuhallbqtzdywbvlzwtil
jctmsxjortnxvlbhuhkblppewjhqjzxrwgftlturxjuwfoaqpp
sgfnxwxolkbrpdmpniitoljzaxabgtnelrmryetxqypwrjdyjc
zipwbdpbazxpesmrcfuikeamtlsrgxrhzfytecenyydeemrhxj
gmdruhillntvpadzbroyygydpmonwuakruvxbdrqhtrjvoqsin
gjbarzvuqplmsmbwtqfghteoknbxmaokwlqqfoblmzsxczjzfj
mzmawtarjdtgongqqufhhdjwcinhlxcsgoltjycxrkloqozxoi
crlfmgflzzxgiiliqlksxyaydsohhahzxtsufzppftvgbpsdlx
ertfmbothijzrrdvfrnsohnwulcxvcvxngvmznhazxrgdsugij
fracotpirvqemsiuualpkpvtmtgchmowkmvoolrjfblrtwkmtr
xhawucytgwlahddkhxxfublukkdldpovqokntydhzzrxiisdwu
ujrkoewqoflyebogbwgdhriwkkoiofwtjlhxxtmzkklzbcmxhv
lrslowamkcwolbcgfkfciegdwqskuazxnycqkkggzsowcmafay
ibmkdwkqmdkjesqnjiqpijixbwjhenmsrrlpcseliiajlvcaac
zkdenxczyooloczcaahnkehbwimvieedpdlqfafbqvxvfmvabd
"""
random_string = random_string.replace("\n","") #remove all newline characters
print(len(random_string)) # Print out the size for reference 

# Above is a string with 2500 characters.
# Create a program that goes through and counts the occurrence of each character, excluding \n using a  dictionary
# Output each letter and its corresponding occurrence in alphabetical order
# Output which letter occurred the most 
# Output which letter occurred the least 
# Output what the percentage of the string each character is, again in alphabetical

#Tips and trick:
# You can iterate through strings like you would a list
# All characters are lowercase 
# Each letter will be PAIRED with its corresponding value 
# That is to say, this is a great use of dictionaries
    # You will  need to add the letter to the dictionary on first occurrence 
    # Then increment its corresponding count 

#Load all the elements into a dictionary
#Will need to first declare a dictionary 
letters = {}

for character in random_string:
    if character in letters:
        letters[character] += 1
    else:                       # if first occurence in the string, need to define key
        letters[character] = 1
# Output: each letter and its corresponding occurrence in alphabetical order
print(sorted(letters.items()))

print("*"*75)
# Output which letter occurred the most 

most_occurred = max(letters, key=letters.get)
least_occurred = min(letters, key=letters.get)

print(f"The letter that occurred the most is {most_occurred}")
print("*"*75)
# Output which letter occurred the least 
print(f"The letter that occurred the least is {least_occurred}")
print("*"*75)

# Output what the percentage of the string each character is, again in alphabetical
letters_percent = {}
for letr in letters:
    letters_percent[letr] = round((letters[letr]/len(random_string))*100, 3)     #rounded for simplicity
print(sorted(letters_percent.items()))
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common
import constants as ct
import rotor
from plugboard import PlugBoard
from enigma import Enigma, EnigmaException
from instances import Rotors, Reflectors


init_rotors = [
    [Rotors.ROTOR_I(), Rotors.ROTOR_II(), Rotors.ROTOR_III()],
    [Rotors.ROTOR_II(), Rotors.ROTOR_I(), Rotors.ROTOR_IV()],
    [Rotors.ROTOR_VII(), Rotors.ROTOR_II(), Rotors.ROTOR_IV()],
]

init_positions = [
    [0, 3, 25],
    [10, 8, 2],
    [22, 22, 4],
]

init_reflector = [
    Reflectors.REFLECTOR_B(),
    Reflectors.REFLECTOR_C(),
]

init_plugboard = [
    PlugBoard([(x, x + 10) for x in range(1, 10)]),
    PlugBoard([]),
    PlugBoard([(1, 2), (3, 4), (5, 6)])
]


@pytest.mark.parametrize('rotors', init_rotors)
@pytest.mark.parametrize('positions', init_positions)
@pytest.mark.parametrize('reflector', init_reflector)
@pytest.mark.parametrize('plugboard', init_plugboard)
def test_enigma_init(rotors, positions, reflector, plugboard):
    Enigma(rotors, positions, reflector, plugboard)


@pytest.mark.parametrize('rotors,positions,reflector,plugboard', [
    ([Rotors.ROTOR_I()], [0, 3, 4, 5], Reflectors.REFLECTOR_B(),
     init_plugboard[0]),
    (init_rotors[1]*2, init_positions[0] * 2, Reflectors.REFLECTOR_C(),
     init_plugboard[0]),
    (init_rotors[2], init_positions[2], Reflectors.REFLECTOR_C(), 1),
    ])
def test_enigma_init_ko(rotors, positions, reflector, plugboard):
    with pytest.raises(EnigmaException):
        Enigma(rotors, positions, reflector, plugboard)


# This is a rotor II with a ringstellung set to 'T' in the constructor
test_constructor_ringstellung = rotor.Rotor(notch={ord('E')-ord(ct.MIN_CHAR)},
                                            permutations=common.str_to_tuples('ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                                                 'AJDKSIRUXBLHWTMCQGZNPYFVOE'),
                                            ringstellung=19)


@pytest.mark.parametrize('positions, reflector, rotors,\
plugboard,user_input, expected_output', [
    ([0, 0, 0], Reflectors.REFLECTOR_B(), [test_constructor_ringstellung, Rotors.ROTOR_III(), Rotors.ROTOR_IV()],
     PlugBoard([]), "testing the ringstellung".replace(' ', ''),
     "ELOWX GRCYS UNRWL PJHDL SK".replace(' ', '')),
])
def test_enigma_cipher_constructor_ringstellung(positions, reflector, rotors, plugboard, user_input, expected_output):
    rotors = rotors
    m = Enigma(rotors, positions, reflector, plugboard)
    output = m.cipher(user_input)
    assert output == expected_output


@pytest.mark.parametrize('positions,reflector, rotors, ringstellung,\
plugboard,user_input, expected_output', [
    ([16, 0, 0], Reflectors.REFLECTOR_B(), [Rotors.ROTOR_I(), Rotors.ROTOR_III(), Rotors.ROTOR_II()], 'QQP',
     PlugBoard([]), "HOLA AMIGO COMO ESTAMO".replace(' ', ''),
     "NREID YYRVA MYCJO NROR".replace(' ', '')),
    ([16, 0, 0], Reflectors.REFLECTOR_B(), [Rotors.ROTOR_I(), Rotors.ROTOR_III(), Rotors.ROTOR_II()], 'QQP',
     PlugBoard([]), "HOLA AMIGO COMO ESTAMO".replace(' ', ''),
     "NREID YYRVA MYCJO NROR".replace(' ', '')),
    ([16, 0, 0], Reflectors.REFLECTOR_B(), [Rotors.ROTOR_V(), Rotors.ROTOR_III(), Rotors.ROTOR_II()], 'QQP',
     PlugBoard([]), "hi my dear friend".replace(' ', ''),
     "AZPEA GGYZW STWG".replace(' ', '')),
    ([0, 0, 0], Reflectors.REFLECTOR_B(), [Rotors.ROTOR_IV(), Rotors.ROTOR_II(), Rotors.ROTOR_III()], 'AAA',
     PlugBoard([]), "Hola amigo como estamo".replace(' ', ''),
     "RZFGC UOBCA DGZNN SNKC".replace(' ', '')),
    ([16, 0, 0, 0], Reflectors.REFLECTOR_B(), [Rotors.ROTOR_I(), Rotors.ROTOR_II(), Rotors.ROTOR_III(), Rotors.ROTOR_BETA()], 'AAAA',
     PlugBoard([]), "hello how are you".replace(' ', ''),
     "SFMSJ MLVKC SJAQ".replace(' ', '')),
    ([16, 9, 10, 11], Reflectors.REFLECTOR_B(), [Rotors.ROTOR_I(), Rotors.ROTOR_II(), Rotors.ROTOR_III(), Rotors.ROTOR_BETA()], 'LOLA',
     PlugBoard([]), "hello how are you".replace(' ', ''),
     "ZRZEV AJICC TGTE".replace(' ', '')),
    ([16, 9, 10, 11], Reflectors.REFLECTOR_B(), [Rotors.ROTOR_I(), Rotors.ROTOR_II(), Rotors.ROTOR_III(), Rotors.ROTOR_BETA()], 'LOLA',
     PlugBoard([(1, 2), (3, 4), (9, 21)]), "hello how are you".replace(' ', ''),
     "ZPZDJ AVIBB NGTD".replace(' ', '')),
    ([16, 9, 10, 11], Reflectors.REFLECTOR_B(), [Rotors.ROTOR_I(), Rotors.ROTOR_II(), Rotors.ROTOR_III(), Rotors.ROTOR_BETA()], 'LOLA',
     PlugBoard([(1, 2), (3, 4), (9, 21)]), "I am counting my calories, yet I really want dessert.    You can't compare apples and oranges, but what about bananas and plantains?    I love bacon, beer, birds, and baboons.    Her hair was windswept as she rode in the black convertible.    Imagine his surprise when he discovered that the safe was full of pudding.    She had some amazing news to share but nobody to share it with.    She insisted that cleaning out your closet was the key to good driving.    The Great Dane looked more like a horse than a dog.    He ended up burning his fingers poking someone else's fire.    I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.    They called out her name time and again, but were met with nothing but silence.    He used to get confused between soldiers and shoulders, but as a military man, he now soldiers responsibility.    He was so preoccupied with whether or not he could that he failed to stop to consider if he should.    Purple is the best city in the forest.    So long and thanks for the fish.    I hear that Nancy is very pretty.    The tortoise jumped into the lake with dreams of becoming a sea turtle.    It took me too long to realize that the ceiling hadn't been painted to look like the sky.    Let me help you with your baggage.    Last Friday I saw a spotted striped blue worm shake hands with a legless lizard.    It was difficult for Mary to admit that most of her workout consisted of exercising poor judgment.    Today we gathered moss for my uncle's wedding.    It's important to remember to be aware of rampaging grizzly bears.    She wondered what his eyes were saying beneath his mirrored sunglasses.    Everyone was curious about the large white blimp that appeared overnight.    Even though he thought the world was flat he didn’t see the irony of wanting to travel around the world.    His ultimate dream fantasy consisted of being content and sleeping eight hours in a row.    He found the end of the rainbow and was surprised at what he found there.    He decided to count all the sand on the beach as a hobby.    The Guinea fowl flies through the air with all the grace of a turtle.".replace(' ', ''),
     "SQSJJ FRXPG HWNES EEYDI NUYBG LXSUK QRWYB LVLBT QBKXC JPVVL UYTVS FSAGF OPLXE MUXSK NFIHS TJRDZ VISEL MBREX EFMPO AXPVP ZTDTA IXDPD KVZVC AONZY WFSAP TJZSM LMCGX PFWJP VUAZU FDYNI QSNTS DTRSF GKAJN LBHHS QPTOQ GEUQX WTWFS MCRKS VVBBJ EKAUP UJHYS XOZJM FWJLP HRKBG WYIVZ XRHRA GPAUN TZVKA TPGLB ZVNEL SCHOJ PTRTH HUUGE EPZGJ YSDJM OKAPU GCJCQ VDPET KJPSZ QDZNJ KPBCB NCZHS VVWZK SIVFR GFZWN BYFXQ UVCWX PZCJM LFKZZ QGPYF PIALV KUGXD BHEYI XLCTA HZPHS YCCGT ZYMEK JDMJW ITOAS ORWBK XLZFR IOPTZ AOIYF QRJYJ RQWYR CDOVU NZYJQ RTMYR WRAYJ OXKLL AQSTV XPWDP XRSOD XQOEA ZMDME KALBI VDJWI CSRSR EBRDS HBMGN XKOLR QVXLV CKPUN QKCFX RWAYA ZUEQY CQDKA PFWRS UJFLH AXDTV IKYWB TFCEN NXTIY WDAFD FBFFY GAKZD AAFMZ JKMVG STHIV AVIWZ SDQWF RPJIM WYRIW YBCZS BZIDJ BFWMM EKFUU DPMZZ OSRCP CKYEY QKJNJ NSYSD LNHUP RXLOW IOAXQ UGQDJ CWVFV YLYQU RRCWF SYILW CWZYC KEAGW RUWTN OUBFY XQVJH KMAUW QILCJ MGQPT ZPQAA FIRTB NFXME QJSTX RTTZJ LGTKI YEBNW GJXOD WYERH ZMDGE BWOHU YYDCA RTKOM SRIYK NAPXS ZBCGN RPPGN LMWHQ BDQTH LGCHM ZSZQS JGKKQ JMTGJ RFKJU LOGLH SOWMI DXQBV IGCGG JQMMR GAEZC RWPLC FCAPD EEJFS HMQBL QUYVE FHKDY LSKWC KWARD VGCNR XKPSL CYNVS GUVYS HFWCM WRXKQ AYHQW XDIKC VTWIH LTZSC SJZHD NPVCD XTUEL FWKQR OUIBB TWLZU RAYKH BYICP WYIYV UHHVS NNDSX IDMTR GAWDZ ZHRMZ GQEII HGWYO UTPUY FZEVF FQUMG QKHXN FPYNX TWIBQ VFAUK XZBRQ NKVZK GEZFW UMIOJ ILSND LARKL QASZG YXMRZ IGMVC FZHNZ YMRLU LCCTJ DUTET CWUQY KZJXH SAWTY MRPYW GZFUE EQUGX FEUWU KFQFA FRNIU SDAFI YYXWS OKGVZ VBPWJ PJXBF VHFNU FMZLB VUUXA IAHCC BJXAN YNIQV VVRFE LGGYY ZKFHH ZURUW OWKED XRNRI NBSBM JKHOQ ETECZ DYCJC LRMIX EFCQB BJPIT WUUDI LWYAF QITSW WCRMH YLFGF PUXWC ZXKHQ HKTUA CHFIR CPALG AGXQQ BVPID MRXGD ICQIZ BCLPK ZNTHX GDLBU ZWUAH HRTYC LLPVS NPOZC ZOQHV BLPQV RFGNX WRANK TVJUH VRQPS VNKYP UMIUS IQZBL EKYHF OQMXW IFRHA CDIDF UFSMU COVWX ZXPLT JNFAG SBXLX UEBGX MUWJU BSRGY YHHJK WLLMX BJRXB MMQTB FXYDE NKKAJ HGIWJ BCXNA YOTQO UJHDB BAEPY FHIQC EPMZD XSSNZ YVESZ UQNYO RBFOI YMRDD OTKPE PQCMX YCTUJ AKWFR EMTLR HPCXJ OKUEX BRAHZ WMOGE UC".replace(' ', '')),
    ([0, 0, 0], Reflectors.REFLECTOR_B(), [Rotors.ROTOR_VI(), Rotors.ROTOR_III(), Rotors.ROTOR_II()], 'QQP',
     PlugBoard([]), "hi my dear friend".replace(' ', ''),
     "TSARA HKDYC LYVL".replace(' ', '')),
    ([25, 0, 0], Reflectors.REFLECTOR_B(), [Rotors.ROTOR_VI(), Rotors.ROTOR_III(), Rotors.ROTOR_II()], 'QQP',
     PlugBoard([]), "hi my dear friend".replace(' ', ''),
     "QSNUJ JFTWK UACW".replace(' ', '')),
    ([25, 0, 0], Reflectors.REFLECTOR_B(), [Rotors.ROTOR_VI(), Rotors.ROTOR_III(), Rotors.ROTOR_II()], 'AAA',
     PlugBoard([]), "himy".replace(' ', ''),
     "QHNG".replace(' ', '')),
    ([25, 0, 0], Reflectors.REFLECTOR_B_thin(), [Rotors.ROTOR_VI(), Rotors.ROTOR_III(), Rotors.ROTOR_II()], 'AAA',
     PlugBoard([]), "hello how are you my dear friend im fine glad you asked".replace(' ', ''),
     "PYWVB XPEDA OMGXW BHWWZ IFVYK OQRQE MDPMI YNATW QFSB".replace(' ', '')),
    ([25, 0, 0], Reflectors.REFLECTOR_B_thin(), [Rotors.ROTOR_VII(), Rotors.ROTOR_III(), Rotors.ROTOR_II()], 'AAA',
     PlugBoard([]), "hello how are you my dear friend im fine glad you asked".replace(' ', ''),
     "NGJOY NMGRF NRCXG IIRUV YXQFI WAZIK MSFUN YJIRT QECO".replace(' ', '')),
    ([7, 2, 19], Reflectors.REFLECTOR_B_thin(), [Rotors.ROTOR_VI(), Rotors.ROTOR_VII(), Rotors.ROTOR_VIII()], 'XOI',
     PlugBoard([]), "hello how are you my dear friend im fine glad you asked".replace(' ', ''),
     "XOWIE KNXZZ ZMCQN GZQPD KNGQQ NVATJ FMQSW IMZXH NCPA".replace(' ', '')),
    ([7, 2, 19, 23], Reflectors.REFLECTOR_B_thin(), [Rotors.ROTOR_VI(), Rotors.ROTOR_VII(), Rotors.ROTOR_VIII(), Rotors.ROTOR_GAMMA()], 'XOII',
     PlugBoard([]), "hello how are you my dear friend im fine glad you asked".replace(' ', ''),
     "PWJBC SEZEL JFEDS KGVXG WDJJF FLOYN IAXKH NPWOR OGYV".replace(' ', '')),
    # Class test
    ([25, 18, 3, 2], Reflectors.REFLECTOR_C_thin(), [Rotors.ROTOR_VIII(), Rotors.ROTOR_VI(), Rotors.ROTOR_V(), Rotors.ROTOR_BETA()], 'LEPE',
     PlugBoard([(0, 4), (1, 5), (2, 12), (3, 16), (7, 20), (9, 13), (11, 23), (15, 17), (18, 25), (21, 22)]),
     "LANOTCTOUARBBFPMHPHGCZXTDYGAHGUFXGEWKBLKGJWLQXXTGPJJAVTOCKZFSLPPQIHZFXOEBWIIEKFZLCLOAQJULJOYHSSMBBGWHZANVOIIPYRBRTDJQDJJOQKCXWDNBBTYVXLYTAPGVEATXSONPNYNQFUDBBHHVWEPYEYDOHNLXKZDNWRHDUWUJUMWWVIIWZXIVIUQDRHYMNCYEFUAPNHOTKHKGDNPSAKNUAGHJZSMJBMHVTREQEDGXHLZWIFUSKDQVELNMIMITHBHDBWVHDFYHJOQIHORTDJDBWXEMEAYXGYQXOHFDMYUXXNOJAZRSGHPLWMLRECWWUTLRTTVLBHYOORGLGOWUXNXHMHYFAACQEKTHSJW".replace(' ', ''),
     "KRKRA LLEXX FOLGE NDESI STSOF ORTBE KANNT ZUGEB ENXXI CHHAB EFOLG ELNBE BEFEH LERHA LTENX XJANS TERLE DESBI SHERI GXNRE ICHSM ARSCH ALLSJ GOERI NGJSE TZTDE RFUEH RERSI EYHVR RGRZS SADMI RALYA LSSEI NENNA CHFOL GEREI NXSCH RIFTL SCHEV OLLMA CHTUN TERWE GSXAB SOFOR TSOLL ENSIE SAEMT LICHE MASSN AHMEN VERFU EGENY DIESI CHAUS DERGE GENWA ERTIG ENLAG EERGE BENXG EZXRE ICHSL EITEI KKTUL PEKKJ BORMA NNJXX OBXDX MMMDU RNHFK STXKO MXADM XUUUB OOIEX KP".replace(' ', '')),
])
def test_enigma_cipher_char(positions, reflector, rotors, ringstellung, plugboard, user_input, expected_output):
    rotors = rotors
    for i in range(len(rotors)):
        rotors[i].ringstellung = common.char_to_int(ringstellung[i])
    m = Enigma(rotors, positions, reflector, plugboard)
    output = m.cipher(user_input)
    assert output == expected_output

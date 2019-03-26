def count_char():

    speaker_charcount_dict = {
        "Arjun" : [0] * 37,
        "Bhagawan" : [0] * 37,
        "Sanjay" : [0] * 37,
        "Dhritarashtra" : [0] * 37,
        "None": [0] * 37,
    }

    speaker_char_group_count_dict = {
        "Arjun" : { 'ka' : 0, 'ca' : 0, 'Ta' : 0, 'ta' : 0, 'pa' : 0, 'ya' : 0, 'ha' : 0, 'total' : 0},
        "Bhagawan" : { 'ka' : 0, 'ca' : 0, 'Ta' : 0, 'ta' : 0, 'pa' : 0, 'ya' : 0, 'ha' : 0, 'total' : 0},
        "Sanjay" : { 'ka' : 0, 'ca' : 0, 'Ta' : 0, 'ta' : 0, 'pa' : 0, 'ya' : 0, 'ha' : 0, 'total' : 0},
        "Dhritarashtra" : { 'ka' : 0, 'ca' : 0, 'Ta' : 0, 'ta' : 0, 'pa' : 0, 'ya' : 0, 'ha' : 0, 'total' : 0},
        "None": { 'ka' : 0, 'ca' : 0, 'Ta' : 0, 'ta' : 0, 'pa' : 0, 'ya' : 0, 'ha' : 0, 'total' : 0}
    }

    # default value for speaker
    speaker = 'None'

    with open('Geeta_input_001.txt', encoding='utf-8') as f:
        for line in f:

            if line.find(u'अर्जुन उवाच') > -1:
                speaker = 'Arjun'
                continue
            if line.find(u'श्रीभगवानुवाच') > -1:
                speaker = 'Bhagawan'
                continue
            if line.find(u'सञ्जय उवाच') > -1:
                speaker = 'Sanjay'
                continue
            if line.find(u'धृतराष्ट्र उवाच') > -1:
                speaker = 'Dhritarashtra'
                continue
            if (line.find(u'ॐ तत्सदिति श्रीमद्भगवद्गीतासूपनिषत्सु') > -1 ) or (line.find(u'ब्रह्मविद्यायां') > -1) or (line.find(u'ध्यायः') > -1):
                speaker = 'None'
                continue

            for character in line:
                x = character.encode('utf-8')
                if x[0] == 224:
                    temp = ((x[1] & 0x03) << 6) | (x[2] & 0x3f)
                    temp = temp - 21
                    if ((temp >= 0) and (temp < 38)):
                        speaker_charcount_dict[speaker][temp] += 1

    for speaker, character_count in speaker_charcount_dict.items():
        #print(speaker)
        for i, c in enumerate(character_count):
            x = bytes([0xe0, 0xa4, 0x95 + i])
            #print("%s, %d" % (x.decode('utf-8'), c))
            speaker_char_group_count_dict[speaker]['total'] += c
            if(i < 5):
                speaker_char_group_count_dict[speaker]['ka'] += c
            if(i > 4) and (i < 10):
                speaker_char_group_count_dict[speaker]['ca'] += c
            if (i > 9) and (i < 15):
                speaker_char_group_count_dict[speaker]['Ta'] += c
            # ta group has 6 characaters : ta, tha, da, dha, na and na.
            if (i > 14) and (i < 21):
                speaker_char_group_count_dict[speaker]['ta'] += c
            if (i > 20) and (i < 26):
                speaker_char_group_count_dict[speaker]['pa'] += c
            if (i > 25) and (i < 36):
            # ya group has 10 characters : ya, ra, ra., la, La, La., va, sh, Sh and sa
                speaker_char_group_count_dict[speaker]['ya'] += c
            # single character ha
            if(i == 36):
                speaker_char_group_count_dict[speaker]['ha'] += c

    for speaker, character_group_count in speaker_char_group_count_dict.items():
        print(speaker)
        for group, count in character_group_count.items():
            print("%s, %.2f" % (group, count * 100 / character_group_count['total']))

if __name__ == "__main__":
    count_char()

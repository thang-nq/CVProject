import Constants

level_map = {}
level_map["level_map1"] = [
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

level_map["level_map2"] = [
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

level_map["level_map3"] = [
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    'XXXX                      XXXX',
    'XXXX                      XXXX',
    'XXXX                      XXXX',
    'XXXX                      XXXX',
    'XXXX                      XXXX',
    'XXXX                      XXXX',
    'XXXX          XX          XXXX',
    'XXXX          XX          XXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

level_map["level_map4"] = [
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '       X                  XXXX',
    '       X                  XXXX',
    '     XXX                  XXXX',
    '                          XXXX',
    '                          XXXX',
    '                          XXXX',
    '                          XXXX',
    '                          XXXX',
    '                          XXXX',
    '                          XXXX',
]

level_map["level_map5"] = [
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '             XXXXXXXX         ',
    '                              ',
    '                              ',
    '                              ',
    'XXXXXXXXXXX                   ',
    'XXXXXXXXXXX                   ',
    'XXXXXXXXXXX                   ',
    'XXXXXXXXXXX          XXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

level_map["level_map6"] = [
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

level_map["level_map7"] = [
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    'XXXX                          ',
    'XXXX                          ',
    'XXXX                          ',
    'XXXX                          ',
    'XXXX                          ',
    'XXXX                          ',
    'XXXX                   XXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXX  XXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

level_map["level_map8"] = [
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    '                              ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

level_map["level_map9"] = [
    '                              ',
    '                              ',
    '                              ',
    '                        XXXXXX',
    '                        XXXXXX',
    '                        XXXXXX',
    '                        XXXXXX',
    '                        XXXXXX',
    '                        XXXXXX',
    '                        XXXXXX',
    '                        XXXXXX',
    '                        XXXXXX',
    '                        XXXXXX',
    '                        XXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]
level_map["level_map10"] = [
    '             XXXX             ',
    '             XXXX             ',
    '             XXXX             ',
    '             XXXX             ',
    '             XXXX             ',
    '             XXXX             ',
    '             XXXX             ',
    '                              ',
    '                              ',
    '         X          X         ',
    '         X          X         ',
    '         X          X         ',
    '         X          X         ',
    '         X          X         ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]
tile_size = 50
screen_w = Constants.WIDTH
screen_h = Constants.HEIGHT


def getMap(number):
    level_name = "level_map" + str(number)
    return level_map[level_name]

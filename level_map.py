import Constants
level_map={}
level_map["level_map1"] = [
'                ',
'                ',
'                ',
'                ',
'                ',
'                ',
'                ',
'                ',
'XXXXXXXXXXXXXXXXX'
]

level_map["level_map2"] =  [
'                ',
'                ',
'                ',
'                ',
'                ',
'                ',
'                ',
'                ',
'XXXXXXXXXXXXXXXX'
]

level_map["level_map3"] =[
'                ',
'                ',
'                ',
'XX            XX',
'XXX          XXX',
'XXXX        XXXX',
'XXXXX  XX  XXXXX',
'XXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXX'
]

level_map["level_map4"] = [
'                ',
'                ',
'                ',
'             XXX',
'   X        XXXX',
'  XX       XXXXX',
'          XXXXXX',
'         XXXXXXX',
'        XXXXXXXX'
]

level_map["level_map5"] =[
'                ',
'                ',
'       XXXXX    ',
'                ',
'                ',
'                ',
'XXXXXX          ',
'XXXXXX      XXXX',
'XXXXXXXXXXXXXXXX'
]

level_map["level_map6"] =[
'                ',
'                ',
'                ',
'       X        ',
'                ',
'                ',
'                ',
'                ',
'XXXXXXXXXXXXXXXX'
]

level_map["level_map7"] = [
'                ',
'                ',
'                ',
'XX              ',
'XXX             ',
'XXXX            ',
'XXXXX        XXX',
'XXXXXXXXXXXX XXX',
'XXXXXXXXXXXXXXXX'
]

level_map["level_map8"] =[
'                ',
'                ',
'X              X',
'XX            XX',
'XXX          XXX',
'XXXX        XXXX',
'XXXXX      XXXXX',
'XXXXXX    XXXXXX',
'XXXXXXXXXXXXXXXX'
]

level_map["level_map9"] = [
'                ',
'                ',
'             XXX',
'X           XXXX',
'XX         XXXXX',
'XXX       XXXXXX',
'XXXX     XXXXXXX',
'XXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXX'
]
tile_size = 50
screen_w = Constants.WIDTH
screen_h = Constants.HEIGHT
def getMap(number):
    level_name = "level_map" + str(number)
    return level_map[level_name]
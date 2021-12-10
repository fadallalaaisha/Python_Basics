# def main(tiles):
#     for i in tiles:
#         if i == tiles:
#             print("is complete")


#         elif i != tiles:
#             print("is not comlete")

#         else:
#             print("is ")

# tiles=range(0,9)
# for line in tiles:
#     if line == 3:
#         print ("is complete")

#     elif line != 2:
#         print("is not comples")
# sassertion- check if somethis is true or
def game(tiles):
    for i in tiles:
        if tiles[i]>=2:
            return True
        elif tiles[i]>=3:
            return True
        else:
            return False
print( game([1,2,9,3,7,2,4,5]) )
print( game([0,1,1,2,2,2,4,4]) )
print( game([0,1,2,3,4,5,6,7,8]) )

      
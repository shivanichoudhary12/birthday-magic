def birthday():
    print("guessing your birthday")
    slide_1 = [[1,3,5,7],[9,11,13,15],[17,19,21,23],[35,27,29,31]]
    slide_2 = [[2,3,6,7],[10,11,14,15],[18,19,22,23],[26,27,30,31]]
    slide_3 = [[4,5,6,7],[12,13,14,15],[20,21,22,23],[26,27,28,29]]
    slide_4 = [[8,9,10,11],[12,13,14,15],[24,25,26,27],[28,29,30,31]]
    slide_5 = [[16,17,18,19],[20,21,22,23],[24,25,26,27],[28,29,30,31]]
    slides = [slide_1,slide_2,slide_3,slide_4,slide_5]
    birth_date = 0
    for i,slide in enumerate(slides):
        print(slide)
        ans = input("/'y/' if number in slides ")   
        if ans == 'y':
            birth_date += 2**i
    return birth_date

parul = birthday()            
print(parul)

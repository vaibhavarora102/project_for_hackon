
ifww 'Covid'== 'Which_highest' or'Which_second_highest' or 'Which_third_highest':
    md=0
    print('had any travel history to foreign contry in last 21 days?')
#     make gui with option yes and no
    if query=="yes":
        md+=1

    print('had you came in contact with the covid infected person?')
        #     make gui with option yes and no
    if query == "yes":
        md += 1

    print('Have any past chronic disease history ?')
#     make gui with option yes and no
    if query=="yes":
        md+=1

    print('Difficulty in breathing?')
#     make gui with option yes and no
    if query=="yes":
        md+=1

#     next logic
#  next logic
    if md<2:
        print("you are at lower risk,"
              "kindly follow the guidlines offered by the arogya bharti "
              "for precautions"
              "and if you feel much difficulty concern to doctor")

    if md>=2:
        print(" we recomend that you should concern with the specialist")


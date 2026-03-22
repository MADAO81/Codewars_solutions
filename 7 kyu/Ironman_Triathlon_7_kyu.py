# https://www.codewars.com/kata/57d001b405c186ccb6000304/train/python


def i_tri(s):
    if s == 0:
        return 'Starting Line... Good Luck!'
    elif s <=2.4:
        return {'Swim': f'{(140.6 - s):.2f} to go!'}
    elif s <= 114.4:
        return {'Bike': f'{(140.6 - s):.2f} to go!'}
    elif s <= 130.6:
        return {'Run': f'{(140.6 - s):.2f} to go!'}
    elif s < 140.6:
        return {'Run': 'Nearly there!'}
    else:
        return 'You\'re done! Stop running!'

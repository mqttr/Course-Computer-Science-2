from lab import Television  # import statement needed to gain access to Television class
counter = 0


def fakeprint(stuff):
    global counter
    counter +=1
    print(counter, stuff)


def main():
    # Television 1
    tv_1 = Television()
    tv_1.power()
    fakeprint(tv_1)             # 1 TV status: Power = True, Channel = 0, Volume = 0

    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.volume_up()
    fakeprint(tv_1)             # 2 TV status: Power = True, Channel = 2, Volume = 1

    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.volume_down()
    tv_1.volume_down()
    fakeprint(tv_1)             # 3 TV status: Power = True, Channel = 1, Volume = 0

    tv_1.power()
    tv_1.volume_up()
    tv_1.channel_down()
    fakeprint(tv_1)             # 4 TV status: Power = False, Channel = 1, Volume = 0

    tv_1.power()
    tv_1.volume_up()
    tv_1.volume_up()
    tv_1.volume_up()
    tv_1.channel_down()
    tv_1.channel_down()
    fakeprint(tv_1)             # 5 TV status: Power = True, Channel = 3, Volume = 2

    # Television 2
    tv_2 = Television()
    tv_2.power()
    tv_2.channel_up()
    tv_2.volume_up()
    fakeprint(tv_2)             # 6 TV status: Power = True, Channel = 1, Volume = 1

    # Muting effect
    tv_1.mute()
    fakeprint(tv_1)             # 7 TV status: Power = True, Channel = 3, Volume = 0
    tv_1.volume_down()
    fakeprint(tv_1)             # 8 TV status: Power = True, Channel = 3, Volume = 1
    tv_1.mute()
    fakeprint(tv_1)             # 9 TV status: Power = True, Channel = 3, Volume = 0
    tv_1.volume_up()
    fakeprint(tv_1)             # 10 TV status: Power = True, Channel = 3, Volume = 2
    tv_1.power()
    tv_1.mute()
    fakeprint(tv_1)             # 11 TV status: Power = False, Channel = 3, Volume = 2


if __name__ == '__main__':
    main()

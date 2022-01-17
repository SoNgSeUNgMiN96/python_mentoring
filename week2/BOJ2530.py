hour , minutes, second = input().split(' ')
elapse = input()
#받아진 값들은 모두 str형식임

second = int(second) + int(elapse)
minutes = int(minutes) + int(second/60)
hour = int(hour) + int(minutes/60)

print("{0} {1} {2}".format(hour%24,minutes%60,second%60))


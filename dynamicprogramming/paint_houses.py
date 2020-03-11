def paintHouses(cost):
    if not cost:
        return 0
    elif(len(cost) == 1):
        return min(cost[0])
    for house in range(1, len(cost)):
            cost[house][0] += min(cost[house-1][1], cost[house-1][2])#red
            cost[house][1] += min(cost[house-1][0], cost[house-1][2])#blue
            cost[house][2] += min(cost[house-1][0], cost[house-1][1])#green
    return min((cost[-1]))

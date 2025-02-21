import random


def GenerateRandomFlips(num: int) -> list[str]:
    HeadTailsList: list[str] = []

    if (num == 0):
        return HeadTailsList
    
    # return ["H" if random.randint(0, 1) == 1 else "T" for _ in range(num)]

    for _ in range(num):
        if (random.randint(0, 1) == 0):
            HeadTailsList.append("T")
        else:
            HeadTailsList.append("H")

    return HeadTailsList


def CalculateStreakOfHeadAndTailsInACoinFlip(FlipCount: int, ComulativeAmount: int) -> tuple[int, int]:
    HeadTailsList = GenerateRandomFlips(FlipCount)

    TotalPreviousHead = 0
    TotalPreviousTail = 0

    TotalComulativeHeads: int = 0
    TotalComulativeTails: int = 0

    for index, item in enumerate(HeadTailsList):
        if (item == "H"):
            if (TotalPreviousHead == ComulativeAmount):
                TotalComulativeHeads += 1
                TotalPreviousHead = 0
            else:
                TotalPreviousHead += 1
                TotalPreviousTail = 0
        else:
            if (TotalPreviousTail == ComulativeAmount):
                TotalComulativeTails += 1
                TotalPreviousTail = 0
            else:
                TotalPreviousTail += 1
                TotalPreviousHead = 0

    print(TotalComulativeHeads, TotalComulativeTails)
    return (TotalComulativeHeads, TotalComulativeTails)


CalculateStreakOfHeadAndTailsInACoinFlip(10000, 6)

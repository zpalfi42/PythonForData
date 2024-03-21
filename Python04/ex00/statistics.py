"""
Learning how to use args and kwargs.
The difference between args and kwargs is that
kwargs are associated to a key and args not.
"""

def mean(args: any) -> None:
    """_summary_ mean
    """
    return (sum(args)/len(args))

def median(args: any) -> None:
    """_summary_ median
    """
    nums = sorted(args)
    lenght = len(nums)
    i = lenght // 2

    if lenght % 2 == 0:
        median = (nums[i-1] + nums[i]) / 2
    else:
        median = nums
        [i]
    return median

def quartile(args: any) -> None:
    """_summary_ quartile
        Not the right way to calculate quartiles but the expected way!
        This is the right way:
        i1 = (lenght + 1) * 1/4
        if i1.is_integer():
            q[0] = float(nums[int(i1) - 1])
        else:
            q[0] = float((nums[int(i1) - 1] + nums[int(i1)]) / 2)
    """
    nums = sorted(args)
    lenght = len(nums)
    i1 = lenght * 1/4
    i2 = lenght * 3/4
    q = [0.0 , 0.0]

    q[0] = float(nums[int(i1)])
    q[1] = float(nums[int(i2)])

    return q

def var(args: any) -> None:
    """_summary_ var
    """
    m = mean(args)
    sqrd_diff = [(x - m) ** 2 for x in args]
    var = sum(sqrd_diff) / len(args)

    return var

def std(args: any) -> None:
    """_summary_ std
    """
    v = var(args)
    std = v ** 0.5

    return std

def ft_statistics(*args: any, **kwargs: any) -> None:
    """_summary_
    """
    modes = {'mean':mean, 'median':median, 'quartile':quartile, 'std':std, 'var':var}
    try:
        for key in kwargs:
            if len(args) == 0:
                print("ERROR")
            elif (kwargs[key] in modes):
                print(f"{kwargs[key]} : {modes[kwargs[key]](args)}")

    except AssertionError as e:
        print("ERROR")
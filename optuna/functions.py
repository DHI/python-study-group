import time

def black_hole(x: float,y: float) -> float:
    """Simple function with single global minimum

    Parameters
    ----------
    x: float
        One parameter
    y: float
        Another parameter
    
    Returns
    -------
    float
        Some value
    """

    #time.sleep(1)
    return (x-2)**2 + 10*y**2
    
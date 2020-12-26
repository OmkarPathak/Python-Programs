import numpy as np

def estimate_coef(x, y): 
    n = np.size(x) 

    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 

    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 

    # calculating regression coefficients 
    b1 = SS_xy / SS_xx 
    b0 = m_y - b1*m_x 

    return(b0, b1)

def main(): 
    # observations 
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 

    # estimating coefficients 
    b = estimate_coef(x, y) 
    print("Estimated coefficients:\nb0 = {}  \\nb1 = {}".format(b[0], b[1]))

if __name__ == "__main__": 
    main()

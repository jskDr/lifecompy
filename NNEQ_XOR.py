import matplotlib.pyplot as plt 

# input is 1, 0
def NNEQ( x1, x2, w1, w2):
    y = x1 * w1 + x2 * w2
    return y

def NNEQ_bias( x1, x2, w1, w2, w_bias):
    y = x1 * w1 + x2 * w2 + w_bias
    return y

def Desired_linaer_bias( x1, x2):
    return x1 - 0.5 * x2 + 1.0

def Desired_xor( x1, x2):
    return x1 ^ x2

def Desired( x1, x2):
    return Desired_xor( x1, x2)

def Loop( w1, w2, mu = 0.01, iter_all = 100):
    for iter in range( iter_all):
        print '---------------'
        print 'Iteration = ', iter
        for x1 in [0, 1]:
            for x2 in [0, 1]:
                # This is computation part.
                out = NNEQ( x1, x2, w1, w2)
                des = Desired( x1, x2)
                err = des - out
                    
                # This is calculation part
                print 'x1, x2 =', x1, x2
                print 'w1, w2 =', w1, w2 
                print 'Output = ', NNEQ( x1, x2, 0, 0)
                print 'Desired = ', Desired( x1, x2)
                print 'Error = ', err
                   
                # This is update part.
                w1 = w1 + mu * err * x1
                w2 = w2 + mu * err * x2    
               
def LoopTrack( w1, w2, mu = 0.01, iter_all = 10):
    # Tracking is started.
    err_array = []
    
    for it in range( iter_all):
        print '---------------'
        print 'Iteration = ', it
        for x1 in [0, 1]:
            for x2 in [0, 1]:
                # This is computation part.
                out = NNEQ( x1, x2, w1, w2)
                des = Desired( x1, x2)
                err = des - out
                    
                # This is calculation part
                print 'x1, x2 =', x1, x2
                print 'w1, w2 =', w1, w2 
                print 'Output = ', NNEQ( x1, x2, 0, 0)
                print 'Desired = ', Desired( x1, x2)
                print 'Error = ', err
                   
                # This is update part.
                w1 = w1 + mu * err * x1
                w2 = w2 + mu * err * x2
                
                err_array.append( err)
            
    return err_array

def LoopTrack_bias( w1, w2, w_bias, mu = 0.01, iter_all = 10):
    # Tracking is started.
    err_array = []
    
    for it in range( iter_all):
        # print '---------------'
        # print 'Iteration = ', it
        for x1 in [0, 1]:
            for x2 in [0, 1]:
                # This is computation part.
                out = NNEQ_bias( x1, x2, w1, w2, w_bias)
                des = Desired( x1, x2)
                err = des - out
                    
                # This is calculation part
                """ print 'x1, x2 =', x1, x2
                print 'w1, w2, w_bias =', w1, w2, w_bias 
                print 'Output = ', out
                print 'Desired = ', des
                print 'Error = ', err """
                   
                # This is update part.
                w1 = w1 + mu * err * x1
                w2 = w2 + mu * err * x2
                w_bias = w_bias + mu * err * 1
                
                err_array.append( err)
            
    return err_array     
               
            
#This is main function
def main_1st(): # 2017-8-2 5:47pm
    w = [0, 0]
    Loop( w[0], w[1])
    
def main_2nd():
    w = [0.5, -0.5]
    err_array = LoopTrack( w[0], w[1], mu = 0.02)
    print err_array
    
    plt.plot( err_array)
    plt.show()
    
def main_3rd():
    w = [0.5, -0.5, 0.5] # the last element is bias value.
    err_array = LoopTrack_bias( w[0], w[1], w[2], mu = 0.02, iter_all = 100)
    # print err_array
    
    plt.plot( err_array, '.-')
    plt.show()
    
main_3rd()
    




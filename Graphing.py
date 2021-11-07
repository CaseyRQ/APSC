import matplotlib.pyplot as plt

def draw_graph(x,y):
    plt.plot(x, y, marker= 'o')
    plt.xlabel('Months')
    plt.ylabel('Power in watts')
    plt.title('Satellite power supply in 1 year')
    plt.show()

def generate_P_t():
    t= (-12)
    P= []

    i= float(50*2.71828)
    r= 250
    power= float(i**(t/r))
    P.append(power)

    draw_graph(t, P)
if __name__=='__main__':
    generate_P_t()


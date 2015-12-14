#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation

class SubplotAnimation(animation.TimedAnimation):
    def __init__(self):
        self.Dt_max = 3 # secs
        self.t = np.asarray([])
        self.x = np.asarray([])
        self.y = np.asarray([])
        
        fig = plt.figure()
        self.ax1 = fig.add_subplot(1, 2, 1)
        self.ax2 = fig.add_subplot(2, 2, 2)
        self.ax3 = fig.add_subplot(2, 2, 4)
        

        self.ax1.set_xlabel('x')
        self.ax1.set_ylabel('y')
        self.line1_History = Line2D([], [], color='black')
        self.line1_Trace = Line2D([], [], color='red', linewidth=2)
        self.line1_NowMarker = Line2D(
            [], [], color='red', marker='o', markeredgecolor='r')
        self.ax1.add_line(self.line1_History)
        self.ax1.add_line(self.line1_Trace)
        self.ax1.add_line(self.line1_NowMarker)
        self.ax1.set_xlim(-1, 1)
        self.ax1.set_ylim(-2, 2)
        self.ax1.set_aspect('equal', 'datalim')
        
        self.ax2.grid(True)
        self.ax2.set_xlabel('y')
        self.ax2.set_ylabel('z')
        self.line2_History = Line2D([], [], color='black')
        self.line2_Trace = Line2D([], [], color='red', linewidth=2)
        self.line2_NowMarker = Line2D(
            [], [], color='red', marker='o', markeredgecolor='r')
        self.ax2.add_line(self.line2_History)
        self.ax2.add_line(self.line2_Trace)
        self.ax2.add_line(self.line2_NowMarker)
        self.ax2.set_ylim(-1, 1)
        self.ax2.set_xlim(0, self.Dt_max+1)
        
        self.ax3.grid(True)
        self.ax3.set_xlabel('x')
        self.ax3.set_ylabel('z')
        self.line3_History = Line2D([], [], color='black')
        self.line3_Trace = Line2D([], [], color='red', linewidth=2)
        self.line3_NowMarker = Line2D( [], [], color='red', marker='o', markeredgecolor='r')
        self.ax3.add_line(self.line3_History)
        self.ax3.add_line(self.line3_Trace)
        self.ax3.add_line(self.line3_NowMarker)
        self.ax3.set_ylim(-1, 1)
        self.ax3.set_xlim(0, self.Dt_max+1)
                

    def draw_frame(self, framedata, t, x, y):
        self.t = np.append(self.t, t)
        self.x = np.append(self.x, x)
        self.y = np.append(self.y, y)
        
        i          = framedata
        head       = i - 1
        head_len   = 0.1 # secs
        
        i          = i-1
        time_now   = self.t[i]
        Dt = 0.01
        if len(self.t) > 1:
            Dt = self.t[-1] - self.t[-2]
            
        time_past  = time_now - head_len
        i_past     = max(0, int((time_now-self.Dt_max)/Dt))
        head_slice = (self.t > time_past) & (self.t < time_now+Dt/2)
        #print head_slice, ", ", self.t, ", ", time_past, ", ", time_now
        #print "x ", self.x[head_slice], ", y ", self.y[head_slice]
        
        self.line1_History.set_data(self.x[:i], self.y[:i])
        self.line1_Trace.set_data(self.x[head_slice], self.y[head_slice])
        self.line1_NowMarker.set_data(self.x[head], self.y[head])

        self.line2_History.set_data(self.t[i_past:i], self.y[i_past:i])
        self.line2_Trace.set_data(self.t[head_slice], self.y[head_slice])
        self.line2_NowMarker.set_data(self.t[head], self.y[head])

        self.line3_History.set_data(self.t[i_past:i], self.x[i_past:i])
        self.line3_Trace.set_data(self.t[head_slice], self.x[head_slice])
        self.line3_NowMarker.set_data(self.t[head], self.x[head])
        
        if time_now > self.Dt_max:
            self.ax2.set_xlim(time_now-self.Dt_max,time_now+1.0)
            self.ax3.set_xlim(time_now-self.Dt_max,time_now+1.0)

        self._drawn_artists = [self.line1_History, self.line1_Trace, self.line1_NowMarker,
                               self.line2_History, self.line2_Trace, self.line2_NowMarker,
                               self.line3_History, self.line3_Trace, self.line3_NowMarker]
        plt.draw()
        plt.pause(0.00001)
        
        
    
    def new_frame_seq(self):
        self.ax2.set_xlim(0, self.Dt_max+1)
        self.ax3.set_xlim(0, self.Dt_max+1)
        return iter(range(len(self.t)))


    def _init_draw(self):
        lines = [self.line1_History, self.line1_Trace, self.line1_NowMarker,
                 self.line2_History, self.line2_Trace, self.line2_NowMarker,
                 self.line3_History, self.line3_Trace, self.line3_NowMarker]
        for l in lines:
            l.set_data([], [])
            


if __name__ == '__main__':
    ani = SubplotAnimation()
    #ani.save(filename='sim.mp4',fps=30,dpi=300)
    plt.show()
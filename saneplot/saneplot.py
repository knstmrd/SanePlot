import matplotlib as mpl
import matplotlib.pyplot as plt

class SanePlot:
    def __init__(self, figsize=(14.0, 10.0), legendloc='upper right', legend_frame_color='#FFFFFF',
                 fontfamily='fantasy', font='Calibri',
                 legend_size=26, tick_size=24, xy_label_size=32, textsize=27, linewidth=5, markersize=5,
                 xlim=None, ylim=None,
                 text=None, text_x_rel=None, text_x_abs=None, text_y_rel=None, text_y_abs=None,
                 log_x_base=0, log_y_base=0,
                 x_label=None, y_label=None, linechange='monochrome'):
        self._linestyles = None
        if linechange is not None:
            if linechange == 'monochrome':
                self._linestyles = ['k-', 'k--', 'ko', 'k^', 'k:', 'k*']
            elif linechange == 'color':
                self._linestyles = ['k', 'g', 'b', 'r', 'c']
            else:
                self._linestyles = linechange
        
        self._nplots = 0
        self._figsize = figsize  # done
        self._legendloc = legendloc  # done
        self._legend_frame_color = legend_frame_color  # done
        self._fontfamily = fontfamily
        self._font = font
        self._legend_size = legend_size  # done
        self._tick_size = tick_size  # done
        self._xy_label_size = xy_label_size  # done
        self._textsize = textsize  # done
        self._linewidth = linewidth  # done
        self._markersize = markersize  # done
        self._xlim = xlim  # done
        self._ylim = ylim  # done
        self._text = text  # done
        self._text_x_rel = text_x_rel  # done
        self._text_x_abs = text_x_abs  # done
        self._text_y_rel = text_y_rel  # done
        self._text_y_abs = text_y_abs  # done
        self._log_y_base = log_y_base  # done
        self._log_x_base = log_x_base  # done
        self._x_label = x_label  # done
        self._y_label = y_label  # done
        
        
        mpl.rcParams['font.family'] = self._fontfamily
        mpl.rcParams['font.'+self._fontfamily] = self._font
        
        self._fig, self._ax = plt.subplots()
        
        
        self._fig.set_size_inches(self._figsize)
        self._ax.tick_params(labelsize=tick_size)
        
        if self._xlim is not None:
            self._ax.set_xlim(self._xlim)
        if self._ylim is not None:
            self._ax.set_ylim(self._ylim)
        
        if self._log_x_base != 0:
            self._ax.set_xscale('log', basex=self._log_x_base)        
        if self._log_y_base != 0:
            self._ax.set_yscale('log', basex=self._log_y_base)
        
        if x_label is not None:
            self._ax.set_xlabel(x_label, fontsize=self._xy_label_size)
        if y_label is not None:
            self._ax.set_ylabel(y_label, fontsize=self._xy_label_size)

    def add_text(self, textsize=None):
        textpos_x = 0
        textpos_y = 0
        if self._text is not None:
            if self._text_x_rel is not None:
                xl = self._ax.get_xlim()
                textpos_x = xl[0] + (xl[1] - xl[0]) * self._text_x_rel
            else:
                textpos_x = self._text_x_abs
            if self._text_y_rel is not None:
                yl = self._ax.get_ylim()
                textpos_y = yl[0] + (yl[1] - yl[0]) * self._text_y_rel
            else:
                textpos_y = self._text_y_abs
        if textsize is None:
            textsize = self._textsize
        self._ax.text(textpos_x, textpos_y, self._text, fontsize=textsize)
        return self._fig
    
    def plot(self, x, y, label=None, linewidth=None, markersize=None):
        if linewidth is None:
            linewidth = self._linewidth
        if markersize is None:
            markersize = self._markersize
        
        if self._linestyles is not None:
            self._ax.plot(x, y, self._linestyles[self._nplots % len(self._linestyles)], label=label,
                          linewidth=linewidth, markersize=markersize)
        else:
            self._ax.plot(x, y, label=label,
                          linewidth=linewidth, markersize=markersize)
        self._nplots += 1
        return self._fig
        
    def legend(self):
        legend = self._ax.legend(loc=self._legendloc, fontsize=self._legend_size,
                                 prop={'family': self._font, 'size': self._legend_size})
        legend.get_frame().set_facecolor(self._legend_frame_color)
        return self._fig
        
    def show(self):
        return self._fig
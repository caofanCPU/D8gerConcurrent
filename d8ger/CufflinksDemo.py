#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://blog.csdn.net/qdPython/article/details/102568352

import cufflinks as cf
import numpy as np
import pandas as pd
import plotly

setattr(plotly.offline, "__PLOTLY_OFFLINE_INITIALIZED", True)
cf.set_config_file(offline=True)

cf.datagen.box(10).iplot(kind='box', legend=False)
cf.datagen.lines(1, 500).ta_plot(study='sma', periods=[13, 21, 55])

df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.iplot(kind='scatter', mode='markers', colors=['orange', 'teal', 'blue', 'yellow'], size=10)
df.iplot(kind='bubble', x='a', y='b', size='c')

df = pd.DataFrame(np.random.randn(1000, 4), columns=['a', 'b', 'c', 'd'])
df.scatter_matrix()

df = cf.datagen.lines(4)
df.iplot(subplots=True, shape=(4, 1), shared_xaxes=True, vertical_spacing=.02, fill=True)
df.iplot(subplots=True, subplot_titles=True, legend=False)

df = cf.datagen.bubble(10, 50, mode='stocks')
figs = cf.figures(df, [dict(kind='histogram', keys='x', color='blue'),
                       dict(kind='scatter', mode='markers', x='x', y='y', size=5),
                       dict(kind='scatter', mode='markers', x='x', y='y', size=5, color='teal')], asList=True)
figs.append(cf.datagen.lines(1).figure(bestfit=True, colors=['blue'], bestfit_colors=['pink']))
base_layout = cf.tools.get_base_layout(figs)
sp = cf.subplots(figs, shape=(3, 2), base_layout=base_layout, vertical_spacing=.15, horizontal_spacing=.03,
                 specs=[[{'rowspan': 2}, {}], [None, {}], [{'colspan': 2}, None]],
                 subplot_titles=['Histogram', 'Scatter 1', 'Scatter 2', 'Bestfit Line'])
sp['layout'].update(showlegend=False)
cf.iplot(sp)

help(df.iplot)

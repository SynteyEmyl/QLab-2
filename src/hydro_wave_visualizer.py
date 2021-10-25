#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""hydro_wave_visualizer.py:
This file starts the program.
"""

__author__ = 'Miguel Angel Avila Torres'
__copyright__ = 'Copyright 2021, hydro-wave-visualizer'
__credits__ = ['Miguel Angel Avila Torres']
__license__ = 'The Legacy License'
__version__ = '1.0.0'
__maintainer__ = f'{__author__}'
__email__ = None
__status__ = 'Release'


if __name__ == '__main__':
    from controller import mainframe
    
    mainframe.app.mainloop()

    exit(code=0x0)

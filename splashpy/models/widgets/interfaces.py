#
#  This file is part of SplashSync Project.
#
#  Copyright (C) 2015-2019 Splash Sync  <www.splashsync.com>
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#  For the full copyright and license information, please view the LICENSE
#  file that was distributed with this source code.
#

from abc import abstractmethod


class WidgetInterface:
    """Common Functions Interfaces for Widgets Classes"""

    def __init__(self):
        pass

    # ====================================================================#
    #  Widget Definition
    # ====================================================================#

    @abstractmethod
    def description(self):
        """Get Description Array for requested Widget Type"""
        raise NotImplementedError("Not implemented yet.")

    # ====================================================================#
    #  Widget CRUD
    # ====================================================================#

    @abstractmethod
    def get(self, object_id, fields):
        """Return requested Widget Data"""
        raise NotImplementedError("Not implemented yet.")

    @abstractmethod
    def isDisabled( self ):
        """Check if Widget is Disabled"""
        raise NotImplementedError("Not implemented yet.")
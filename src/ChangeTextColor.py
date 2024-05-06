#To clarify this code is to change the text cikir if an item in a QListWidget

from tkinter import Widget
from final.MayaDev.vendor.Maya.PySide2 import QtCore


class ChangeTextColorOfItemInQWidget:
    def clickable(widget):
        """Re implementation Double Click Event on a widget"""

class MouseDoubleClickFilter(QtCore.QObject):
    doubleCLicked = QtCore.pyqtSignal()

    def eventFilter(self,obj,event):
        if obj == Widget:
            if event.type() == QtCore.QEventMouseButtonDblClick:
                self.doubleCLicked.emit()
        
        return True

    filter = MouseDoubleClickFilter(Widget) # type: ignore
    Widget.installEventFilter(filter)

        # Connect the double click signal

    clickable(qlistwidget).connect(handleDoubleClick) # type: ignore
    def handleDoubleClick():

        # Implement your color update logic here

        pass
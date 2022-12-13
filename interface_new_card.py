from PyQt5 import QtCore, QtGui, QtWidgets
import main
from functools import partial


class Ui_Dialog(object):
    def __init__(self):
        self.enter_subject_label = QtWidgets.QLabel(Dialog)
        self.enter_subject = QtWidgets.QLineEdit(Dialog)
        self.new_subject = QtWidgets.QPushButton(Dialog)
        self.button_list = list()
        self.title = QtWidgets.QLabel(Dialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(400, 300)

        height = 250
        self.title.setGeometry(QtCore.QRect(150, 10, 300, 30))
        self.title.setObjectName("title")

        subjects_nb = main.subjects_nb()
        for i in range(subjects_nb):
            self.button_list.append(QtWidgets.QPushButton(Dialog))
            self.button_list[i].setGeometry(QtCore.QRect(50, 30 * i + 50, 300, 30))
            self.button_list[i].setObjectName(main.subject_name(i))
        self.new_subject.setGeometry(QtCore.QRect(50, 30 * subjects_nb + 50, 300, 30))
        self.new_subject.setObjectName("New subject")
        self.enter_subject_label.setGeometry(QtCore.QRect(50, 30 * subjects_nb + 50 + 30, 300, 30))
        self.enter_subject_label.setObjectName("Enter subject label")
        self.enter_subject_label.hide()

        self.retranslateUi(Dialog)
        self.enter_subject.setGeometry(QtCore.QRect(50, 30 * subjects_nb + 60 + 50, 300, 30))
        self.enter_subject.hide()

        self.new_subject.clicked.connect(self.new_sub)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.enter_subject.editingFinished.connect(lambda: which_lesson(self, False))

        for i in range(subjects_nb):
            self.button_list[i].clicked.connect(partial(which_lesson, self, True, j=i))

    def new_sub(self):

        self.enter_subject_label.show()
        self.enter_subject.show()
        for i in range(main.subjects_nb()):
            self.button_list[i].setVisible(False)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        for i in range(main.subjects_nb()):
            self.button_list[i].setText((_translate("Dialog", main.subject_name(i))))
        self.enter_subject_label.setText("Enter the new subject")
        self.new_subject.setText((_translate("Dialog", "New subject")))

        self.title.setText((_translate("Dialog", "New flashcard")))


def new_subject(dialog):
    dialog.enter_subject_label.show()
    dialog.enter_subject.show()
    for i in range(main.subjects_nb()):
        dialog.button_list[i].setVisible(False)


def which_lesson(dialog, boolean, j=0, flag=False):

    if boolean:
        for i in range(main.subjects_nb()):
            dialog.button_list[i].setVisible(False)
            dialog.new_subject.hide()
        lessons_nb = main.lessons_nb(main.subject_name(j))
        print(main.subject_name(j))
        dialog.list_lists = list()
        flag = True
        for i in range(lessons_nb):
            dialog.list_lists.append(QtWidgets.QPushButton(Dialog))
            dialog.list_lists[i].setGeometry(QtCore.QRect(50, 30 * i + main.subjects_nb() + 50, 300, 30))
            dialog.list_lists[i].setText(main.lesson_name(i, main.subject_name(j)))
            dialog.list_lists[i].show()

        dialog.new_list = QtWidgets.QPushButton(Dialog)
        dialog.new_list.setGeometry(
            QtCore.QRect(50, 30 * lessons_nb + main.subjects_nb() + 50, 300, 30))
        dialog.new_list.setObjectName("New list")
        dialog.new_list.setText("New list")
        dialog.title.setText(main.subject_name(j))
        dialog.new_list.show()

    else:
        dialog.new_list = QtWidgets.QPushButton(Dialog)
        dialog.new_list.setGeometry(
            QtCore.QRect(50, 30 * main.subjects_nb() + 50 + 90, 300, 30))
        dialog.new_list.setObjectName("New list")
        dialog.new_list.setText("New list")
        dialog.new_list.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

# close database

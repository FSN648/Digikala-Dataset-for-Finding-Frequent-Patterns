# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DigiKala_API.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import time

#%% Panda Class for Import DataFrame as a table in GUI
class PandasModel(QtCore.QAbstractTableModel): 
    def __init__(self, df = pd.DataFrame(), parent=None): 
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        return QtCore.QVariant(str(self._df.ix[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()
#%% GUI.py file that developted with Qt Designer
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 300))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.sup = QtWidgets.QTextEdit(self.groupBox)
        self.sup.setObjectName("sup")
        self.horizontalLayout_11.addWidget(self.sup)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.length = QtWidgets.QTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setObjectName("length")
        self.horizontalLayout_4.addWidget(self.length)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.conf = QtWidgets.QTextEdit(self.groupBox)
        self.conf.setObjectName("conf")
        self.horizontalLayout_9.addWidget(self.conf)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lift = QtWidgets.QTextEdit(self.groupBox)
        self.lift.setObjectName("lift")
        self.horizontalLayout_10.addWidget(self.lift)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.inyear = QtWidgets.QTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inyear.sizePolicy().hasHeightForWidth())
        self.inyear.setSizePolicy(sizePolicy)
        self.inyear.setObjectName("inyear")
        self.horizontalLayout_2.addWidget(self.inyear)
        self.inmonth = QtWidgets.QTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inmonth.sizePolicy().hasHeightForWidth())
        self.inmonth.setSizePolicy(sizePolicy)
        self.inmonth.setObjectName("inmonth")
        self.horizontalLayout_2.addWidget(self.inmonth)
        self.inday = QtWidgets.QTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inday.sizePolicy().hasHeightForWidth())
        self.inday.setSizePolicy(sizePolicy)
        self.inday.setObjectName("inday")
        self.horizontalLayout_2.addWidget(self.inday)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.outyear = QtWidgets.QTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outyear.sizePolicy().hasHeightForWidth())
        self.outyear.setSizePolicy(sizePolicy)
        self.outyear.setObjectName("outyear")
        self.horizontalLayout_3.addWidget(self.outyear)
        self.outmonth = QtWidgets.QTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outmonth.sizePolicy().hasHeightForWidth())
        self.outmonth.setSizePolicy(sizePolicy)
        self.outmonth.setObjectName("outmonth")
        self.horizontalLayout_3.addWidget(self.outmonth)
        self.outday = QtWidgets.QTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outday.sizePolicy().hasHeightForWidth())
        self.outday.setSizePolicy(sizePolicy)
        self.outday.setObjectName("outday")
        self.horizontalLayout_3.addWidget(self.outday)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.city = QtWidgets.QTextEdit(self.groupBox_2)
        self.city.setObjectName("city")
        self.horizontalLayout_5.addWidget(self.city)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_2.addWidget(self.widget)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.text = QtWidgets.QPlainTextEdit(self.frame)
        self.text.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.text.setFont(font)
        self.text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text.setObjectName("text")
        self.verticalLayout_2.addWidget(self.text)
        self.verticalLayout.addWidget(self.frame)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.primary = QtWidgets.QTableView(self.tab)
        self.primary.setObjectName("primary")
        self.gridLayout.addWidget(self.primary, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.advance = QtWidgets.QTableView(self.tab_2)
        self.advance.setObjectName("advance")
        self.gridLayout_2.addWidget(self.advance, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "کمینه‌ی پارامترهای ورودی"))
        self.label_9.setText(_translate("MainWindow", "Support:"))
        self.label_3.setText(_translate("MainWindow", "Length:"))
        self.label_7.setText(_translate("MainWindow", "Confidence:"))
        self.label_8.setText(_translate("MainWindow", "Lift:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "مکان و زمان مورد بررسی"))
        self.label_10.setText(_translate("MainWindow", "لطفا تاریخ را به صورت میلادی وارد کنید: روز/ماه/سال"))
        self.label.setText(_translate("MainWindow", "تاریخ شروع:"))
        self.label_2.setText(_translate("MainWindow", "تاریخ پایان:"))
        self.label_4.setText(_translate("MainWindow", "نام شهر:"))
        self.pushButton.setText(_translate("MainWindow", "Apriori"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "نتایج اولیه"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "آنالیز پیشرفته"))

#%%Class of Apriori Algorithem
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Apriori_Alg)

    def Apriori_Alg(self):
        self.text.clear()
        self.progressBar.setProperty("value", 0)
        
        jj = 0
        countlist = [10, 27, 43, 67, 89, 100]
        count = countlist[jj]
        time.sleep(1)
        self.progressBar.setValue(count)
        jj += 1
            
        order_org = pd.read_csv('3-p5s3708k.csv')
        order_org = order_org[['DateTime_CartFinalize','ID_Item', 'ID_Customer', 'Quantity_item', 'city_name_fa']]
        product = pd.read_excel('product.xlsx')
        product = product[['id','category_title_fa']]
        product = product.rename(columns={'id':'ID_Item'})
        Meg = pd.merge(order_org, product, on="ID_Item", how='inner',indicator= True)
        Meg['DateTime'] = pd.to_datetime(Meg['DateTime_CartFinalize'])
        Meg['DateTime_CartFinalize'] = pd.to_datetime(Meg['DateTime_CartFinalize'])
        Meg.set_index(['DateTime'],inplace=True)
        Meg.drop(['ID_Item'], axis=1, inplace=True)
        Meg.sort_index(inplace=True)
        
        count = countlist[jj]
        time.sleep(1)
        self.progressBar.setValue(count)
        jj += 1
        
        Inyear = self.inyear.toPlainText()
        Outyear = self.outyear.toPlainText()
        Inmonth = self.inmonth.toPlainText()
        Outmonth = self.outmonth.toPlainText()
        Inday = self.inday.toPlainText()
        Outday = self.outday.toPlainText()
        City = self.city.toPlainText()
        Sup = self.sup.toPlainText()
        Conf = self.conf.toPlainText()
        Lif = self.lift.toPlainText()
        Length = self.length.toPlainText()
        
        if Inyear == '' or Outyear == '' or Inmonth == '' or Outmonth == ''\
        or Inday == '' or Outday == '' or City == '' or Sup == '' or Conf == ''\
        or Lif == '' or Length == '':
            self.text.setPlainText('لطفا مقادیر مورد نیاز را وارد نمایید')
            
        elif int(Inmonth)<=0 or int(Inmonth)>=13 or int(Inday)<=0 or int(Inday)>=32 or \
        int(Outmonth)<=0 or int(Outmonth)>=13 or int(Outday)<=0 or int(Outday)>=32 :
            self.text.setPlainText('تاریخ وارد شده صحیح نیست')
            
        elif City not in Meg.city_name_fa.values:
            self.text.setPlainText('اطلاعاتی در خصوص شهر مورد نظر شما در دسترس نیست')
        else:
            
            Inyear = int(self.inyear.toPlainText())
            Outyear = int(self.outyear.toPlainText())
            Inmonth = int(self.inmonth.toPlainText())
            Outmonth = int(self.outmonth.toPlainText())
            Inday = int(self.inday.toPlainText())
            Outday = int(self.outday.toPlainText())
            Sup = float(self.sup.toPlainText())
            Conf = float(self.conf.toPlainText())
            Lif = float(self.lift.toPlainText())
            Length = int(self.length.toPlainText())
    
            order_fil = Meg[(Meg['DateTime_CartFinalize']>=pd.Timestamp(Inyear,Inmonth,Inday)) & \
                            (Meg['DateTime_CartFinalize']<=pd.Timestamp(Outyear,Outmonth,Outday))& \
                            (Meg['city_name_fa'] == City)]
            
            count = countlist[jj]
            time.sleep(1)
            self.progressBar.setValue(count)
            jj += 1
        
            if order_fil.empty:
                self.text.setPlainText('اطلاعاتی در خصوص شهر مورد نظر شما، در بازه‌ی زمانی مشخص شده، در دسترس نیست')
            else:
                i = 0
                Dic = {}
                for ID in order_fil['ID_Customer']:
                    if ID not in Dic.keys():
                        Dic[ID] = []
                    if order_fil['Quantity_item'][i] > 1:
                        num = 1
                        while num <= order_fil['Quantity_item'][i]:
                            Dic[ID].append(order_fil['category_title_fa'][i])
                            num += 1
                    else:
                        Dic[ID].append(order_fil['category_title_fa'][i])
                    i += 1

                count = countlist[jj]
                time.sleep(1)
                self.progressBar.setValue(count)
                jj += 1
                
                dataset = list(Dic.values()) 
                te = TransactionEncoder()

                te_ary = te.fit(dataset).transform(dataset)
                df_new = pd.DataFrame(te_ary, columns=te.columns_)
                frequent_itemsets = apriori(df_new, min_support=Sup, use_colnames=True)
                frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
                    
                #******for saving time in processing of big data, these codes can be used instead:
                #oht_ary = te.fit(dataset).transform(dataset, sparse=True)
                #sparse_df = pd.SparseDataFrame(oht_ary, columns=te.columns_, default_fill_value=False)
                #sparse_df.columns = [str(i) for i in sparse_df.columns]
                #frequent_itemsets = apriori(sparse_df, min_support=Sup, use_colnames=True, verbose=1, low_memory=False)
                #frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
        
                rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=Conf)
                rules = association_rules(frequent_itemsets, metric="lift", min_threshold=Lif)
                rules["antecedent_len"] = rules["antecedents"].apply(lambda x: len(x))
                rules[ (rules['antecedent_len'] >= Length) ]

                count = countlist[jj]
                time.sleep(1)
                self.progressBar.setValue(count)
                jj += 1
            
                Item_list = []
                for i in frequent_itemsets['itemsets']:
                    sets = [i] 
                    Item_list.append([list(xx) for xx in sets])
                for i in range(len(Item_list)):
                    frequent_itemsets.at[i,'itemsets'] = Item_list[i][0]

                Item_list_rules = []
                for i in rules['antecedents']:
                    sets = [i] 
                    Item_list_rules.append([list(xx) for xx in sets])
                for i in range(len(Item_list_rules)):
                    rules.at[i,'antecedents'] = Item_list_rules[i][0]

                Item_list_rules2 = []
                for i in rules['consequents']:
                    sets = [i] 
                    Item_list_rules2.append([list(xx) for xx in sets])
                for i in range(len(Item_list_rules2)):
                    rules.at[i,'consequents'] = Item_list_rules2[i][0]
                    
                frequent_itemsets = frequent_itemsets.round(2)
                rules = rules.round(2)
                
                count = countlist[jj]
                time.sleep(1)
                self.progressBar.setValue(count)
                jj += 1
                    
                if rules.empty:
                    self.text.setPlainText('هیچگونه تحلیل پیشرفته‌ای در دست نیست')
                
                primaryResults = PandasModel(frequent_itemsets)
                AdvanceResults = PandasModel(rules)
                self.advance.setModel(AdvanceResults)
                self.primary.setModel(primaryResults)
                
     
#%%
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())


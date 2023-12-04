from PySide6.QtWidgets import QApplication,QWidget
from PySide6 import QtGui,QtWidgets
from Ui_單形法 import Ui_Form
import matplotlib.pyplot as plt
import numpy as np
class MyWindow(Ui_Form,QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        plt.axis('off')
        plt.savefig('temp.png',dpi=300)
        plt.close()
        self.img=QtGui.QPixmap('temp.png')
        self.img=self.img.scaled(800,600)
        scene=QtWidgets.QGraphicsScene(self)
        scene.addPixmap(self.img)
        self.graphicsView.setScene(scene)
        self.matrix=[[0 for i in range(6)] for i in range(8)]
        self.pushButton.setEnabled(False)
        self.executing=False
        self.canexec=False
        self.bind()
    def bind(self):
        self.spinBox_1.valueChanged.connect(self.change)
        self.spinBox_2.valueChanged.connect(self.change)
        self.spinBox_3.valueChanged.connect(self.change)
        self.spinBox_4.valueChanged.connect(self.change)
        self.spinBox_5.valueChanged.connect(self.change)
        self.spinBox_11.valueChanged.connect(self.change)
        self.spinBox_12.valueChanged.connect(self.change)
        self.spinBox_13.valueChanged.connect(self.change)
        self.spinBox_14.valueChanged.connect(self.change)
        self.spinBox_15.valueChanged.connect(self.change)
        self.spinBox_16.valueChanged.connect(self.change)
        self.spinBox_17.valueChanged.connect(self.change)
        self.spinBox_18.valueChanged.connect(self.change)
        self.spinBox_19.valueChanged.connect(self.change)
        self.spinBox_20.valueChanged.connect(self.change)
        self.spinBox_21.valueChanged.connect(self.change)
        self.spinBox_22.valueChanged.connect(self.change)
        self.spinBox_23.valueChanged.connect(self.change)
        self.spinBox_24.valueChanged.connect(self.change)
        self.spinBox_25.valueChanged.connect(self.change)
        self.spinBox_26.valueChanged.connect(self.change)
        self.spinBox_27.valueChanged.connect(self.change)
        self.spinBox_28.valueChanged.connect(self.change)
        self.spinBox_29.valueChanged.connect(self.change)
        self.spinBox_30.valueChanged.connect(self.change)
        self.spinBox_31.valueChanged.connect(self.change)
        self.spinBox_32.valueChanged.connect(self.change)
        self.spinBox_33.valueChanged.connect(self.change)
        self.spinBox_34.valueChanged.connect(self.change)
        self.spinBox_35.valueChanged.connect(self.change)
        self.spinBox_36.valueChanged.connect(self.change)
        self.spinBox_37.valueChanged.connect(self.change)
        self.spinBox_38.valueChanged.connect(self.change)
        self.spinBox_39.valueChanged.connect(self.change)
        self.spinBox_40.valueChanged.connect(self.change)
        self.spinBox_41.valueChanged.connect(self.change)
        self.spinBox_42.valueChanged.connect(self.change)
        self.spinBox_43.valueChanged.connect(self.change)
        self.spinBox_44.valueChanged.connect(self.change)
        self.spinBox_45.valueChanged.connect(self.change)
        self.spinBox_46.valueChanged.connect(self.change)
        self.spinBox_47.valueChanged.connect(self.change)
        self.spinBox_48.valueChanged.connect(self.change)
        self.spinBox_49.valueChanged.connect(self.change)
        self.spinBox_50.valueChanged.connect(self.change)
        self.spinBox_51.valueChanged.connect(self.change)
        self.spinBox_52.valueChanged.connect(self.change)
        self.pushButton.clicked.connect(self.push)
        self.radioButton.clicked.connect(self.change)
        self.radioButton_2.clicked.connect(self.change)
        self.checkBox.clicked.connect(self.change)
    
    def push(self):
        if not self.executing:
            self.a=self.trans_matrix(self.matrix)
            self.basic=[]
            for i in range(2,len(self.a)):
                self.basic.append(self.a[i][0])
            self.unbasic=[]
            for i in range(2,len(self.a[0])-len(self.a)+1):
                self.unbasic.append(self.a[0][i])
            self.BV=[i[0] for i in self.a]
        if self.checkBox.isChecked():
            while True:
                re=self.simplex(self.a,self.BV,self.basic,self.unbasic)
                self.a=re[1]
                self.basic=re[3]
                self.unbasic=re[2]
                if re[0]==0:
                    symbol=[]
                    ans=[]
                    for i in range(2,len(self.a[0])-1):
                        if self.a[0][i] in self.basic:
                            symbol.append(self.a[0][i])
                            ans.append(self.a[self.basic.index(self.a[0][i])+2][len(self.a[0])-1])
                        elif self.a[0][i] in self.unbasic:
                            symbol.append(self.a[0][i])
                            ans.append(0)
                    s=''
                    for i in range(len(symbol)):
                        s=s+str(symbol[i])+' = '+str(ans[i])+'\n'
                    if self.a[0][1]=='m':
                        self.textEdit.setText('最佳解為'+str(self.a[1][len(self.a[0])-1]*-1)+'，此時\n'+s)
                    elif self.a[0][1]=='M':
                        self.textEdit.setText('最佳解為'+str(self.a[1][len(self.a[0])-1])+'，此時\n'+s)
                    break
                elif re[0]==1:
                    self.textEdit.setText('無解')
                    break
            self.draw(self.a)
            self.executing=False
        elif not self.checkBox.isChecked():
            self.executing=True
            self.lock()
            re=self.simplex(self.a,self.BV,self.basic,self.unbasic)
            self.a=re[1]
            self.basic=re[3]
            self.unbasic=re[2]
            if re[0]==0:
                symbol=[]
                ans=[]
                for i in range(2,len(self.a[0])-1):
                    if self.a[0][i] in self.basic:
                        symbol.append(self.a[0][i])
                        ans.append(self.a[self.basic.index(self.a[0][i])+2][len(self.a[0])-1])
                    elif self.a[0][i] in self.unbasic:
                        symbol.append(self.a[0][i])
                        ans.append(0)
                s=''
                for i in range(len(symbol)):
                    s=s+str(symbol[i])+' = '+str(ans[i])+'\n'
                if self.a[0][1]=='m':
                    self.textEdit.setText('最佳解為'+str(self.a[1][len(self.a[0])-1]*-1)+'，此時\n'+s)
                elif self.a[0][1]=='M':
                    self.textEdit.setText('最佳解為'+str(self.a[1][len(self.a[0])-1])+'，此時\n'+s)
                self.executing=False
            elif re[0]==1:
                self.textEdit.setText('無解')
                self.executing=False
            elif re[0]==2:
                self.textEdit.setText('進行中...')
                
        self.draw(self.a)
        self.lock()
            
    def simplex(self,a,BV,basic,unbasic):
        for i in range(2,len(a)):
            if a[i][len(a[0])-1]<0:
                co=True
                for j in range(2,len(a[0])-1):
                    if a[i][j]<0:
                        co=False
                        break
                if not co:
                    for j in range(2,len(a[0])):
                        a[i][j]=a[i][j]*-1
                elif co:
                    re=[1,a,unbasic,basic]
                    return re
            elif a[i][len(a[0])-1]>0:
                co=True
                for j in range(2,len(a[0])-1):
                    if a[i][j]>0:
                        co=False
                        break
                if co:
                    re=[1,a,unbasic,basic]
                    return re
        allnotnegatives=True
        for i in range(2,len(a[0])-1):
            if a[1][i]<0:
                allnotnegatives=False
        if allnotnegatives:
            #[state,answer,unbasic,basic]
            re=[0,a,unbasic,basic]
            return re
        temp=0
        for i in range(2,len(a[0])-1):
            if a[1][i]<temp:
                temp=a[1][i]
                entering=a[0][i]
        noanswer=True
        for i in basic:
            if a[BV.index(i)][a[0].index(entering)]>0:
                temp=a[BV.index(i)][a[0].index("RHS")]/a[BV.index(i)][a[0].index(entering)]
                pivot=i
                noanswer=False
                break
        if noanswer:
            re=[1,a,unbasic,basic]
            return re
        for i in basic:
            if a[BV.index(i)][a[0].index(entering)]>0 and a[BV.index(i)][a[0].index("RHS")]/a[BV.index(i)][a[0].index(entering)]<temp:
                temp=a[BV.index(i)][a[0].index("RHS")]/a[BV.index(i)][a[0].index(entering)]
                pivot=i
        temp=a[BV.index(pivot)][a[0].index(entering)]
        for i in range(2,len(a[0])):
            a[BV.index(pivot)][i]=a[BV.index(pivot)][i]/temp
        for i in range(1,len(a)):
            if i==BV.index(pivot):
                continue
            if a[i][a[0].index(entering)]!=0:
                temp=a[i][a[0].index(entering)]
                for j in range(2,len(a[0])):
                    a[i][j]=a[i][j]-a[BV.index(pivot)][j]*temp
        basic[basic.index(pivot)]=entering
        unbasic[unbasic.index(entering)]=pivot
        BV[BV.index(pivot)]=entering
        a[BV.index(entering)][0]=entering
        for i in range(2,len(a)):
            if a[i][len(a[0])-1]<0:
                co=True
                for j in range(2,len(a[0])-1):
                    if a[i][j]<0:
                        co=False
                        break
                if not co:
                    for j in range(2,len(a[0])):
                        a[i][j]=a[i][j]*-1
                elif co:
                    re=[1,a,unbasic,basic]
                    return re
            elif a[i][len(a[0])-1]>0:
                co=True
                for j in range(2,len(a[0])-1):
                    if a[i][j]>0:
                        co=False
                        break
                if co:
                    re=[1,a,unbasic,basic]
                    return re
        allnotnegatives=True
        for i in range(2,len(a[0])-1):
            if a[1][i]<0:
                allnotnegatives=False
        if allnotnegatives:
            #[state,answer,unbasic,basic]
            re=[0,a,unbasic,basic]
            return re
        re=[2,a,unbasic,basic]
        return re
        
    def trans_matrix(self,matrix):
        trans_matrix=[["BV"]]
        if matrix[0][0]==0:
            trans_matrix[0].append('M')
        elif matrix[0][0]==1:
            trans_matrix[0].append('m')
        if trans_matrix[0][1]=='M':
            trans_matrix.append(['M',1])
        elif trans_matrix[0][1]=='m':
            trans_matrix.append(['m',-1])
        b=[]
        for i in range(1,6):
            if matrix[0][i]!=0:
                b.append(i)
                trans_matrix[0].append(chr(ord('a')-1+i))
                if trans_matrix[0][1]=='M':
                    trans_matrix[1].append(matrix[0][i]*-1)
                elif trans_matrix[0][1]=='m':
                    trans_matrix[1].append(matrix[0][i])
        a=[]
        for i in range(1,8):
            allzero=True
            for j in range(5):
                if matrix[i][j]!=0:
                    allzero=False
                    break
            if not allzero:
                a.append(i)
        for i in range(len(a)):
            trans_matrix[0].append('s'+str(i+1))
            trans_matrix[1].append(0)
        trans_matrix[0].append('RHS')
        trans_matrix[1].append(0)
        for i in range(len(a)):
            trans_matrix.append(['s'+str(i+1),0])
            for j in range(5):
                if j+1 in b:
                    trans_matrix[i+2].append(matrix[a[i]][j])
            for k in range(i):
                trans_matrix[i+2].append(0)
            trans_matrix[i+2].append(1)
            for l in range(len(a)-i-1):
                trans_matrix[i+2].append(0)
            trans_matrix[i+2].append(matrix[a[i]][5])
        return trans_matrix
    
    def lock(self):
        if self.executing:
            self.spinBox_1.setReadOnly(True)
            self.spinBox_2.setReadOnly(True)
            self.spinBox_3.setReadOnly(True)
            self.spinBox_4.setReadOnly(True)
            self.spinBox_5.setReadOnly(True)
            self.spinBox_11.setReadOnly(True)
            self.spinBox_12.setReadOnly(True)
            self.spinBox_13.setReadOnly(True)
            self.spinBox_14.setReadOnly(True)
            self.spinBox_15.setReadOnly(True)
            self.spinBox_16.setReadOnly(True)
            self.spinBox_17.setReadOnly(True)
            self.spinBox_18.setReadOnly(True)
            self.spinBox_19.setReadOnly(True)
            self.spinBox_20.setReadOnly(True)
            self.spinBox_21.setReadOnly(True)
            self.spinBox_22.setReadOnly(True)
            self.spinBox_23.setReadOnly(True)
            self.spinBox_24.setReadOnly(True)
            self.spinBox_25.setReadOnly(True)
            self.spinBox_26.setReadOnly(True)
            self.spinBox_27.setReadOnly(True)
            self.spinBox_28.setReadOnly(True)
            self.spinBox_29.setReadOnly(True)
            self.spinBox_30.setReadOnly(True)
            self.spinBox_31.setReadOnly(True)
            self.spinBox_32.setReadOnly(True)
            self.spinBox_33.setReadOnly(True)
            self.spinBox_34.setReadOnly(True)
            self.spinBox_35.setReadOnly(True)
            self.spinBox_36.setReadOnly(True)
            self.spinBox_37.setReadOnly(True)
            self.spinBox_38.setReadOnly(True)
            self.spinBox_39.setReadOnly(True)
            self.spinBox_40.setReadOnly(True)
            self.spinBox_41.setReadOnly(True)
            self.spinBox_42.setReadOnly(True)
            self.spinBox_43.setReadOnly(True)
            self.spinBox_44.setReadOnly(True)
            self.spinBox_45.setReadOnly(True)
            self.spinBox_46.setReadOnly(True)
            self.spinBox_47.setReadOnly(True)
            self.spinBox_48.setReadOnly(True)
            self.spinBox_49.setReadOnly(True)
            self.spinBox_50.setReadOnly(True)
            self.spinBox_51.setReadOnly(True)
            self.spinBox_52.setReadOnly(True)
            self.radioButton.setDisabled(True)
            self.radioButton_2.setDisabled(True)
        else:
            self.spinBox_1.setReadOnly(False)
            self.spinBox_2.setReadOnly(False)
            self.spinBox_3.setReadOnly(False)
            self.spinBox_4.setReadOnly(False)
            self.spinBox_5.setReadOnly(False)
            self.radioButton.setEnabled(True)
            self.radioButton_2.setEnabled(True)
            
    def change(self):
        self.spin_detect()
        self.radio_detect()
        self.matrix_bind()
        self.message()
        self.lock()
        if self.canexec:
            self.pushButton.setEnabled(True)
            a=self.trans_matrix(self.matrix)
            self.draw(a)
        else:
            self.pushButton.setEnabled(False)
            plt.axis('off')
            plt.savefig('temp.png',dpi=300)
            plt.close()
            self.img=QtGui.QPixmap('temp.png')
            self.img=self.img.scaled(800,600)
            scene=QtWidgets.QGraphicsScene(self)
            scene.addPixmap(self.img)
            self.graphicsView.setScene(scene)
            
    def spin_detect(self):
        if self.spinBox_1.value()==0:
            self.spinBox_11.setValue(0)
            self.spinBox_11.setReadOnly(True)
            self.spinBox_17.setValue(0)
            self.spinBox_17.setReadOnly(True)
            self.spinBox_23.setValue(0)
            self.spinBox_23.setReadOnly(True)
            self.spinBox_29.setValue(0)
            self.spinBox_29.setReadOnly(True)
            self.spinBox_35.setValue(0)
            self.spinBox_35.setReadOnly(True)
            self.spinBox_41.setValue(0)
            self.spinBox_41.setReadOnly(True)
            self.spinBox_47.setValue(0)
            self.spinBox_47.setReadOnly(True)
        else:
            self.spinBox_11.setReadOnly(False)
            self.spinBox_17.setReadOnly(False)
            self.spinBox_23.setReadOnly(False)
            self.spinBox_29.setReadOnly(False)
            self.spinBox_35.setReadOnly(False)
            self.spinBox_41.setReadOnly(False)
            self.spinBox_47.setReadOnly(False)
        if self.spinBox_2.value()==0:
            self.spinBox_12.setValue(0)
            self.spinBox_12.setReadOnly(True)
            self.spinBox_18.setValue(0)
            self.spinBox_18.setReadOnly(True)
            self.spinBox_24.setValue(0)
            self.spinBox_24.setReadOnly(True)
            self.spinBox_30.setValue(0)
            self.spinBox_30.setReadOnly(True)
            self.spinBox_36.setValue(0)
            self.spinBox_36.setReadOnly(True)
            self.spinBox_42.setValue(0)
            self.spinBox_42.setReadOnly(True)
            self.spinBox_48.setValue(0)
            self.spinBox_48.setReadOnly(True)
        else:
            self.spinBox_12.setReadOnly(False)
            self.spinBox_18.setReadOnly(False)
            self.spinBox_24.setReadOnly(False)
            self.spinBox_30.setReadOnly(False)
            self.spinBox_36.setReadOnly(False)
            self.spinBox_42.setReadOnly(False)
            self.spinBox_48.setReadOnly(False)
        if self.spinBox_3.value()==0:
            self.spinBox_13.setValue(0)
            self.spinBox_13.setReadOnly(True)
            self.spinBox_19.setValue(0)
            self.spinBox_19.setReadOnly(True)
            self.spinBox_25.setValue(0)
            self.spinBox_25.setReadOnly(True)
            self.spinBox_31.setValue(0)
            self.spinBox_31.setReadOnly(True)
            self.spinBox_37.setValue(0)
            self.spinBox_37.setReadOnly(True)
            self.spinBox_43.setValue(0)
            self.spinBox_43.setReadOnly(True)
            self.spinBox_49.setValue(0)
            self.spinBox_49.setReadOnly(True)
        else:
            self.spinBox_13.setReadOnly(False)
            self.spinBox_19.setReadOnly(False)
            self.spinBox_25.setReadOnly(False)
            self.spinBox_31.setReadOnly(False)
            self.spinBox_37.setReadOnly(False)
            self.spinBox_43.setReadOnly(False)
            self.spinBox_49.setReadOnly(False)
        if self.spinBox_4.value()==0:
            self.spinBox_14.setValue(0)
            self.spinBox_14.setReadOnly(True)
            self.spinBox_20.setValue(0)
            self.spinBox_20.setReadOnly(True)
            self.spinBox_26.setValue(0)
            self.spinBox_26.setReadOnly(True)
            self.spinBox_32.setValue(0)
            self.spinBox_32.setReadOnly(True)
            self.spinBox_38.setValue(0)
            self.spinBox_38.setReadOnly(True)
            self.spinBox_44.setValue(0)
            self.spinBox_44.setReadOnly(True)
            self.spinBox_50.setValue(0)
            self.spinBox_50.setReadOnly(True)
        else:
            self.spinBox_14.setReadOnly(False)
            self.spinBox_20.setReadOnly(False)
            self.spinBox_26.setReadOnly(False)
            self.spinBox_32.setReadOnly(False)
            self.spinBox_38.setReadOnly(False)
            self.spinBox_44.setReadOnly(False)
            self.spinBox_50.setReadOnly(False)
        if self.spinBox_5.value()==0:
            self.spinBox_15.setValue(0)
            self.spinBox_15.setReadOnly(True)
            self.spinBox_21.setValue(0)
            self.spinBox_21.setReadOnly(True)
            self.spinBox_27.setValue(0)
            self.spinBox_27.setReadOnly(True)
            self.spinBox_33.setValue(0)
            self.spinBox_33.setReadOnly(True)
            self.spinBox_39.setValue(0)
            self.spinBox_39.setReadOnly(True)
            self.spinBox_45.setValue(0)
            self.spinBox_45.setReadOnly(True)
            self.spinBox_51.setValue(0)
            self.spinBox_51.setReadOnly(True)
        else:
            self.spinBox_15.setReadOnly(False)
            self.spinBox_21.setReadOnly(False)
            self.spinBox_27.setReadOnly(False)
            self.spinBox_33.setReadOnly(False)
            self.spinBox_39.setReadOnly(False)
            self.spinBox_45.setReadOnly(False)
            self.spinBox_51.setReadOnly(False)
        if self.spinBox_11.value()==0 and self.spinBox_12.value()==0 and self.spinBox_13.value()==0 and self.spinBox_14.value()==0 and self.spinBox_15.value()==0:
            self.spinBox_16.setValue(0)
            self.spinBox_16.setReadOnly(True)
        else:
            self.spinBox_16.setReadOnly(False)
        if self.spinBox_17.value()==0 and self.spinBox_18.value()==0 and self.spinBox_19.value()==0 and self.spinBox_20.value()==0 and self.spinBox_21.value()==0:
            self.spinBox_22.setValue(0)
            self.spinBox_22.setReadOnly(True)
        else:
            self.spinBox_22.setReadOnly(False)
        if self.spinBox_23.value()==0 and self.spinBox_24.value()==0 and self.spinBox_25.value()==0 and self.spinBox_26.value()==0 and self.spinBox_27.value()==0:
            self.spinBox_28.setValue(0)
            self.spinBox_28.setReadOnly(True)
        else:
            self.spinBox_28.setReadOnly(False)
        if self.spinBox_29.value()==0 and self.spinBox_30.value()==0 and self.spinBox_31.value()==0 and self.spinBox_32.value()==0 and self.spinBox_33.value()==0:
            self.spinBox_34.setValue(0)
            self.spinBox_34.setReadOnly(True)
        else:
            self.spinBox_34.setReadOnly(False)
        if self.spinBox_35.value()==0 and self.spinBox_36.value()==0 and self.spinBox_37.value()==0 and self.spinBox_38.value()==0 and self.spinBox_39.value()==0:
            self.spinBox_40.setValue(0)
            self.spinBox_40.setReadOnly(True)
        else:
            self.spinBox_40.setReadOnly(False)
        if self.spinBox_41.value()==0 and self.spinBox_42.value()==0 and self.spinBox_43.value()==0 and self.spinBox_44.value()==0 and self.spinBox_45.value()==0:
            self.spinBox_46.setValue(0)
            self.spinBox_46.setReadOnly(True)
        else:
            self.spinBox_46.setReadOnly(False)
        if self.spinBox_47.value()==0 and self.spinBox_48.value()==0 and self.spinBox_49.value()==0 and self.spinBox_50.value()==0 and self.spinBox_51.value()==0:
            self.spinBox_52.setValue(0)
            self.spinBox_52.setReadOnly(True)
        else:
            self.spinBox_52.setReadOnly(False)

    def matrix_bind(self):
        if self.radioButton.isChecked():
            self.matrix[0][0]=0
        elif self.radioButton_2.isChecked():
            self.matrix[0][0]=1
        self.matrix[0][1]=self.spinBox_1.value()
        self.matrix[0][2]=self.spinBox_2.value()
        self.matrix[0][3]=self.spinBox_3.value()
        self.matrix[0][4]=self.spinBox_4.value()
        self.matrix[0][5]=self.spinBox_5.value()
        self.matrix[1][0]=self.spinBox_11.value()
        self.matrix[1][1]=self.spinBox_12.value()
        self.matrix[1][2]=self.spinBox_13.value()
        self.matrix[1][3]=self.spinBox_14.value()
        self.matrix[1][4]=self.spinBox_15.value()
        self.matrix[1][5]=self.spinBox_16.value()
        self.matrix[2][0]=self.spinBox_17.value()
        self.matrix[2][1]=self.spinBox_18.value()
        self.matrix[2][2]=self.spinBox_19.value()
        self.matrix[2][3]=self.spinBox_20.value()
        self.matrix[2][4]=self.spinBox_21.value()
        self.matrix[2][5]=self.spinBox_22.value()
        self.matrix[3][0]=self.spinBox_23.value()
        self.matrix[3][1]=self.spinBox_24.value()
        self.matrix[3][2]=self.spinBox_25.value()
        self.matrix[3][3]=self.spinBox_26.value()
        self.matrix[3][4]=self.spinBox_27.value()
        self.matrix[3][5]=self.spinBox_28.value()
        self.matrix[4][0]=self.spinBox_29.value()
        self.matrix[4][1]=self.spinBox_30.value()
        self.matrix[4][2]=self.spinBox_31.value()
        self.matrix[4][3]=self.spinBox_32.value()
        self.matrix[4][4]=self.spinBox_33.value()
        self.matrix[4][5]=self.spinBox_34.value()
        self.matrix[5][0]=self.spinBox_35.value()
        self.matrix[5][1]=self.spinBox_36.value()
        self.matrix[5][2]=self.spinBox_37.value()
        self.matrix[5][3]=self.spinBox_38.value()
        self.matrix[5][4]=self.spinBox_39.value()
        self.matrix[5][5]=self.spinBox_40.value()
        self.matrix[6][0]=self.spinBox_41.value()
        self.matrix[6][1]=self.spinBox_42.value()
        self.matrix[6][2]=self.spinBox_43.value()
        self.matrix[6][3]=self.spinBox_44.value()
        self.matrix[6][4]=self.spinBox_45.value()
        self.matrix[6][5]=self.spinBox_46.value()
        self.matrix[7][0]=self.spinBox_47.value()
        self.matrix[7][1]=self.spinBox_48.value()
        self.matrix[7][2]=self.spinBox_49.value()
        self.matrix[7][3]=self.spinBox_50.value()
        self.matrix[7][4]=self.spinBox_51.value()
        self.matrix[7][5]=self.spinBox_52.value()

    def radio_detect(self):
        if self.radioButton.isChecked():
            self.label_6.setText('e  =  M')
        elif self.radioButton_2.isChecked():
            self.label_6.setText('e  =  m')
        
    def draw(self,a):
        xticks = len(a[0])
        yticks = len(a)
        plt.axis([0,xticks,0,yticks])
        for i in range(yticks):
            for j in range(xticks):
                plt.text(j+0.5,(yticks-i)-0.5,a[i][j],va='center',ha='center')
            plt.plot([0,xticks],[i+1,i+1],color='black')
        for i in range(xticks):
            plt.plot([i+1,i+1],[0,yticks],color='black')
        plt.xticks([])
        plt.yticks([])
        plt.savefig('temp.png',dpi=300)
        plt.close()
        self.img=QtGui.QPixmap('temp.png')
        self.img=self.img.scaled(800,600)
        self.graphicsView.scene().clear()
        scene=QtWidgets.QGraphicsScene(self)
        scene.addPixmap(self.img)
        self.graphicsView.setScene(scene)
    def message(self):
        func_zero=True
        for i in range(1,6):
            if self.matrix[0][i]!=0:
                func_zero=False
                break
        limit_zero=True
        for i in range(1,8):
            for j in range(0,5):
                if self.matrix[i][j]!=0:
                    limit_zero=False
                    break
        if func_zero:
            self.canexec=False
            self.textEdit.setText('請輸入函式')
        elif limit_zero:
            self.canexec=False
            self.textEdit.setText('請輸入限制式')
        else:
            self.canexec=True
            self.textEdit.setText('')

if __name__=='__main__':
    app=QApplication([])
    window=MyWindow()
    window.show()
    app.exec()
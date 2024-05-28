# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:32:40 2023

@author: anus_
"""

import sys
import math
from scipy.stats import norm
from PyQt6.QtWidgets import (QApplication, QFormLayout, QLineEdit, QPushButton, QDialog)

class SomeWindow(QDialog):
    def __init__(self):
        super().__init__()

        layout = QFormLayout()

        # Asset Price
        self.assetPrice = QLineEdit()
        self.assetPrice.setObjectName("assetprice")
        self.assetPrice.setText("100")

        # Strike Price
        self.strikePrice = QLineEdit()
        self.strikePrice.setObjectName("strikePrice")
        self.strikePrice.setText("100")

        # St Dev
        self.stdev = QLineEdit()
        self.stdev.setObjectName("stdev")
        self.stdev.setText("0.2")

        # Risk Free Rate
        self.rf = QLineEdit()
        self.rf.setObjectName("rf")
        self.rf.setText("0.06")

        # Time Years
        self.timeyears = QLineEdit()
        self.timeyears.setObjectName("timeyears")
        self.timeyears.setText("0.25")

        # Submit Button
        self.submit_btn = QPushButton()
        self.submit_btn.setObjectName("submit_btn")
        self.submit_btn.setText("Calculate Call Price")

        # Output
        self.Output = QLineEdit()
        self.Output.setObjectName("output")
        self.Output.setText("0")

        layout.addRow("Enter Asset Price", self.assetPrice)
        layout.addRow("Enter Strike Price", self.strikePrice)
        layout.addRow("Enter StDev", self.stdev)
        layout.addRow("Enter Rf", self.rf)
        layout.addRow("Enter Time Years", self.timeyears)
        layout.addRow(self.submit_btn)
        layout.addRow("Call Price", self.Output)

        self.setLayout(layout)

        self.submit_btn.clicked.connect(self.callPriceCalc)
        self.Output.setEnabled(False)

        self.assetPrice.textChanged.connect(self.callPriceCalc)
        self.strikePrice.textChanged.connect(self.callPriceCalc)
        self.rf.textChanged.connect(self.callPriceCalc)
        self.timeyears.textChanged.connect(self.callPriceCalc)
        self.stdev.textChanged.connect(self.callPriceCalc)

    def callPriceCalc(self):
        AssetPrice = float(self.assetPrice.text())
        StrikePrice = float(self.strikePrice.text())
        StDev = float(self.stdev.text())
        Rf = float(self.rf.text())
        TimeYears = float(self.timeyears.text())

        num1 = math.log(AssetPrice/StrikePrice)
        num2 = (Rf + ( (StDev**2) / 2))*TimeYears
        den = StDev*(TimeYears**.5)
        d1 = (num1+num2)/den
        d2 = d1 - den

        nd1 = norm.cdf(d1)
        nd2 = norm.cdf(d2)

        callPrice = round(AssetPrice*nd1 - StrikePrice*nd2*math.exp(-Rf * TimeYears),2)

        self.Output.setText(f'{callPrice}')



app = QApplication(sys.argv)
SomeForm = SomeWindow()
SomeForm.show()
sys.exit(app.exec())


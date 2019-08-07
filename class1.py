def PopulateForm(self):
        layout = QVBoxLayout()
        label = QtWidgets.QLabel()
        label.setText("Notes about sample %s" % idc.GetInputMD5())

        self.editor = QtWidgets.QTextEdit()

        self.editor.setFontFamily(self.skel_settings.notepad_font_name)
        self.editor.setFontPointSize(self.skel_settings.notepad_font_size)

        text = self.skel_conn.get_abstract()
        self.editor.setPlainText(text)

        # editor.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.editor.textChanged.connect(self._onTextChange)

        layout.addWidget(label)
        layout.addWidget(self.editor)
        self.setLayout(layout
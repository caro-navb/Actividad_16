from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from administrador_particulas import Administrador
from particula import Particula
from pprint import pprint, pformat
from collections import deque

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.administrador_particulas = Administrador()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.grafo = dict()
        self.grafo2 = dict()
        self.ui.pushButton.clicked.connect(self.click_agregar)
        self.ui.pushButton_3.clicked.connect(self.click_agregar_inicio)
        self.ui.pushButton_4.clicked.connect(self.click_mostrar)
        
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        self.ui.actionDiccionario.triggered.connect(self.action_diccionario)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.Profundidad_pushButton.clicked.connect(self.busqueda_profundidad)
        self.ui.Amplitud_pushButton.clicked.connect(self.busqueda_amplitud)

    
    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEdit.clear()
        str = pformat(self.grafo, width=50, indent=1)
        self.ui.plainTextEdit.insertPlainText(str)

    @Slot()
    def click_agregar(self):
        id = self.ui.lineEdit_2.text()
        origenx = self.ui.spinBox_13.value()
        origeny = self.ui.spinBox_16.value()
        destinox = self.ui.spinBox_15.value()
        destinoy = self.ui.spinBox_11.value()
        velocidad = self.ui.lineEdit.text()
        red = self.ui.spinBox_9.value()
        green = self.ui.spinBox_10.value()
        blue = self.ui.spinBox_14.value()

        particula = Particula(id, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        self.administrador_particulas.agregar_final(particula)
        
        origen = (particula.origenx, particula.origeny)
        destino = (particula.destinox, particula.destinoy)
        peso = particula.distancia
        
        arista_o_d = (particula.destinox, particula.destinoy, peso)
        arista_d_o = (particula.origenx, particula.origeny, peso)

        if origen in self.grafo:
            self.grafo[origen].append(arista_o_d)
        else:
            self.grafo[origen] = [arista_o_d]
        if destino in self.grafo:
            self.grafo[destino].append(arista_d_o)
        else:
            self.grafo[destino] = [arista_d_o]
        
        arista_o_d = (particula.destinox, particula.destinoy)
        arista_d_o = (particula.origenx, particula.origeny)

        if origen in self.grafo2:
            self.grafo2[origen].append(arista_o_d)
        else:
            self.grafo2[origen] = [arista_o_d]
        if destino in self.grafo2:
            self.grafo2[destino].append(arista_d_o)
        else:
            self.grafo2[destino] = [arista_d_o]

    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.lineEdit_2.text()
        origenx = self.ui.spinBox_13.value()
        origeny = self.ui.spinBox_16.value()
        destinox = self.ui.spinBox_15.value()
        destinoy = self.ui.spinBox_11.value()
        velocidad = self.ui.lineEdit.text()
        red = self.ui.spinBox_9.value()
        green = self.ui.spinBox_10.value()
        blue = self.ui.spinBox_14.value()

        origen = (particula.origenx, particula.origeny)
        destino = (particula.destinox, particula.destinoy)
        peso = particula.distancia
        
        arista_o_d = (particula.destinox, particula.destinoy, peso)
        arista_d_o = (particula.origenx, particula.origeny, peso)

        if origen in self.grafo:
            self.grafo[origen].append(arista_o_d)
        else:
            self.grafo[origen] = [arista_o_d]
        if destino in self.grafo:
            self.grafo[destino].append(arista_d_o)
        else:
            self.grafo[destino] = [arista_d_o]

        arista_o_d = (particula.destinox, particula.destinoy)
        arista_d_o = (particula.origenx, particula.origeny)

        if origen in self.grafo2:
            self.grafo2[origen].append(arista_o_d)
        else:
            self.grafo2[origen] = [arista_o_d]
        if destino in self.grafo2:
            self.grafo2[destino].append(arista_d_o)
        else:
            self.grafo2[destino] = [arista_d_o]

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.administrador_particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
            for particula in self.administrador_particulas:
                origen = (particula.origenx, particula.origeny)
                destino = (particula.destinox, particula.destinoy)
                peso = particula.distancia
        
                arista_o_d = (particula.destinox, particula.destinoy, peso)
                arista_d_o = (particula.origenx, particula.origeny, peso)

                if origen in self.grafo:
                    self.grafo[origen].append(arista_o_d)
                else:
                    self.grafo[origen] = [arista_o_d]
                if destino in self.grafo:
                    self.grafo[destino].append(arista_d_o)
                else:
                    self.grafo[destino] = [arista_d_o]
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )
        
    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.administrador_particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )

    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.administrador_particulas:
            if id == particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setColumnCount(10)
                headers = ["ID", "Origen_x", "Origen_y", "Destino_x", "Destino_y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                origenx_widget = QTableWidgetItem(str(particula.origenx))
                origeny_widget = QTableWidgetItem(str(particula.origeny))
                destinox_widget = QTableWidgetItem(str(particula.destinox))
                destinoy_widget = QTableWidgetItem(str(particula.destinoy))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))
                

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origenx_widget)
                self.ui.tabla.setItem(0, 2, origeny_widget)
                self.ui.tabla.setItem(0, 3, destinox_widget)
                self.ui.tabla.setItem(0, 4, destinoy_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado = True
                return
        
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención!",
                f'La particula con id "{id}" no fue encontrada'
            )


    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "Origen_x", "Origen_y", "Destino_x", "Destino_y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.administrador_particulas))

        row = 0
        for particula in self.administrador_particulas:
            id_widget = QTableWidgetItem(str(particula.id))
            origenx_widget = QTableWidgetItem(str(particula.origenx))
            origeny_widget = QTableWidgetItem(str(particula.origeny))
            destinox_widget = QTableWidgetItem(str(particula.destinox))
            destinoy_widget = QTableWidgetItem(str(particula.destinoy))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origenx_widget)
            self.ui.tabla.setItem(row, 2, origeny_widget)
            self.ui.tabla.setItem(row, 3, destinox_widget)
            self.ui.tabla.setItem(row, 4, destinoy_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1

    def wheelEvent(self, event):
        print(event.delta())
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.administrador_particulas:
            r = particula.red
            g = particula.green
            b = particula.blue

            color = QColor(r, g, b)
            pen.setColor(color)

            origenx = particula.origenx
            origeny = particula.origeny
            destinox = particula.destinox
            destinoy = particula.destinoy

            self.scene.addEllipse(origenx, origeny, 3, 3, pen)
            self.scene.addEllipse(destinox, destinoy, 3, 3, pen)
            self.scene.addLine(origenx+3, origeny+3, destinox, destinoy, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear() 

    @Slot()
    def action_diccionario(self):
        mystr = pformat(self.grafo, width=40, indent=1)
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(mystr))

    @Slot()
    def busqueda_amplitud(self):
        visitados = deque() 
        cola = deque()
        origenx = self.ui.spinBox_13.value()
        origeny = self.ui.spinBox_16.value()

        origen = (origenx, origeny)
        visitados.append(origen)
        cola.append(origen)

        while len(cola) > 0:
            vertice = cola[0]
            print(vertice)
            cola.popleft()

            adyacentes = self.grafo2[vertice]

            for ady in adyacentes:
                if not ady in visitados:
                    visitados.append(ady)
                    cola.append(ady)


    @Slot()
    def busqueda_profundidad(self):
        visitados = deque() 
        pila = deque()
        recorrido = deque()
        origenx = self.ui.spinBox_13.value()
        origeny = self.ui.spinBox_16.value()

        origen = (origenx, origeny)
        visitados.append(origen)
        pila.append(origen)

        while len(pila) > 0:
            vertice = pila[-1]
            recorrido.append(vertice)
            print(vertice)
            pila.pop()

            adyacentes = self.grafo2[vertice]

            for ady in adyacentes:
                if not ady in visitados:
                    visitados.append(ady)
                    pila.append(ady)
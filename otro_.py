#botones = ('C','+/-','%','÷','7','8','9','x','4','5','6','-','1','2','3','+','0','0',',','=')
#botones = (('C', 2), ('+/-',1), ('÷', 1), ('7', 1), ('8', 1), ('9', 1), ('x', 1), ('4', 1), ('5', 1), ('6', 1), ('-', 1), ('1', 1), ('2', 1), ('3', 1), ('+', 1), ('0',2), (',', 1), ('=', 1))
#coordenadar =[]


class Keyboard_con_lista(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width= WIDTH*4, height=HEIGHT*5)
        self.pack_propagate(0)
        s = ttk.Style()
        s.theme_use('alt')

        coordenadas = []
        for fila in range(5):
            for columna in range(4):
                coordenadas.append((fila, columna))

        k = 0
        for tecla, ancho in botones:
            boton = CalcButton(self, tecla, width=ancho)
            boton.grid(row = coordenadas[k][0], column = coordenadas[k][1], columnspan=ancho)
            k += ancho        
        
        
        #self.teclado = ttk.Frame(self, width=calculator.WIDTH*4, height=calculator.HEIGHT*5)
        #self.teclado.grid_propagate(0)
        #self.teclado.pack(side=TOP, fill=BOTH, expand=True)

        '''
        botonC = calculator.CalcButton(self.teclado, 'C')
        botonC.grid(row=0, column=0)

        botonC = calculator.CalcButton(self.teclado, '+/-')
        botonC.grid(row=0, column=1)

        botonC = calculator.CalcButton(self.teclado, '%')
        botonC.grid(row=0, column=2)

        botonC = calculator.CalcButton(self.teclado, '÷')
        botonC.grid(row=0, column=3)
        
        botonC = calculator.CalcButton(self.teclado, '7')
        botonC.grid(row=1, column=0)

        botonC = calculator.CalcButton(self.teclado, '8')
        botonC.grid(row=1, column=1)

        botonC = calculator.CalcButton(self.teclado, '9')
        botonC.grid(row=1, column=2)
        
        botonC = calculator.CalcButton(self.teclado, 'x')
        botonC.grid(row=1, column=3)
        
        botonC = calculator.CalcButton(self.teclado, '4')
        botonC.grid(row=2, column=0)

        botonC = calculator.CalcButton(self.teclado, '5')
        botonC.grid(row=2, column=1)

        botonC = calculator.CalcButton(self.teclado, '6')
        botonC.grid(row=2, column=2)
        
        botonC = calculator.CalcButton(self.teclado, '-')
        botonC.grid(row=2, column=3)
        
        botonC = calculator.CalcButton(self.teclado, '1')
        botonC.grid(row=3, column=0)

        botonC = calculator.CalcButton(self.teclado, '2')
        botonC.grid(row=3, column=1)

        botonC = calculator.CalcButton(self.teclado, '3')
        botonC.grid(row=3, column=2)
        
        botonC = calculator.CalcButton(self.teclado, '+')
        botonC.grid(row=3, column=3)

        botonC = calculator.CalcButton(self.teclado, '0', width=2)
        botonC.grid(row=4, column=0,columnspan = 2)

        botonC = calculator.CalcButton(self.teclado, ',')
        botonC.grid(row=4, column=2)

        botonC = calculator.CalcButton(self.teclado, '=')
        botonC.grid(row=4, column=3)
        '''

        '''
        self.calcButtonC = ttk.Frame(self, width=136, height=50)
        btn = ttk.Button(self.calcButtonC, text= 'C')
        self.calcButtonC.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        #self.calcButtonC.pack(side=TOP)
        self.calcButtonC.grid(column=0,row=1, columnspan=2)
        #self.botonC = ttk.Button(self, text= 'C')
        #self.botonC.pack(side=TOP)

        self.calcButtonCs = ttk.Frame(self, width=68, height=50)
        btn = ttk.Button(self.calcButtonCs, text= '+/-')
        self.calcButtonCs.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        self.calcButtonCs.grid(column=3,row=1)

        self.calcButtondiv = ttk.Frame(self, width=68, height=50)
        btn = ttk.Button(self.calcButtondiv, text= '/')
        self.calcButtondiv.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        self.calcButtondiv.grid(column=4,row=1)
        '''
        
        

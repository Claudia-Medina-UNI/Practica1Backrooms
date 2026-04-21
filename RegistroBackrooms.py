class RegistroNivelBackrooms:
    def _init_(self, numero_nivel, nombre_nivel, clase_seguridad, entidades_totales, habitable):
        self.__numero_nivel = numero_nivel
        self.__nombre_nivel = nombre_nivel
        self.__clase_seguridad = clase_seguridad
        self.__entidades_totales = entidades_totales
        self.__habitable = habitable
        
    def getNumeroNivel(self):
        return self.__numero_nivel
    def setNumeroNivel(self, numero_nivel):
        self.__numero_nivel = numero_nivel

    def getNombreNivel(self):
        return self.__nombre_nivel
    def setNombreNivel(self, nombre_nivel):
        self.__nombre_nivel = nombre_nivel

    def getClaseSeguridad(self):
        return self.__clase_seguridad
    def setClaseSeguridad(self, clase_seguridad):
        self.__clase_seguridad = clase_seguridad

    def getEntidadesTotales(self):
        return self.__entidades_totales
    def setEntidadesTotales(self, entidades_totales):
        self.__entidades_totales = entidades_totales

    def getHabitable(self):
        return self.__habitable
    def setHabitable(self, habitable):
        self.__habitable = habitable
    
    def info(self):
        if self.__habitable == True:
            estado = "[✓] Si es habitable ☻"
        else:
            estado = "[✘] NO, PELIGRO, NO ES HABITABLE ☠"
        print("\n" + "="*40)
        print("╔═══════════════════════════╗")
        print("║ ☣︎ SISTEMA DE ARCHIVOS M.E.G ☣︎ ║")
        print("╚═══════════════════════════╝")
        print(f"Nivel: {self._numero_nivel} - {self._nombre_nivel}")
        print(f"Clasificacion: {self.__clase_seguridad}")
        print(f"Entidades: {self.__entidades_totales}")
        print(f"Habitable: {estado}")
        print("="*40)
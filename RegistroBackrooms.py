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

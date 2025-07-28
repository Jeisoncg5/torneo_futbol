# Proyecto: **Gestión de Torneos Internacionales de Fútbol (Python + JSON)**

------

Jeison Leonardo Cristancho García - J3 

## **Descripción General**

Este proyecto es una **aplicación de Python + JSON** para administrar equipos, jugadores, transferencias y torneos de fútbol. Todo el almacenamiento se hace mediante **archivos JSON **.

------

## **Estructura del Proyecto**

```
torneo_futbol/
├── main.py  
│
├── app/
│   └── config.py                  
│
├── controllers/               
│   ├── equipos.py              
│   ├── jugadores.py           
│   ├── torneos.py
│   ├── transferencias.py       
│   └── estadisticas.py       
│
├── utils/
│   └── corefiles.py         
│   └── screenControllers.py
│   └── validateData.py
│
├── data/                      
│   ├── equipos.json
│   ├── jugadores.json
│   ├── dirigentes.json
│   ├── ligas.json
│   ├── torneos.json
│   ├── partidos.json
│   └── transferencias.json
│
└── README.md                  
```

------

## **Menús del programa**

Aquí observaremos como se organizaron  los menús  del programa en todos los archivos

​                            **GESTOR DE TORNEOS **(Menú principal)

1. Registrar equipo
2. Listar equipos
3. Registrar jugador
4. Listar jugadores
5. Transferencia de jugador (venta/préstamo)
6. Estadísticas 
7. Administrar torneos
8. Salir



​                    **ADMINISTRACIÓN DE TORNEOS **(Sub menú de administrar torneos)

1. Registrar partido
2. Ver tabla de posiciones (Función fase beta no incluida)
3. Volver al menú principal



##  Funcionalidades

###  1. Registro de Equipos
Permite ingresar:
- Nombre del equipo
- Fecha de fundación
- País
- ID de liga (opcional)

---

###  2. Registro de Jugadores
Permite registrar jugadores asignándolos a un equipo:
- Nombre
- Posición
- Número Dorsal
- ID del equipo

---

### 3. Transferencias
Permite mover un jugador entre equipos como:
- Venta (se actualiza el equipo)
- Préstamo (no se cambia el equipo)

Guarda:
- Fecha
- Jugador
- Equipo origen y destino
- Tipo

---

### 4. Estadísticas Generales
- Total de equipos
- Total de jugadores
- Jugadores por equipo
- Transferencias realizadas

---

### 5. Torneos y Tabla de Posiciones
Permite:
- Registrar partidos entre equipos (con goles)
- Calcular automáticamente:
  - PJ, PG, PE, PP, GF, GC,Puntos


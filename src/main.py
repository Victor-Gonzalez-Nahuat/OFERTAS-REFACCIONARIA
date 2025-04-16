import flet as ft
import requests
from datetime import datetime

API_URL_OFERTAS = "https://api-refaccionaria-production.up.railway.app/ofertas"

def formatear_fecha(fecha):

    fecha_str = str(fecha)
    if len(fecha_str) == 6:
        try:
            anio = int(fecha_str[:2]) + 2000
            mes = int(fecha_str[2:4])
            dia = int(fecha_str[4:])
            return f"{dia:02d}/{mes:02d}/{anio}"
        except Exception as ex:
            return "Fecha inválida"
    return fecha

def main(page: ft.Page):
    page.title = "Ofertas Refaccionaria Falla"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.bgcolor = ft.colors.WHITE

    header = ft.Container(
        content=ft.Column([
            ft.Row(
            controls=[
                ft.Image(
                    src="https://i.ibb.co/8LxBQKh2/images.png",
                    width=60,
                    height=60,
                    fit=ft.ImageFit.CONTAIN
                ),
                ft.Text("REFACCIONARIA FALLA", size=26, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Text("Ofertas del Catálogo", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)
        ]),
        padding=20,
        bgcolor="#e9423a",
        border_radius=ft.BorderRadius(bottom_left=20, bottom_right=20, top_left=0, top_right=0)
    )

    ofertas_container = ft.Column(spacing=20, scroll=ft.ScrollMode.AUTO)

    def cargar_ofertas(e):
        try:
            response = requests.get(API_URL_OFERTAS)
            if response.status_code == 200:
                ofertas = response.json() 
                if not ofertas:
                    ofertas_container.controls = [ft.Text("No hay ofertas vigentes en este momento.", size=18)]
                else:
                    tarjetas = []
                    for oferta in ofertas:
                        fecha_vigencia = formatear_fecha(oferta.get("fecha", ""))
                        imagen_src = oferta.get("imagen", None)
                        imagen_control = ft.Row([
                            ft.Image(src=imagen_src, width=150, height=150, fit=ft.ImageFit.CONTAIN) if imagen_src else ft.Container(width=150, height=150, bgcolor=ft.colors.GREY_300)
                            ], alignment=ft.MainAxisAlignment.CENTER
                            )
                        
                        tarjeta = ft.Card(
                            content=ft.Container(
                                padding=20,
                                content=ft.Column([
                                    imagen_control,
                                    ft.Text(f"{oferta.get('nombre')}"),
                                    ft.Text(f"Vigencia: {fecha_vigencia}"),
                                    ft.Text(f"Observaciones: {oferta.get('observaciones', 'Sin observaciones')}", size=14),
                                    ft.Text(f"Código: {oferta.get('codigo', 'N/A')}", weight=ft.FontWeight.BOLD),
                                ], spacing=10),
                            ),
                            width=350,
                            elevation=4,
                        )
                        tarjetas.append(tarjeta)
                    
                    ofertas_container.controls = tarjetas
            else:
                ofertas_container.controls = [ft.Text("Error al obtener las ofertas.", size=18)]
        except Exception as ex:
            ofertas_container.controls = [ft.Text(f"Error: {str(ex)}", size=18)]
        page.update()

    btn_recargar = ft.ElevatedButton("Recargar Ofertas", on_click=cargar_ofertas, bgcolor=ft.colors.BLUE)

    page.add(header, 
             ft.Row([
                 ft.Column([
                     ofertas_container
                 ], height=500, scroll=ft.ScrollMode.AUTO)
             ], alignment= ft.MainAxisAlignment.CENTER)
             )

    cargar_ofertas(None)

ft.app(target=main)

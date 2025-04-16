import flet as ft
import requests

API_URL = "https://api-refaccionaria-production.up.railway.app/producto/"

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.RED)
    page.title = "Ofertas Refaccionaria Falla"
    page.padding = 10

    

    logo = ft.Image(
    src="https://i.ibb.co/8LxBQKh2/images.png", 
    width=60,
    height=60,
    fit=ft.ImageFit.CONTAIN
    )

    titulo_empresa = ft.Text(
        "REFACCIONARIA FALLA",
        size=26,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.WHITE
    )
    titulo = ft.Text("Ofertas del Catalogo", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    encabezado = ft.Container(
        content=ft.Column([
            ft.Row([
                logo,
                titulo_empresa
            ]),
            titulo,
        ]),
        padding=20,
        bgcolor="#e9423a",
        border_radius=ft.BorderRadius(top_left=0, top_right=0, bottom_left= 20, bottom_right= 20),  # Esquinas inferiores redondeadas
    )
    resultado_card = ft.Container(
        ft.Row([
            ft.Image(
            src="https://i.ibb.co/8LxBQKh2/images.png", 
            width=250,
            height=250,
            fit=ft.ImageFit.CONTAIN
            )
        ], alignment=ft.MainAxisAlignment.CENTER))


    page.add(
        ft.Column([
            encabezado,
            ft.Column([
                resultado_card
            ], scroll=ft.ScrollMode.AUTO, height=400)
        ], spacing=20)
    )

ft.app(target=main)

import flet as ft
import hashlib, hmac

DEMO_SALT = b"ubuntuhub-demo-salt"
DEMO_HASH = "119e0b98e877db9ed05ff9d81c24b4fb51ad7028a9bed73b835e0a5a10e4025a"
DEMO_EMAIL = "demo_user@gmail.com"


def hash_password(password):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), DEMO_SALT, 100_000).hex()


def check_login(email, password):
    if not email or not password:
        return False
    email = email.strip().lower()
    return email == DEMO_EMAIL and hmac.compare_digest(hash_password(password), DEMO_HASH)


def login(page: ft.Page):

    email_field = ft.TextField(label="email", value=DEMO_EMAIL, filled=True)
    password_field = ft.TextField(label="password", filled=True, password=True, can_reveal_password=True)
    error_text = ft.Text("Wrong email or password", color=ft.Colors.RED_400, visible=False)

    def logged_in(e):
        if check_login(email_field.value, password_field.value):
            error_text.visible = False
            page.navigate("/home")
        else:
            error_text.visible = True
            page.update()

    login_form = ft.Column(
        expand=True,
        controls=[
            ft.Text("UbuntuHub", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("I am because we are", size=16, color=ft.Colors.GREY_800),
            email_field,
            password_field,
            error_text,
            ft.FilledButton("log in", on_click=logged_in),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return ft.View(
        route="/login",
        controls=[
            ft.Row(
                expand=True,
                controls=[login_form],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
    )
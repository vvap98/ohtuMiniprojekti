import reflex as rx

config = rx.Config(
    app_name="viitturi",
    app_module_import="viitturi.main",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ]
)

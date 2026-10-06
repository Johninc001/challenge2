from nicegui import app, ui
import encrypt

@ui.page('/')
def index():
    app.storage.user['count'] = app.storage.user.get('count', 0) + 1
    if app.storage.user['count'] == 1:
        ui.label('Welcome to your first visit!')
        key=encrypt.get_key()
        try:
            app.storage.user['key']=key
        except Exception as e:
            ui.label(f'Error occurred: {e}')
        ui.label(f'Your key is: {key}')
    else:
        ui.label(f'Welcome back! You have visited this page {app.storage.user["count"]} times.')
        try:
            key=app.storage.user['key']
        except Exception as e:
            ui.label(f'Error occurred: {e}')
            print("storage error:", e)
    with ui.card():   
        with ui.row():
            ui.label('your own page visits:')
            ui.label().bind_text_from(app.storage.user, 'count')

ui.run(storage_secret='private key to secure the browser session cookie')
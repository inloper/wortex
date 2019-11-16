# Creates an application instance and runs on dev server

if __name__ == '__main__':
    from application import create_app
    app = create_app()
    app.run()
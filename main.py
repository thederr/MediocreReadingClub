from website import create_app;

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) 
    ### debug = true is for testing only. reruns the web server when changes are made ####


def config_logger(app):
    import logging
    from logging.handlers import RotatingFileHandler
    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)

    # Setup the file handler object
    flasklog_handler = RotatingFileHandler('app.log', maxBytes=32768, backupCount=30)

dict_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'kettle_logs.log',
            'formatter': 'base'
        }
    },
    'formatters': {
        'base': {
            'format': '%(asctime)s - %(message)s'
        }
    },
    'loggers': {
        'kettle_logger': {
            'handlers': ['file_handler'],
            'level': 'INFO'
        }
    }
}

class Config:
	SECRET_KEY = 'caee0c7010e55f0340b475babe839928'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = None
	MAIL_PASSWORD = None
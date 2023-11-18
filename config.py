import os


class Config:
    """Configurações base que são comuns a todos os ambientes."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma_chave_secreta_bem_segura'
    # Outras configurações globais podem ser incluídas aqui


class DevelopmentConfig(Config):
    """Configurações para o ambiente de desenvolvimento."""
    DEBUG = True
    # Configurações específicas para o desenvolvimento, como URL do banco de dados
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or 'mongodb://localhost:27017/meu_banco_dev'


class TestingConfig(Config):
    """Configurações para o ambiente de testes."""
    TESTING = True
    # Configurações específicas para testes
    DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or 'mongodb://localhost:27017/meu_banco_test'


class ProductionConfig(Config):
    """Configurações para o ambiente de produção."""
    DEBUG = False
    # Configurações específicas para produção, como URL do banco de dados
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'mongodb://localhost:27017/meu_banco_prod'


# Um dicionário para mapear os nomes de configuração para as classes de configuração
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
